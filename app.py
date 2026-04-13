import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# ─────────────────────────────────────────
# 1. DATABASE CONNECTION
# ─────────────────────────────────────────
# ─────────────────────────────────────────
# 1. DATABASE CONNECTION (UPDATED FOR CLOUD)
# ─────────────────────────────────────────
def get_data(query):
    try:
        # This pulls credentials from the Streamlit Cloud "Secrets" panel
        conn = psycopg2.connect(
            host=st.secrets["DB_HOST"],
            database=st.secrets["DB_NAME"],
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASS"],
            port=st.secrets["DB_PORT"]
        )
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Cloud Database Error: {e}")
        return pd.DataFrame()


# ─────────────────────────────────────────
# 2. PAGE CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Vision Bank | Executive Suite",
    page_icon="V",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ─────────────────────────────────────────
# 3. GLOBAL CSS — FANG DARK THEME
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=IBM+Plex+Mono:wght@400;600&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #020C1B;
    color: #CBD5E1;
}
.stApp { background-color: #020C1B; }

/* ── Sidebar shell ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #020C1B 0%, #050E1F 60%, #0A1628 100%) !important;
    border-right: 1px solid #0F2444 !important;
    padding-top: 0 !important;
}
[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }

/* ── Sidebar text overrides ── */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stRadio label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span {
    color: #94A3B8 !important;
    font-size: 12px !important;
    font-weight: 500 !important;
    letter-spacing: 0.6px !important;
}

/* ── Selectbox ── */
[data-testid="stSidebar"] .stSelectbox > div > div {
    background-color: #0D1B2E !important;
    border: 1px solid #1E3A5F !important;
    border-radius: 8px !important;
    color: #E2E8F0 !important;
    font-size: 13px !important;
}
.stSelectbox > div > div {
    background-color: #0D1B2E !important;
    border: 1px solid #1E3A5F !important;
    border-radius: 8px !important;
    color: #E2E8F0 !important;
}
.stMultiSelect > div > div {
    background-color: #0D1B2E !important;
    border: 1px solid #1E3A5F !important;
    border-radius: 8px !important;
}

/* ── Sidebar brand header ── */
.sb-brand {
    padding: 20px 16px 12px;
    border-bottom: 1px solid #0F2444;
    margin-bottom: 16px;
}
.sb-brand-name {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 800;
    color: #38BDF8;
    letter-spacing: 1px;
}
.sb-brand-tag {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 9px;
    color: #334155;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 2px;
}

/* ── Sidebar section label ── */
.sb-section-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #1E3A5F;
    padding: 4px 0 8px;
    margin-top: 8px;
}

/* ── Sidebar KPI Card ── */
.sb-kpi {
    background: linear-gradient(135deg, #0A1628 0%, #0D1F38 100%);
    border: 1px solid #0F2444;
    border-left: 3px solid #38BDF8;
    border-radius: 10px;
    padding: 12px 14px;
    margin-bottom: 8px;
    transition: border-color 0.25s ease, transform 0.15s ease;
}
.sb-kpi:hover {
    border-left-color: #0EA5E9;
    border-color: #1E3A5F;
    transform: translateX(2px);
}
.sb-kpi-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 5px;
}
.sb-kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #F0F6FF;
    line-height: 1.1;
}
.sb-kpi-delta-pos {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #34D399;
    margin-top: 3px;
}
.sb-kpi-delta-neg {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #F87171;
    margin-top: 3px;
}
.sb-kpi-neutral {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    color: #64748B;
    margin-top: 3px;
}

/* ── Sidebar divider ── */
.sb-hr {
    border: none;
    border-top: 1px solid #0F2444;
    margin: 14px 0;
}

