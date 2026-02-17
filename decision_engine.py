"""Claude API decision engine.

Assembles input files, calls Claude with the V2 system prompt,
and parses the structured outputs (trade_plan.json, orders.csv, etc.).
"""

import json
import logging
import os
import re
from pathlib import Path

from anthropic import Anthropic

log = logging.getLogger(__name__)
BASE_DIR = Path(__file__).parent


def load_system_prompt():
    """Load V2 system prompt from system_prompt.txt."""
    path = BASE_DIR / "system_prompt.txt"
    with open(path) as f:
        return f.read()


def assemble_user_message(config, market_data_csv, positions_json,
                          universe_csv, trading_calendar_json,
                          signals_json=None):
    """Build the user message containing all input files.

    Each file is clearly delimited so Claude can parse them.
    """
    sections = [
        f"=== config.json ===\n{json.dumps(config, indent=2)}",
        f"=== market_data.csv ===\n{market_data_csv}",
        f"=== positions.json ===\n{positions_json}",
        f"=== universe.csv ===\n{universe_csv}",
        f"=== trading_calendar.json ===\n{trading_calendar_json}",
    ]

    if signals_json:
        sections.append(f"=== signals.json ===\n{signals_json}")

    sections.append(
        "\n--- OUTPUT INSTRUCTIONS ---\n"
        "Output each file delimited by === filename === headers, "
        "in this exact order:\n"
        "=== run_status.json ===\n"
        "=== trade_plan.json ===\n"
        "=== orders.csv ===\n"
        "=== daily_report.md ===\n"
        "=== trade_log_update.json ===\n"
        "Output valid JSON for .json files (no markdown code fences). "
        "Output raw CSV for orders.csv. Output raw markdown for daily_report.md."
    )

    return "\n\n".join(sections)


def call_claude(system_prompt, user_message, config):
    """Call Claude API and return the full response text.

    Uses config['claude_model'] and config['claude_max_tokens'].
    API key from ANTHROPIC_API_KEY environment variable.
    """
    client = Anthropic()

    model = config.get("claude_model", "claude-haiku-4-5-20251001")
    max_tokens = config.get("claude_max_tokens", 8000)

    log.info("Calling Claude API (model=%s, max_tokens=%d)...", model, max_tokens)
    log.info("System prompt: %d chars, User message: %d chars",
             len(system_prompt), len(user_message))

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )

    response_text = response.content[0].text
    log.info("Claude response: %d chars, stop_reason=%s",
             len(response_text), response.stop_reason)
    log.info("Token usage: input=%d, output=%d",
             response.usage.input_tokens, response.usage.output_tokens)

    return response_text


def parse_outputs(response_text):
    """Parse Claude's response into structured outputs.

    Looks for === filename === delimiters and extracts content between them.

    Returns dict with keys:
    - run_status: dict (parsed JSON)
    - trade_plan: dict (parsed JSON)
    - orders_csv: str (raw CSV)
    - daily_report: str (raw markdown)
    - trade_log_update: dict (parsed JSON)
    """
    outputs = {}

    # Split on === filename === pattern
    sections = re.split(r"===\s*(\S+\.(?:json|csv|md))\s*===", response_text)

    # sections alternates: [preamble, filename1, content1, filename2, content2, ...]
    file_contents = {}
    for i in range(1, len(sections) - 1, 2):
        filename = sections[i].strip()
        content = sections[i + 1].strip()
        file_contents[filename] = content

    # Parse each expected output
    outputs["run_status"] = _parse_json_section(
        file_contents.get("run_status.json", ""), "run_status.json"
    )
    outputs["trade_plan"] = _parse_json_section(
        file_contents.get("trade_plan.json", ""), "trade_plan.json"
    )
    outputs["orders_csv"] = file_contents.get("orders.csv", "")
    outputs["daily_report"] = file_contents.get("daily_report.md", "")
    outputs["trade_log_update"] = _parse_json_section(
        file_contents.get("trade_log_update.json", ""), "trade_log_update.json"
    )

    # Log what we got
    for key, val in outputs.items():
        if val:
            log.info("  Parsed %s: %s", key,
                     f"{len(val)} chars" if isinstance(val, str) else "OK")
        else:
            log.warning("  Missing or empty: %s", key)

    return outputs


def _parse_json_section(text, name):
    """Parse a JSON section, handling possible markdown code fences."""
    if not text:
        log.warning("Empty section: %s", name)
        return {}

    # Remove markdown code fences if present
    cleaned = re.sub(r"```(?:json)?\s*", "", text)
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as e:
        log.error("Failed to parse %s: %s", name, e)
        log.error("Content preview: %s", cleaned[:200])

        # Try to extract JSON object from the text
        match = re.search(r"\{[\s\S]*\}", cleaned)
        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

        return {}


def run_decision_engine(config, base_dir):
    """Main entry point for the decision engine.

    1. Load system prompt
    2. Read input files from disk
    3. Assemble user message
    4. Call Claude API
    5. Parse outputs
    6. Write output files to output/ directory

    Returns the parsed outputs dict.
    """
    base_dir = Path(base_dir)

    # Load system prompt
    system_prompt = load_system_prompt()

    # Read input files
    market_data_csv = (base_dir / "data" / "market_data.csv").read_text()
    positions_json = (base_dir / "positions.json").read_text()
    universe_csv = (base_dir / "universe.csv").read_text()
    trading_cal_json = (base_dir / "data" / "trading_calendar.json").read_text()

    # Optional signals
    signals_json = None
    signals_path = base_dir / "data" / "signals.json"
    if signals_path.exists():
        signals_json = signals_path.read_text()

    # Assemble and call
    user_message = assemble_user_message(
        config, market_data_csv, positions_json,
        universe_csv, trading_cal_json, signals_json
    )

    response_text = call_claude(system_prompt, user_message, config)

    # Parse outputs
    outputs = parse_outputs(response_text)

    # Write output files
    output_dir = base_dir / "output"
    output_dir.mkdir(exist_ok=True)

    if outputs.get("run_status"):
        with open(output_dir / "run_status.json", "w", encoding="utf-8") as f:
            json.dump(outputs["run_status"], f, indent=2)

    if outputs.get("trade_plan"):
        with open(output_dir / "trade_plan.json", "w", encoding="utf-8") as f:
            json.dump(outputs["trade_plan"], f, indent=2)

    if outputs.get("orders_csv"):
        with open(output_dir / "orders.csv", "w", encoding="utf-8") as f:
            f.write(outputs["orders_csv"])
    else:
        # Write header-only orders.csv
        with open(output_dir / "orders.csv", "w", encoding="utf-8") as f:
            f.write("order_id,ticker,side,order_type,quantity,limit_price_gbp,"
                    "time_in_force,stop_price_gbp,reason\n")

    if outputs.get("daily_report"):
        with open(output_dir / "daily_report.md", "w", encoding="utf-8") as f:
            f.write(outputs["daily_report"])

    if outputs.get("trade_log_update"):
        with open(output_dir / "trade_log_update.json", "w", encoding="utf-8") as f:
            json.dump(outputs["trade_log_update"], f, indent=2)

    # Save raw response for debugging
    with open(output_dir / "raw_response.txt", "w", encoding="utf-8") as f:
        f.write(response_text)

    return outputs
