"""Generate static HTML dashboard from trading bot data.

Reads all JSON/CSV data files and produces a self-contained docs/index.html
with embedded data, Chart.js charts, and responsive dark-theme layout.
Deployed to GitHub Pages for access from any device.
"""

import json
import re
import html
from datetime import date
from pathlib import Path

BASE_DIR = Path(__file__).parent


def load_json(path, default=None):
    """Load a JSON file, returning default on failure."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default if default is not None else {}


def load_text(path):
    """Load a text file, returning empty string on failure."""
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def markdown_to_html(md_text):
    """Simple markdown to HTML conversion (no external deps)."""
    if not md_text:
        return "<p>No daily report available.</p>"

    lines = md_text.split("\n")
    html_lines = []
    in_table = False
    in_list = False

    for line in lines:
        stripped = line.strip()

        # Headers
        if stripped.startswith("# "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h2>{_inline(stripped[2:])}</h2>")
        elif stripped.startswith("## "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h3>{_inline(stripped[3:])}</h3>")
        elif stripped.startswith("### "):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f"<h4>{_inline(stripped[4:])}</h4>")
        # Horizontal rule
        elif stripped.startswith("---"):
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append("<hr>")
        # Table rows
        elif "|" in stripped and not stripped.startswith("```"):
            if stripped.replace("|", "").replace("-", "").replace(" ", "") == "":
                continue  # separator row
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            if not in_table:
                html_lines.append('<table class="report-table"><tbody>')
                in_table = True
            html_lines.append("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in cells) + "</tr>")
        else:
            if in_table:
                html_lines.append("</tbody></table>")
                in_table = False

            # List items
            if stripped.startswith("- ") or stripped.startswith("* "):
                if not in_list:
                    html_lines.append("<ul>")
                    in_list = True
                html_lines.append(f"<li>{_inline(stripped[2:])}</li>")
            elif stripped.startswith(tuple(f"{i}." for i in range(1, 20))):
                if not in_list:
                    html_lines.append("<ul>")
                    in_list = True
                text = re.sub(r"^\d+\.\s*", "", stripped)
                html_lines.append(f"<li>{_inline(text)}</li>")
            elif stripped == "":
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
            else:
                if in_list:
                    html_lines.append("</ul>")
                    in_list = False
                html_lines.append(f"<p>{_inline(stripped)}</p>")

    if in_table:
        html_lines.append("</tbody></table>")
    if in_list:
        html_lines.append("</ul>")

    return "\n".join(html_lines)


def _inline(text):
    """Convert inline markdown (bold, code) to HTML."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    text = re.sub(r"✓", r'<span class="check">&#10003;</span>', text)
    return text


def generate():
    """Generate the dashboard HTML file."""
    # Load all data
    positions = load_json(BASE_DIR / "positions.json", {})
    config = load_json(BASE_DIR / "config.json", {})
    run_status = load_json(BASE_DIR / "output" / "run_status.json", {})
    trade_plan = load_json(BASE_DIR / "output" / "trade_plan.json", {})
    trade_log = load_json(BASE_DIR / "logs" / "trade_log.json", [])
    trade_log_update = load_json(BASE_DIR / "output" / "trade_log_update.json", {})
    equity_history = load_json(BASE_DIR / "equity_history.json", [])
    daily_report_md = load_text(BASE_DIR / "output" / "daily_report.md")

    # Compute summary values
    equity = positions.get("equity_value_gbp", 100)
    cash = positions.get("cash_balance_gbp", 100)
    peak = positions.get("portfolio_peak_equity_gbp", 100)
    starting_capital = 100.0
    total_pnl = equity - starting_capital
    total_pnl_pct = (total_pnl / starting_capital) * 100
    drawdown_pct = (peak - equity) / peak * 100 if peak > 0 else 0
    pos_list = positions.get("positions", [])
    as_of = positions.get("as_of_date", "N/A")
    status = run_status.get("status", "UNKNOWN")
    max_positions = config.get("max_positions", 5)

    # Candidates from trade plan
    candidates = trade_plan.get("candidates_considered", [])

    # Flatten trade log entries
    all_trades = []
    for entry in trade_log:
        if isinstance(entry, dict) and "entries" in entry:
            for e in entry["entries"]:
                e["date"] = entry.get("as_of_date", "")
                all_trades.append(e)
        elif isinstance(entry, dict):
            all_trades.append(entry)

    # Sector allocation
    sectors = {}
    for p in pos_list:
        sector = p.get("sector", "Unknown")
        sectors[sector] = sectors.get(sector, 0) + p.get("market_value_gbp", 0)
    if cash > 0:
        sectors["Cash"] = cash

    # Convert daily report
    daily_report_html = markdown_to_html(daily_report_md)

    # Build HTML
    html_content = _build_html(
        equity=equity,
        cash=cash,
        total_pnl=total_pnl,
        total_pnl_pct=total_pnl_pct,
        drawdown_pct=drawdown_pct,
        pos_list=pos_list,
        as_of=as_of,
        status=status,
        max_positions=max_positions,
        equity_history=equity_history,
        sectors=sectors,
        candidates=candidates,
        all_trades=all_trades,
        daily_report_html=daily_report_html,
    )

    # Write output
    docs_dir = BASE_DIR / "docs"
    docs_dir.mkdir(exist_ok=True)
    with open(docs_dir / "index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Dashboard generated: docs/index.html ({len(html_content)} bytes)")