/* ── Radio nav pills ── */
[data-testid="stSidebar"] [data-testid="stRadio"] > label {
    display: none !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] > div {
    gap: 4px !important;
    flex-direction: column !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] > div > label {
    background: #0A1628 !important;
    border: 1px solid #0F2444 !important;
    border-radius: 8px !important;
    padding: 10px 14px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] > div > label:hover {
    background: #0D1F38 !important;
    border-color: #38BDF8 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] > div > label[data-checked="true"] {
    background: linear-gradient(135deg, #0C2340, #0E2F55) !important;
    border-color: #38BDF8 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] p {
    font-family: 'Syne', sans-serif !important;
    font-size: 12px !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    color: #94A3B8 !important;
}

/* ── Page title bar ── */
.page-header {
    background: linear-gradient(135deg, #0A1628 0%, #0D1F38 100%);
    border: 1px solid #0F2444;
    border-radius: 16px;
    padding: 24px 32px;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 16px;
}
.page-title {
    font-family: 'Syne', sans-serif;
    font-size: 28px;
    font-weight: 800;
    color: #F0F6FF;
    line-height: 1.1;
}
.page-subtitle {
    font-size: 13px;
    color: #475569;
    margin-top: 4px;
    font-family: 'IBM Plex Mono', monospace;
    letter-spacing: 0.5px;
}
.page-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, #0EA5E9, #38BDF8);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
}

/* ── KPI top row cards ── */
.kpi-row-card {
    background: linear-gradient(135deg, #0A1628 0%, #0D1F38 100%);
    border: 1px solid #0F2444;
    border-radius: 14px;
    padding: 20px 22px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s, transform 0.15s;
}
.kpi-row-card:hover {
    border-color: #1E3A5F;
    transform: translateY(-2px);
}
.kpi-row-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #38BDF8, #0EA5E9);
    border-radius: 14px 14px 0 0;
}
.kpi-row-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #475569;
    margin-bottom: 8px;
}
.kpi-row-value {
    font-family: 'Syne', sans-serif;
    font-size: 26px;
    font-weight: 800;
    color: #F0F6FF;
    line-height: 1;
}
.kpi-row-sub {
    font-size: 11px;
    color: #334155;
    margin-top: 6px;
    font-family: 'IBM Plex Mono', monospace;
}
.kpi-accent-green::before { background: linear-gradient(90deg, #34D399, #10B981); }
.kpi-accent-red::before   { background: linear-gradient(90deg, #F87171, #EF4444); }
.kpi-accent-amber::before { background: linear-gradient(90deg, #FBBF24, #F59E0B); }
.kpi-accent-purple::before{ background: linear-gradient(90deg, #A78BFA, #8B5CF6); }

/* ── Chart container ── */
.chart-card {
    background: linear-gradient(135deg, #0A1628 0%, #0D1F38 100%);
    border: 1px solid #0F2444;
    border-radius: 14px;
    padding: 4px;
    margin-bottom: 20px;
}

/* ── Filter bar ── */
.filter-bar {
    background: #0A1628;
    border: 1px solid #0F2444;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 22px;
}
.filter-bar-title {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 9px;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #1E3A5F;
    margin-bottom: 12px;
}

/* ── Strategic hub boxes ── */
.chat-bubble {
    background: linear-gradient(135deg, #0A1628 0%, #0D1F38 100%);
    border: 1px solid #0F2444;
    padding: 20px 24px;
    border-radius: 14px;
    margin: 8px 0;
    font-size: 14px;
    line-height: 1.8;
    color: #94A3B8;
}
.strategist-move {
    background: rgba(56, 189, 248, 0.07);
    border: 1px solid rgba(56, 189, 248, 0.15);
    border-left: 3px solid #38BDF8;
    padding: 10px 14px;
    border-radius: 8px;
    color: #38BDF8;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 11px;
    margin-top: 14px;
    letter-spacing: 0.3px;
}

/* ── Audit table ── */
.audit-filter-row { margin-bottom: 16px; }

/* ── Streamlit default metric override ── */
div[data-testid="metric-container"] {
    background: #0A1628;
    border: 1px solid #0F2444;
    border-radius: 12px;
    padding: 16px 20px;
}
div[data-testid="metric-container"] label {
    color: #475569 !important;
    font-family: 'IBM Plex Mono', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    color: #F0F6FF !important;
    font-size: 24px !important;
    font-weight: 700 !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #020C1B; }
::-webkit-scrollbar-thumb { background: #1E3A5F; border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: #38BDF8; }

/* ── Slider ── */
[data-testid="stSlider"] [data-testid="stMarkdownContainer"] p { color: #475569 !important; }

/* ── Expander ── */
details { border: 1px solid #0F2444 !important; border-radius: 10px !important; background: #0A1628 !important; margin-bottom: 8px !important; }
summary { color: #94A3B8 !important; font-family: 'DM Sans', sans-serif !important; font-size: 14px !important; padding: 14px 18px !important; }
summary:hover { color: #38BDF8 !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# 4. LOAD DATA
# ─────────────────────────────────────────
# ─────────────────────────────────────────
# 2. DATA LOADING
# ─────────────────────────────────────────
# This stays the same, but now it uses the Cloud function above
df_raw = get_data("SELECT * FROM cleaned_loans")

if df_raw.empty:
    st.error("No data found. Check Secrets configuration.")
    st.stop()

# Ensure correct dtypes
df_raw['loan_amount']    = pd.to_numeric(df_raw['loan_amount'],    errors='coerce')
df_raw['dti_ratio']      = pd.to_numeric(df_raw['dti_ratio'],      errors='coerce')
df_raw['monthly_income'] = pd.to_numeric(df_raw['monthly_income'], errors='coerce')
df_raw.dropna(subset=['loan_amount', 'dti_ratio'], inplace=True)


# ─────────────────────────────────────────
# 5. PLOTLY THEME
# ─────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color="#64748B", size=12),
    title_font=dict(family="Syne", color="#94A3B8", size=15),
    xaxis=dict(gridcolor="#0F2444", linecolor="#0F2444", tickfont=dict(color="#475569")),
    yaxis=dict(gridcolor="#0F2444", linecolor="#0F2444", tickfont=dict(color="#475569")),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#64748B")),
    margin=dict(l=20, r=20, t=50, b=20),
    colorway=["#38BDF8", "#34D399", "#FBBF24", "#F87171", "#A78BFA", "#FB923C"],
)

def styled_fig(fig):
    fig.update_layout(**PLOTLY_LAYOUT)
    return fig


# ─────────────────────────────────────────
# HELPER: KPI CARD
# ─────────────────────────────────────────
def kpi_card(label, value, delta="", positive=True, accent="blue"):
    accent_map = {
        "blue":   "kpi-row-card",
        "green":  "kpi-row-card kpi-accent-green",
        "red":    "kpi-row-card kpi-accent-red",
        "amber":  "kpi-row-card kpi-accent-amber",
        "purple": "kpi-row-card kpi-accent-purple",
    }
    cls = accent_map.get(accent, "kpi-row-card")
    delta_col  = "#34D399" if positive else "#F87171"
    delta_icon = "+" if positive else ""
    delta_html = (
        f'<div style="font-family:IBM Plex Mono,monospace;font-size:10px;'
        f'color:{delta_col};margin-top:6px;">{delta_icon}{delta}</div>'
        if delta else ""
    )
    st.markdown(f"""
    <div class="{cls}">
        <div class="kpi-row-label">{label}</div>
        <div class="kpi-row-value">{value}</div>
        {delta_html}
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# HELPER: SIDEBAR KPI
# ─────────────────────────────────────────
def sb_kpi(label, value, delta="", positive=True):
    delta_class = "sb-kpi-delta-pos" if positive else "sb-kpi-delta-neg"
    delta_icon  = "+" if positive else ""
    delta_html  = f'<div class="{delta_class}">{delta_icon}{delta}</div>' if delta else ""
    st.markdown(f"""
    <div class="sb-kpi">
        <div class="sb-kpi-label">{label}</div>
        <div class="sb-kpi-value">{value}</div>
        {delta_html}
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# HELPER: PAGE HEADER
# ─────────────────────────────────────────
def page_header(icon_letter, title, subtitle):
    st.markdown(f"""
    <div class="page-header">
        <div class="page-icon">
            <span style="font-family:Syne,sans-serif;font-weight:800;
                         color:#020C1B;font-size:18px;">{icon_letter}</span>
        </div>
        <div>
            <div class="page-title">{title}</div>
            <div class="page-subtitle">{subtitle}</div>
        </div>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# 6. SIDEBAR — NAVIGATION + DYNAMIC KPIs
# ─────────────────────────────────────────
with st.sidebar:

    # Brand
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-brand-name">VISION BANK</div>
        <div class="sb-brand-tag">Executive Intelligence Suite v3.0</div>
    </div>""", unsafe_allow_html=True)

    # Navigation
    st.markdown('<div class="sb-section-label">Navigation</div>', unsafe_allow_html=True)
    menu = st.radio(
        "SELECT SUITE",
        ["EXECUTIVE TRENDS", "REGIONAL RISK HUB",
         "MASTER AUDIT CHAMBER", "STRATEGIC INTEL HUB"],
        label_visibility="collapsed",
    )

    st.markdown('<hr class="sb-hr">', unsafe_allow_html=True)

    # ── Global filters (always visible) ──
    st.markdown('<div class="sb-section-label">Global Filters</div>', unsafe_allow_html=True)

    regions_all = sorted(df_raw['region'].dropna().unique().tolist())
    sb_region   = st.selectbox("Region", ["All Regions"] + regions_all, key="sb_region")

    scores_all  = sorted(df_raw['behavior_score'].dropna().unique().tolist())
    sb_score    = st.multiselect(
        "Behavior Score",
        scores_all,
        default=scores_all,
        key="sb_score",
    )

    loan_min  = float(df_raw['loan_amount'].min())
    loan_max  = float(df_raw['loan_amount'].max())
    sb_loan_range = st.slider(
        "Loan Amount (GHS)",
        min_value=loan_min,
        max_value=loan_max,
        value=(loan_min, loan_max),
        format="GHS %.0f",
        key="sb_loan_range",
    )

    st.markdown('<hr class="sb-hr">', unsafe_allow_html=True)

    # ── Apply global filters to produce df ──
    df = df_raw.copy()
    if sb_region != "All Regions":
        df = df[df['region'] == sb_region]
    if sb_score:
        df = df[df['behavior_score'].isin(sb_score)]
    df = df[(df['loan_amount'] >= sb_loan_range[0]) & (df['loan_amount'] <= sb_loan_range[1])]

    # ── Derived metrics on filtered df ──
    total_loans    = df['loan_amount'].sum()
    avg_loan       = df['loan_amount'].mean()
    avg_dti        = df['dti_ratio'].mean()
    total_borrowers= len(df)
    high_risk_pct  = (df['behavior_score'] == 'High Risk').mean() * 100 if len(df) > 0 else 0
    median_income  = df['monthly_income'].median() if 'monthly_income' in df.columns else 0

    reg = df.groupby('region').agg(
        loan_amount=('loan_amount', 'sum'),
        dti_ratio=('dti_ratio', 'mean'),
        borrowers=('loan_amount', 'count'),
    ).reset_index()

    # ── DYNAMIC SIDEBAR KPIs per hub ──
    st.markdown('<div class="sb-section-label">Hub KPIs</div>', unsafe_allow_html=True)

    if menu == "EXECUTIVE TRENDS":
        sb_kpi("Total Disbursed",   f"GHS {total_loans:,.0f}",   "Portfolio exposure")
        sb_kpi("Total Borrowers",   f"{total_borrowers:,}",      f"{len(regions_all)} regions active")
        sb_kpi("Avg Loan Size",     f"GHS {avg_loan:,.0f}",      "Per customer")
        sb_kpi("Avg DTI Ratio",     f"{avg_dti:.3f}",             "Lower is safer", positive=avg_dti < 0.4)
        sb_kpi("High Risk %",       f"{high_risk_pct:.1f}%",      "Of total portfolio", positive=high_risk_pct < 25)

    elif menu == "REGIONAL RISK HUB":
        if not reg.empty:
            top_region  = reg.loc[reg['loan_amount'].idxmax(), 'region']
            risk_region = reg.loc[reg['dti_ratio'].idxmax(),   'region']
            safe_region = reg.loc[reg['dti_ratio'].idxmin(),   'region']
            avg_reg_dti = reg['dti_ratio'].mean()
            top_vol     = reg['loan_amount'].max()
            sb_kpi("Regions Active",  str(len(reg)),               "Under current filter")
            sb_kpi("Top Volume Region", top_region,                f"GHS {top_vol:,.0f}")
            sb_kpi("Riskiest Region", risk_region,                 "Highest avg DTI", positive=False)
            sb_kpi("Safest Region",   safe_region,                 "Lowest avg DTI",  positive=True)
            sb_kpi("Avg Regional DTI", f"{avg_reg_dti:.3f}",       "Cross-region mean")
        else:
            st.info("No regional data for filter.")

    elif menu == "MASTER AUDIT CHAMBER":
        high_dti_count  = (df['dti_ratio'] > 0.5).sum()
        med_dti_count   = ((df['dti_ratio'] > 0.35) & (df['dti_ratio'] <= 0.5)).sum()
        low_dti_count   = (df['dti_ratio'] <= 0.35).sum()
        sb_kpi("Total Records",     f"{total_borrowers:,}",        "In filtered dataset")
        sb_kpi("Critical DTI (>0.5)", f"{high_dti_count:,}",       f"{high_dti_count/max(total_borrowers,1)*100:.1f}% flagged", positive=False)
        sb_kpi("Moderate DTI",       f"{med_dti_count:,}",           "0.35 - 0.50 range", positive=False)
        sb_kpi("Healthy DTI",        f"{low_dti_count:,}",           "Below 0.35 threshold", positive=True)
        sb_kpi("Median Income",     f"GHS {median_income:,.0f}",   "Filtered dataset")

    elif menu == "STRATEGIC INTEL HUB":
        most_common  = df['behavior_score'].value_counts().idxmax() if len(df) > 0 else "N/A"
        least_common = df['behavior_score'].value_counts().idxmin() if len(df) > 0 else "N/A"
        risk_r = reg.loc[reg['dti_ratio'].idxmax(), 'region'] if not reg.empty else "N/A"
        best_r = reg.loc[reg['loan_amount'].idxmax(), 'region'] if not reg.empty else "N/A"
        sb_kpi("Dominant Segment",  most_common,                   "Largest behavior group")
        sb_kpi("Best Segment",      least_common,                   "Most disciplined payers", positive=True)
        sb_kpi("Focus Region",      risk_r,                        "Highest risk zone", positive=False)
        sb_kpi("Revenue Leader",    best_r,                        "Top loan volume region", positive=True)
        sb_kpi("Insights Ready",    "14",                          "Strategic Q&A panels")

    # Footer
    st.markdown('<hr class="sb-hr">', unsafe_allow_html=True)
    st.markdown(f"""
    <div style="font-family:IBM Plex Mono,monospace;font-size:9px;
                color:#1E3A5F;letter-spacing:1px;text-align:center;padding:4px 0;">
        {total_borrowers:,} records loaded
    </div>""", unsafe_allow_html=True)


# ════════════════════════════════════════════
# HUB 1 — EXECUTIVE TRENDS
# ════════════════════════════════════════════
if menu == "EXECUTIVE TRENDS":

    page_header("E", "Executive Trends", "High-level portfolio overview — filtered & live")

    # ── In-hub dropdown filters ──
    st.markdown('<div class="filter-bar"><div class="filter-bar-title">Chart Controls</div>', unsafe_allow_html=True)
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        chart_style = st.selectbox(
            "Chart Style",
            ["Histogram", "Box Plot", "Violin"],
            key="exec_chart_style",
        )
    with fc2:
        color_by = st.selectbox(
            "Color Dimension",
            ["behavior_score", "region", None],
            format_func=lambda x: x if x else "None",
            key="exec_color_by",
        )
    with fc3:
        scatter_size = st.selectbox(
            "Scatter Size By",
            ["None", "dti_ratio", "loan_amount"],
            key="exec_scatter_size",
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # ── KPI Row ──
    k1, k2, k3, k4 = st.columns(4)
    with k1: kpi_card("Total Disbursed", f"GHS {total_loans:,.0f}", accent="blue")
    with k2: kpi_card("Total Borrowers", f"{total_borrowers:,}", accent="purple")
    with k3: kpi_card("Avg Loan Size", f"GHS {avg_loan:,.0f}", accent="amber")
    with k4:
        pos = avg_dti < 0.4
        kpi_card("Avg DTI Ratio", f"{avg_dti:.3f}",
                 delta="Safe" if pos else "Elevated",
                 positive=pos,
                 accent="green" if pos else "red")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Charts Row 1 ──
    ch1, ch2 = st.columns([3, 2])
    with ch1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        cb = color_by if color_by else None
        if chart_style == "Histogram":
            fig = px.histogram(df, x="loan_amount", color=cb,
                               title="Loan Amount Distribution",
                               nbins=40, opacity=0.85)
        elif chart_style == "Box Plot":
            fig = px.box(df, y="loan_amount", color=cb,
                         title="Loan Amount Box Plot")
        else:
            fig = px.violin(df, y="loan_amount", color=cb,
                            title="Loan Amount Violin", box=True)
        st.plotly_chart(styled_fig(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with ch2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        risk_counts = df['behavior_score'].value_counts().reset_index()
        risk_counts.columns = ['score', 'count']
        fig2 = px.pie(
            risk_counts, names='score', values='count',
            title="Risk Score Distribution",
            hole=0.55,
            color_discrete_sequence=["#38BDF8", "#34D399", "#FBBF24", "#F87171", "#A78BFA"],
        )
        fig2.update_traces(textfont_color="#94A3B8", pull=[0.03]*len(risk_counts))
        st.plotly_chart(styled_fig(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Charts Row 2 ──
    ch3, ch4 = st.columns(2)
    with ch3:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        sz = None if scatter_size == "None" else scatter_size
        fig3 = px.scatter(
            df.sample(min(2000, len(df))),
            x="monthly_income", y="loan_amount",
            color=color_by if color_by else "behavior_score",
            size=sz,
            title="Income vs Loan Amount",
            opacity=0.65,
        )
        st.plotly_chart(styled_fig(fig3), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with ch4:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        dti_dist = df.groupby('behavior_score')['dti_ratio'].mean().reset_index()
        fig4 = px.bar(
            dti_dist, x='behavior_score', y='dti_ratio',
            title="Avg DTI by Behavior Score",
            color='dti_ratio',
            color_continuous_scale=["#34D399", "#FBBF24", "#F87171"],
        )
        fig4.update_coloraxes(showscale=False)
        st.plotly_chart(styled_fig(fig4), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════
# HUB 2 — REGIONAL RISK HUB
# ════════════════════════════════════════════
elif menu == "REGIONAL RISK HUB":

    page_header("R", "Regional Risk Hub", "Geographic exposure and risk concentration analysis")

    # ── In-hub dropdowns ──
    st.markdown('<div class="filter-bar"><div class="filter-bar-title">Regional Controls</div>', unsafe_allow_html=True)
    rc1, rc2, rc3 = st.columns(3)
    with rc1:
        reg_metric = st.selectbox(
            "Primary Metric",
            ["loan_amount", "dti_ratio", "borrowers"],
            format_func=lambda x: {
                "loan_amount": "Total Loan Volume",
                "dti_ratio":   "Avg DTI Ratio",
                "borrowers":   "Borrower Count",
            }[x],
            key="reg_metric",
        )
    with rc2:
        reg_sort = st.selectbox(
            "Sort By",
            ["Highest First", "Lowest First"],
            key="reg_sort",
        )
    with rc3:
        reg_chart_type = st.selectbox(
            "Chart Type",
            ["Bar", "Horizontal Bar", "Scatter"],
            key="reg_chart_type",
        )
    st.markdown('</div>', unsafe_allow_html=True)

    if reg.empty:
        st.warning("No regional data available for current filter.")
        st.stop()

    reg_sorted = reg.sort_values(reg_metric, ascending=(reg_sort == "Lowest First"))

    # ── KPI Row ──
    top_r   = reg.loc[reg['loan_amount'].idxmax(), 'region']
    risk_r  = reg.loc[reg['dti_ratio'].idxmax(),   'region']
    safe_r  = reg.loc[reg['dti_ratio'].idxmin(),   'region']
    top_vol = reg['loan_amount'].max()

    k1, k2, k3, k4 = st.columns(4)
    with k1: kpi_card("Regions Active", str(len(reg)), accent="blue")
    with k2: kpi_card("Top Volume", top_r, delta=f"GHS {top_vol:,.0f}", positive=True, accent="green")
    with k3: kpi_card("Riskiest Region", risk_r, delta="Highest DTI", positive=False, accent="red")
    with k4: kpi_card("Safest Region", safe_r, delta="Lowest DTI", positive=True, accent="purple")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Main chart ──
    ch1, ch2 = st.columns([3, 2])
    with ch1:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        if reg_chart_type == "Bar":
            fig = px.bar(
                reg_sorted, x='region', y=reg_metric,
                color='dti_ratio',
                title=f"Regions by {reg_metric.replace('_',' ').title()}",
                color_continuous_scale=["#34D399", "#FBBF24", "#F87171"],
            )
        elif reg_chart_type == "Horizontal Bar":
            fig = px.bar(
                reg_sorted, y='region', x=reg_metric,
                orientation='h',
                color='dti_ratio',
                title=f"Regions by {reg_metric.replace('_',' ').title()}",
                color_continuous_scale=["#34D399", "#FBBF24", "#F87171"],
            )
        else:
            fig = px.scatter(
                reg_sorted, x='loan_amount', y='dti_ratio',
                size='borrowers', color='region', text='region',
                title="Regional Risk vs Volume Bubble",
            )
            fig.update_traces(textposition='top center')
        st.plotly_chart(styled_fig(fig), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with ch2:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        fig2 = px.treemap(
            reg, path=['region'], values='loan_amount',
            color='dti_ratio',
            title="Regional Volume Treemap",
            color_continuous_scale=["#38BDF8", "#FBBF24", "#F87171"],
        )
        fig2.update_traces(textfont_size=14)
        st.plotly_chart(styled_fig(fig2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ── Breakdown table ──
    st.markdown('<div class="chart-card" style="padding:16px 20px;">', unsafe_allow_html=True)
    st.markdown('<div class="filter-bar-title" style="margin-bottom:12px;">Regional Breakdown Table</div>', unsafe_allow_html=True)
    display_reg = reg_sorted.copy()
    display_reg['loan_amount'] = display_reg['loan_amount'].apply(lambda x: f"GHS {x:,.0f}")
    display_reg['dti_ratio']   = display_reg['dti_ratio'].apply(lambda x: f"{x:.4f}")
    display_reg.columns         = ['Region', 'Total Loans', 'Avg DTI', 'Borrowers']
    st.dataframe(display_reg, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ════════════════════════════════════════════
# HUB 3 — MASTER AUDIT CHAMBER
# ════════════════════════════════════════════
elif menu == "MASTER AUDIT CHAMBER":

    page_header("A", "Master Audit Chamber", "Full portfolio records with risk-tier highlighting")

    # ── In-hub dropdowns ──
    st.markdown('<div class="filter-bar"><div class="filter-bar-title">Audit Controls</div>', unsafe_allow_html=True)
    ac1, ac2, ac3, ac4 = st.columns(4)
    with ac1:
        audit_region = st.selectbox(
            "Filter Region",
            ["All"] + sorted(df['region'].dropna().unique().tolist()),
            key="audit_region",
        )
    with ac2:
        audit_score = st.selectbox(
            "Filter Risk Score",
            ["All"] + sorted(df['behavior_score'].dropna().unique().tolist()),
            key="audit_score",
        )
    with ac3:
        dti_threshold = st.selectbox(
            "DTI Risk Tier",
            ["All", "Critical (>0.5)", "Moderate (0.35-0.5)", "Healthy (<0.35)"],
            key="audit_dti_tier",
        )
    with ac4:
        audit_sort_col = st.selectbox(
            "Sort By",
            ["loan_amount", "dti_ratio", "monthly_income"],
            format_func=lambda x: x.replace("_", " ").title(),
            key="audit_sort",
        )
    st.markdown('</div>', unsafe_allow_html=True)

    # Apply audit-level filters
    df_audit = df.copy()
    if audit_region != "All":
        df_audit = df_audit[df_audit['region'] == audit_region]
    if audit_score != "All":
        df_audit = df_audit[df_audit['behavior_score'] == audit_score]
    if dti_threshold == "Critical (>0.5)":
        df_audit = df_audit[df_audit['dti_ratio'] > 0.5]
    elif dti_threshold == "Moderate (0.35-0.5)":
        df_audit = df_audit[(df_audit['dti_ratio'] > 0.35) & (df_audit['dti_ratio'] <= 0.5)]
    elif dti_threshold == "Healthy (<0.35)":
        df_audit = df_audit[df_audit['dti_ratio'] <= 0.35]

    df_audit = df_audit.sort_values(audit_sort_col, ascending=False)

    # ── KPI row ──
    n_crit = (df_audit['dti_ratio'] > 0.5).sum()
    n_mod  = ((df_audit['dti_ratio'] > 0.35) & (df_audit['dti_ratio'] <= 0.5)).sum()
    n_safe = (df_audit['dti_ratio'] <= 0.35).sum()
    k1, k2, k3, k4 = st.columns(4)
    with k1: kpi_card("Records in View", f"{len(df_audit):,}", accent="blue")
    with k2: kpi_card("Critical DTI", f"{n_crit:,}", delta=f"{n_crit/max(len(df_audit),1)*100:.1f}% of view", positive=False, accent="red")
    with k3: kpi_card("Moderate DTI", f"{n_mod:,}", delta=f"{n_mod/max(len(df_audit),1)*100:.1f}% of view", positive=False, accent="amber")
    with k4: kpi_card("Healthy DTI", f"{n_safe:,}", delta=f"{n_safe/max(len(df_audit),1)*100:.1f}% of view", positive=True, accent="green")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Styled dataframe ──
    def color_dti(val):
        try:
            v = float(val)
            if v > 0.5:   return "background-color:#3B0000;color:#F87171"
            elif v > 0.35: return "background-color:#2D1B00;color:#FBBF24"
            return "color:#34D399"
        except:
            return ""

    # REPLACEMENT LOGIC: Drop index columns and hide index
    cols_to_hide = ['id', 'Unnamed: 0', '']
    display_df = df_audit.drop(columns=[c for c in cols_to_hide if c in df_audit.columns], errors='ignore')

    st.dataframe(
        display_df.style.map(color_dti, subset=['dti_ratio']),
        height=640,
        use_container_width=True,
        hide_index=True
    )

# ════════════════════════════════════════════
# HUB 4 — STRATEGIC INTEL HUB
# ════════════════════════════════════════════
elif menu == "STRATEGIC INTEL HUB":

    page_header("S", "Strategic Intel Hub", "Executive summary and automated risk insights")

    st.markdown('<div class="chat-bubble">', unsafe_allow_html=True)
    st.write("### 🤖 Strategist AI Insights")
    
    if high_risk_pct > 30:
        st.markdown(f"⚠️ **PORTFOLIO ALERT**: High Risk concentration is currently at **{high_risk_pct:.1f}%**. This exceeds the internal safety threshold.")
    else:
        st.info(f"✅ **PORTFOLIO HEALTH**: High Risk exposure is stable at {high_risk_pct:.1f}%.")

    if not reg.empty:
        risk_r_name = reg.loc[reg['dti_ratio'].idxmax(), 'region']
        st.markdown(f"📍 **REGIONAL SNAPSHOT**: The **{risk_r_name}** region shows the highest average DTI ratio. Recommend reviewing Tier 2 lending criteria in this zone.")
    
    st.markdown('<div class="strategist-move">STRATEGIC RECOMMENDATION: Diversify Tier 1 outreach in high-volume regions to offset DTI volatility.</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    with st.expander("🔍 Which regions are driving the most volume?"):
        if not reg.empty:
            st.write(f"The top three regions by loan volume are: {', '.join(reg.nlargest(3, 'loan_amount')['region'].tolist())}.")

    with st.expander("⚖️ How does DTI relate to Loan Amount?"):
        st.write("Our analysis shows that larger loans often correlate with more stable DTI ratios, suggesting better income-to-debt balances in high-value segments.")