def _build_html(**data):
    """Build the complete HTML string."""
    pnl_color = "#4ade80" if data["total_pnl"] >= 0 else "#f87171"
    pnl_sign = "+" if data["total_pnl"] >= 0 else ""
    status_color = {"OK": "#4ade80", "NO_TRADES": "#facc15", "BLOCKED": "#f87171"}.get(
        data["status"], "#94a3b8"
    )

    # Positions table rows
    pos_rows = ""
    for p in data["pos_list"]:
        pnl = p.get("unrealised_pnl_gbp", 0)
        pnl_c = "#4ade80" if pnl >= 0 else "#f87171"
        cost = p.get("avg_cost_gbp", 0)
        mv = p.get("market_value_gbp", 0)
        pnl_pct = (pnl / (cost * p.get("quantity", 1)) * 100) if cost > 0 and p.get("quantity", 0) > 0 else 0
        stop = p.get("current_stop_gbp")
        stop_str = f"£{stop:.2f}" if stop else "—"
        pos_rows += f"""<tr>
            <td><strong>{p.get('ticker','')}</strong></td>
            <td>{p.get('sector','')}</td>
            <td>{p.get('quantity',0):.4f}</td>
            <td>£{cost:.2f}</td>
            <td>£{mv:.2f}</td>
            <td style="color:{pnl_c}">£{pnl:+.2f} ({pnl_pct:+.1f}%)</td>
            <td>{p.get('days_held',0)}</td>
            <td>{stop_str}</td>
        </tr>"""

    if not data["pos_list"]:
        pos_rows = '<tr><td colspan="8" style="text-align:center;color:#64748b">No positions held</td></tr>'

    # Candidates rows
    cand_rows = ""
    for c in data["candidates"][:5]:
        conf = c.get("confidence", 0)
        conf_bar_w = int(conf * 100)
        trend = c.get("trend_status", "—")
        entry = c.get("entry_type", "—")
        reason = c.get("rejected_reason") or "Accepted"
        reason_c = "#f87171" if c.get("rejected_reason") else "#4ade80"
        cand_rows += f"""<tr>
            <td><strong>{c.get('ticker','')}</strong></td>
            <td>{entry}</td>
            <td>{trend}</td>
            <td><div class="conf-bar"><div class="conf-fill" style="width:{conf_bar_w}%"></div><span>{conf:.2f}</span></div></td>
            <td style="color:{reason_c}">{html.escape(str(reason)[:60])}</td>
        </tr>"""

    if not data["candidates"]:
        cand_rows = '<tr><td colspan="5" style="text-align:center;color:#64748b">No candidates evaluated</td></tr>'

    # Trade history rows
    trade_rows = ""
    for t in reversed(data["all_trades"][-20:]):
        action = t.get("action", "")
        action_c = "#4ade80" if action == "BUY" else "#f87171" if action == "SELL" else "#94a3b8"
        trade_rows += f"""<tr>
            <td>{t.get('date','')}</td>
            <td><strong>{t.get('ticker','')}</strong></td>
            <td style="color:{action_c}">{action}</td>
            <td>£{t.get('planned_price_gbp',0):.2f}</td>
            <td>{t.get('planned_quantity',0):.4f}</td>
            <td>{t.get('confidence',0):.2f}</td>
            <td>{t.get('entry_type','')}</td>
        </tr>"""

    if not data["all_trades"]:
        trade_rows = '<tr><td colspan="7" style="text-align:center;color:#64748b">No trades yet</td></tr>'

    # JSON data for charts
    equity_json = json.dumps(data["equity_history"])
    sector_labels = json.dumps(list(data["sectors"].keys()))
    sector_values = json.dumps([round(v, 2) for v in data["sectors"].values()])
    sector_colors = json.dumps(_sector_colors(list(data["sectors"].keys())))

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Daily Equity Trader</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4"></script>
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ background:#0f1117; color:#e2e8f0; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',system-ui,sans-serif; padding:16px; max-width:1200px; margin:0 auto; }}
h1 {{ font-size:1.4rem; margin-bottom:4px; }}
.subtitle {{ color:#64748b; font-size:0.85rem; margin-bottom:20px; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(160px,1fr)); gap:12px; margin-bottom:24px; }}
.card {{ background:#1a1d25; border-radius:10px; padding:16px; }}
.card-label {{ font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; color:#64748b; margin-bottom:4px; }}
.card-value {{ font-size:1.5rem; font-weight:700; }}
.card-sub {{ font-size:0.75rem; color:#64748b; margin-top:2px; }}
.section {{ background:#1a1d25; border-radius:10px; padding:20px; margin-bottom:16px; }}
.section-title {{ font-size:1rem; font-weight:600; margin-bottom:12px; color:#94a3b8; text-transform:uppercase; letter-spacing:1px; font-size:0.75rem; }}
table {{ width:100%; border-collapse:collapse; font-size:0.8rem; }}
th {{ text-align:left; padding:8px; color:#64748b; border-bottom:1px solid #2d3343; font-size:0.7rem; text-transform:uppercase; letter-spacing:1px; }}
td {{ padding:8px; border-bottom:1px solid #1e2230; }}
.charts {{ display:grid; grid-template-columns:2fr 1fr; gap:16px; margin-bottom:16px; }}
@media(max-width:768px) {{ .charts {{ grid-template-columns:1fr; }} }}
canvas {{ max-height:300px; }}
.conf-bar {{ position:relative; background:#1e2230; border-radius:4px; height:20px; overflow:hidden; min-width:80px; }}
.conf-fill {{ background:#3b82f6; height:100%; border-radius:4px; }}
.conf-bar span {{ position:absolute; right:6px; top:2px; font-size:0.7rem; }}
.report-section {{ max-height:500px; overflow-y:auto; }}
.report-section h2 {{ font-size:1rem; color:#e2e8f0; margin:16px 0 8px; }}
.report-section h3 {{ font-size:0.9rem; color:#94a3b8; margin:12px 0 6px; }}
.report-section h4 {{ font-size:0.85rem; color:#94a3b8; margin:10px 0 4px; }}
.report-section p {{ font-size:0.8rem; line-height:1.5; margin-bottom:8px; color:#cbd5e1; }}
.report-section ul {{ padding-left:20px; margin-bottom:8px; }}
.report-section li {{ font-size:0.8rem; line-height:1.5; color:#cbd5e1; margin-bottom:2px; }}
.report-section hr {{ border:none; border-top:1px solid #2d3343; margin:16px 0; }}
.report-section code {{ background:#2d3343; padding:1px 4px; border-radius:3px; font-size:0.75rem; }}
.report-section .report-table {{ margin:8px 0; }}
.report-section .report-table td {{ font-size:0.75rem; padding:4px 8px; }}
.check {{ color:#4ade80; }}
details {{ cursor:pointer; }}
details summary {{ font-size:0.85rem; color:#60a5fa; padding:4px 0; }}
.status-badge {{ display:inline-block; padding:2px 10px; border-radius:12px; font-size:0.7rem; font-weight:600; letter-spacing:1px; }}
</style>
</head>
<body>
<h1>Daily Equity Trader</h1>
<div class="subtitle">Paper Trading | FTSE 100 | Last updated: {data['as_of']} | Status: <span class="status-badge" style="background:{status_color}22;color:{status_color}">{data['status']}</span></div>

<div class="cards">
    <div class="card">
        <div class="card-label">Equity</div>
        <div class="card-value">£{data['equity']:.2f}</div>
        <div class="card-sub" style="color:{pnl_color}">{pnl_sign}£{data['total_pnl']:.2f} ({pnl_sign}{data['total_pnl_pct']:.1f}%)</div>
    </div>
    <div class="card">
        <div class="card-label">Cash</div>
        <div class="card-value">£{data['cash']:.2f}</div>
    </div>
    <div class="card">
        <div class="card-label">Drawdown</div>
        <div class="card-value" style="color:{'#f87171' if data['drawdown_pct'] > 5 else '#facc15' if data['drawdown_pct'] > 0 else '#4ade80'}">{data['drawdown_pct']:.1f}%</div>
        <div class="card-sub">Limit: 15%</div>
    </div>
    <div class="card">
        <div class="card-label">Positions</div>
        <div class="card-value">{len(data['pos_list'])} / {data['max_positions']}</div>
    </div>
</div>

<div class="charts">
    <div class="section">
        <div class="section-title">Equity Curve</div>
        <canvas id="equityChart"></canvas>
    </div>
    <div class="section">
        <div class="section-title">Allocation</div>
        <canvas id="sectorChart"></canvas>
    </div>
</div>

<div class="section">
    <div class="section-title">Positions</div>
    <div style="overflow-x:auto">
    <table>
        <thead><tr><th>Ticker</th><th>Sector</th><th>Qty</th><th>Avg Cost</th><th>Mkt Value</th><th>P&L</th><th>Days</th><th>Stop</th></tr></thead>
        <tbody>{pos_rows}</tbody>
    </table>
    </div>
</div>

<div class="section">
    <div class="section-title">Today's Candidates</div>
    <div style="overflow-x:auto">
    <table>
        <thead><tr><th>Ticker</th><th>Entry</th><th>Trend</th><th>Confidence</th><th>Status</th></tr></thead>
        <tbody>{cand_rows}</tbody>
    </table>
    </div>
</div>

<div class="section">
    <div class="section-title">Trade History</div>
    <div style="overflow-x:auto">
    <table>
        <thead><tr><th>Date</th><th>Ticker</th><th>Action</th><th>Price</th><th>Qty</th><th>Confidence</th><th>Type</th></tr></thead>
        <tbody>{trade_rows}</tbody>
    </table>
    </div>
</div>

<div class="section">
    <div class="section-title">Daily Report</div>
    <details>
        <summary>Expand Claude's full analysis</summary>
        <div class="report-section">{data['daily_report_html']}</div>
    </details>
</div>

<div style="text-align:center;color:#475569;font-size:0.7rem;margin-top:24px;padding-bottom:16px">
    Daily Equity Trader | Paper Trading | Not financial advice
</div>

<script>
const equityData = {equity_json};
const sectorLabels = {sector_labels};
const sectorValues = {sector_values};
const sectorColors = {sector_colors};

// Equity curve
if (equityData.length > 0) {{
    new Chart(document.getElementById('equityChart'), {{
        type: 'line',
        data: {{
            labels: equityData.map(d => d.date),
            datasets: [{{
                label: 'Equity (£)',
                data: equityData.map(d => d.equity_gbp),
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59,130,246,0.1)',
                fill: true,
                tension: 0.3,
                pointRadius: equityData.length > 30 ? 0 : 3,
            }}, {{
                label: 'Starting Capital',
                data: equityData.map(() => 100),
                borderColor: '#475569',
                borderDash: [5,5],
                pointRadius: 0,
                fill: false,
            }}]
        }},
        options: {{
            responsive: true,
            plugins: {{ legend: {{ labels: {{ color: '#94a3b8', font: {{ size: 11 }} }} }} }},
            scales: {{
                x: {{ ticks: {{ color: '#64748b', maxRotation: 45, font: {{ size: 10 }} }}, grid: {{ color: '#1e2230' }} }},
                y: {{ ticks: {{ color: '#64748b', callback: v => '£' + v, font: {{ size: 10 }} }}, grid: {{ color: '#1e2230' }} }}
            }}
        }}
    }});
}} else {{
    document.getElementById('equityChart').parentElement.innerHTML += '<p style="color:#64748b;font-size:0.8rem;text-align:center;margin-top:40px">No equity history yet. Data will appear after the first run.</p>';
}}

// Sector allocation
if (sectorValues.length > 0) {{
    new Chart(document.getElementById('sectorChart'), {{
        type: 'doughnut',
        data: {{
            labels: sectorLabels,
            datasets: [{{ data: sectorValues, backgroundColor: sectorColors, borderWidth: 0 }}]
        }},
        options: {{
            responsive: true,
            plugins: {{
                legend: {{ position: 'bottom', labels: {{ color: '#94a3b8', font: {{ size: 10 }}, padding: 8 }} }}
            }}
        }}
    }});
}}
</script>
</body>
</html>"""


def _sector_colors(sectors):
    """Assign colors to sectors."""
    palette = {
        "Cash": "#475569",
        "Energy": "#f97316",
        "Healthcare": "#22c55e",
        "Financials": "#3b82f6",
        "Consumer Staples": "#a855f7",
        "Materials": "#eab308",
        "Industrials": "#06b6d4",
        "Utilities": "#14b8a6",
        "Telecom": "#ec4899",
        "Broad Market": "#6366f1",
        "UK Market": "#8b5cf6",
        "UK Mid Cap": "#d946ef",
        "US Market": "#0ea5e9",
        "Commodities": "#f59e0b",
    }
    default = ["#64748b", "#94a3b8", "#cbd5e1", "#e2e8f0"]
    colors = []
    di = 0
    for s in sectors:
        if s in palette:
            colors.append(palette[s])
        else:
            colors.append(default[di % len(default)])
            di += 1
    return colors


if __name__ == "__main__":
    generate()
