

import streamlit as st
import pandas as pd
import io

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="GemFlow Pro",
    layout="wide",
    page_icon="♦"
)

# ---------------- STYLING ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap');

/* ── Base ── */
.stApp {
    background: #0a0a0a;
    font-family: 'Inter', sans-serif;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1100px;
}

/* ── Header ── */
.gfp-header {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 1.5rem 0 1.5rem;
    border-bottom: 1px solid rgba(212,175,55,0.2);
    margin-bottom: 2rem;
}

.gfp-logo-ring {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    border: 1.5px solid rgba(212,175,55,0.6);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    background: linear-gradient(135deg, rgba(212,175,55,0.12), rgba(212,175,55,0.04));
    flex-shrink: 0;
}

.gfp-title {
    font-family: 'Cinzel', serif;
    font-size: 22px;
    font-weight: 700;
    color: #d4af37;
    letter-spacing: 0.04em;
    margin: 0;
    line-height: 1.2;
}

.gfp-subtitle {
    font-size: 12px;
    color: rgba(255,255,255,0.35);
    margin: 3px 0 0;
    font-weight: 300;
    letter-spacing: 0.02em;
}

.gfp-status {
    margin-left: auto;
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
    padding: 4px 12px;
    border-radius: 20px;
    background: rgba(212,175,55,0.08);
    color: rgba(212,175,55,0.8);
    border: 1px solid rgba(212,175,55,0.2);
    font-family: 'Inter', sans-serif;
    letter-spacing: 0.05em;
    flex-shrink: 0;
}

.gfp-status-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #d4af37;
}

/* ── Section label ── */
.section-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.25);
    margin-bottom: 1rem;
}

/* ── Upload cards ── */
.uc {
    background: #111111;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 14px;
    padding: 1.25rem 1.2rem 0.9rem;
    margin-bottom: 6px;
    transition: border-color 0.2s;
}

.uc:hover { border-color: rgba(212,175,55,0.25); }

.uc-icon {
    width: 34px;
    height: 34px;
    border-radius: 9px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    margin-bottom: 12px;
}

.uc-icon-gold   { background: rgba(212,175,55,0.12); border: 1px solid rgba(212,175,55,0.2); }
.uc-icon-blue   { background: rgba(56,189,248,0.1);  border: 1px solid rgba(56,189,248,0.2); }
.uc-icon-silver { background: rgba(192,192,192,0.1); border: 1px solid rgba(192,192,192,0.18); }

.uc-title {
    font-size: 13px;
    font-weight: 600;
    color: rgba(255,255,255,0.88);
    margin: 0 0 5px;
    letter-spacing: 0.01em;
}

.uc-desc {
    font-size: 12px;
    color: rgba(255,255,255,0.35);
    margin: 0 0 11px;
    line-height: 1.65;
    font-weight: 300;
}

.uc-tag {
    display: inline-flex;
    align-items: center;
    font-size: 10px;
    padding: 3px 9px;
    border-radius: 5px;
    font-weight: 500;
    letter-spacing: 0.03em;
}

.tag-gold   { background: rgba(212,175,55,0.1);  color: #d4af37;  border: 1px solid rgba(212,175,55,0.25); }
.tag-blue   { background: rgba(56,189,248,0.08); color: #38bdf8;  border: 1px solid rgba(56,189,248,0.2); }
.tag-silver { background: rgba(192,192,192,0.08);color: #c0c0c0;  border: 1px solid rgba(192,192,192,0.18); }

/* ── File uploader override ── */
[data-testid="stFileUploader"] {
    border: 1px dashed rgba(212,175,55,0.2) !important;
    border-radius: 10px !important;
    padding: 10px !important;
    background: rgba(212,175,55,0.02) !important;
    margin-top: 12px;
    transition: border-color 0.2s, background 0.2s;
}

[data-testid="stFileUploader"]:hover {
    border-color: rgba(212,175,55,0.45) !important;
    background: rgba(212,175,55,0.05) !important;
}

[data-testid="stFileUploaderDropzoneInstructions"] p,
[data-testid="stFileUploaderDropzoneInstructions"] span {
    color: rgba(255,255,255,0.35) !important;
    font-size: 12px !important;
}

/* ── Divider ── */
.gfp-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(212,175,55,0.35), rgba(56,189,248,0.2), transparent);
    border: none;
    margin: 2rem 0;
}

/* ── Run button ── */
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #b8860b, #d4af37, #b8860b) !important;
    background-size: 200% !important;
    color: #0a0a0a !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 32px !important;
    font-size: 14px !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    cursor: pointer;
    transition: transform 0.15s, box-shadow 0.15s;
    box-shadow: 0 4px 24px rgba(212,175,55,0.25);
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 32px rgba(212,175,55,0.4) !important;
}

.stButton > button:active { transform: scale(0.99) !important; }

/* ── Metric cards ── */
[data-testid="stMetric"] {
    background: #111111 !important;
    border: 1px solid rgba(212,175,55,0.15) !important;
    border-radius: 12px !important;
    padding: 1rem 1.25rem !important;
}

[data-testid="stMetricLabel"] {
    color: rgba(255,255,255,0.35) !important;
    font-size: 10px !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

[data-testid="stMetricValue"] {
    color: #d4af37 !important;
    font-size: 22px !important;
    font-weight: 600 !important;
}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.07);
}

/* ── Alerts ── */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    border: none !important;
    background: rgba(212,175,55,0.07) !important;
    color: rgba(255,255,255,0.75) !important;
}

/* ── Download button ── */
[data-testid="stDownloadButton"] > button {
    background: transparent !important;
    color: #38bdf8 !important;
    border: 1px solid rgba(56,189,248,0.35) !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    padding: 12px 24px !important;
    width: 100%;
    font-size: 13px !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase !important;
    transition: background 0.2s, box-shadow 0.2s;
}

[data-testid="stDownloadButton"] > button:hover {
    background: rgba(56,189,248,0.07) !important;
    box-shadow: 0 0 20px rgba(56,189,248,0.15) !important;
}

/* ── Caption ── */
.stCaption, [data-testid="stCaptionContainer"] p {
    color: rgba(255,255,255,0.3) !important;
    font-size: 12px !important;
}

/* ── Spinner ── */
[data-testid="stSpinner"] { color: #d4af37 !important; }

/* ── Success ── */
.stSuccess {
    background: rgba(52,211,153,0.07) !important;
    border: 1px solid rgba(52,211,153,0.2) !important;
    border-radius: 12px !important;
    color: rgba(255,255,255,0.7) !important;
}

/* ── Info ── */
.stInfo {
    background: rgba(56,189,248,0.06) !important;
    border: 1px solid rgba(56,189,248,0.18) !important;
    border-radius: 12px !important;
    color: rgba(255,255,255,0.6) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="gfp-header">
    <div class="gfp-logo-ring">♦</div>
    <div>
        <p class="gfp-title">GemFlow Pro</p>
        <p class="gfp-subtitle">Intelligent diamond inventory automation — merge, clean & reprice at scale</p>
    </div>
    <div class="gfp-status">
        <span class="gfp-status-dot"></span> System Ready
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------- UPLOAD SECTION ----------------
st.markdown('<p class="section-label">Step 1 — Upload your source files</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="uc">
        <div class="uc-icon uc-icon-gold">📋</div>
        <p class="uc-title">Master Stock File</p>
        <p class="uc-desc">Primary inventory export — the base file everything is merged into.</p>
        <span class="uc-tag tag-gold">Lot # · Lab · Price/Cts · Quality</span>
    </div>
    """, unsafe_allow_html=True)
    main_file = st.file_uploader("main", type=["xlsx"], label_visibility="collapsed")

with col2:
    st.markdown("""
    <div class="uc">
        <div class="uc-icon uc-icon-blue">🧪</div>
        <p class="uc-title">Lab-Grown Data File</p>
        <p class="uc-desc">Lab inventory export used to pull aging and days-in-stock data per lot.</p>
        <span class="uc-tag tag-blue">Stock ID · No. of Days</span>
    </div>
    """, unsafe_allow_html=True)
    labgrown_file = st.file_uploader("lab", type=["xlsx"], label_visibility="collapsed")

with col3:
    st.markdown("""
    <div class="uc">
        <div class="uc-icon uc-icon-silver">⏳</div>
        <p class="uc-title">Pending Memo File</p>
        <p class="uc-desc">Current memo and hold records — flags transit and on-memo stones.</p>
        <span class="uc-tag tag-silver">Lot # · Status · Customer</span>
    </div>
    """, unsafe_allow_html=True)
    pending_file = st.file_uploader("pending", type=["xlsx"], label_visibility="collapsed")


# ---------------- FUNCTIONS ----------------
def remove_unwanted_columns(df):
    df.columns = df.columns.str.strip()
    columns_to_remove = [
        "Polish", "Sym.", "Flu. Int.", "Tab %", "Dep %", "Cut", "Origin",
        "List Price", "% Off", "Price A%", "Price A", "Price B%", "Price B", "%RP/Cost",
        "Rect Cost", "Other Cost", "P&L", "P&&L", "S. Qlty.",
        "General Note", "Private Note",
        "CN", "SN", "CW", "SW", "Milky", "Im", "Md", "Im Md",
        "Itemserial", "Sp", "Price", "Cts",
        "Lab2", "Cert2", "Price/Cts1", "Price/Cts2",
        "Price B", "6", "Im Md Itemserial Sp Price Cts"
    ]
    return df.drop(columns=[col for col in columns_to_remove if col in df.columns], errors='ignore')

def filter_lab(df):
    df["Lab"] = df["Lab"].astype(str).str.strip().str.upper()
    return df[df["Lab"].isin(["GIA", "IGI", "GCAL"])]

def fill_quality(df):
    df["Quality"] = df["Quality"].fillna("").astype(str).str.strip()
    df["Rapnet Note"] = df["Rapnet Note"].fillna("").astype(str).str.upper()
    rapnet_map = df.set_index("Lot #")["Rapnet Note"].to_dict()

    def update_quality(row):
        if row["Quality"] == "":
            rap_val = rapnet_map.get(row["Lot #"], "")
            if "CVD" in rap_val:    return "CVD"
            elif "HPHT" in rap_val: return "HPHT"
        return row["Quality"]

    df["Quality"] = df.apply(update_quality, axis=1)
    return df.drop(columns=["Rapnet Note"], errors="ignore")


def apply_vlookup_lab(main_df, lab_file):
    lab_df = pd.read_excel(lab_file, header=2)
    lab_df.columns  = [str(col).strip() for col in lab_df.columns]
    main_df.columns = [str(col).strip() for col in main_df.columns]

    stock_col = None
    for col in lab_df.columns:
        c = str(col).lower().strip()
        if "stock #" in c or "stock#" in c or "stock id" in c or c == "id":
            stock_col = col
            break

    days_col = None
    for col in lab_df.columns:
        c = str(col).lower().strip()
        if "how old stone in stock" in c:
            days_col = col
            break

    if stock_col is None:
        raise ValueError(f"Stock column not found. Columns = {list(lab_df.columns)}")
    if days_col is None:
        raise ValueError(f"Days column not found. Columns = {list(lab_df.columns)}")

    lab_df = lab_df.rename(columns={stock_col: "Lot #", days_col: "No. Of Days"})
    lab_df = lab_df[["Lot #", "No. Of Days"]]

    main_df["Lot #"] = main_df["Lot #"].astype(str).str.strip()
    lab_df["Lot #"]  = lab_df["Lot #"].astype(str).str.strip()

    merged_df = pd.merge(main_df, lab_df, on="Lot #", how="left")

    if "Price / Cts" in merged_df.columns:
        cols = list(merged_df.columns)
        cols.remove("No. Of Days")
        idx = cols.index("Price / Cts")
        cols.insert(idx, "No. Of Days")
        merged_df = merged_df[cols]

    return merged_df

def apply_vlookup_pending(main_df, pending_file):
    pending_df = pd.read_excel(pending_file)
    main_df.columns    = main_df.columns.str.strip()
    pending_df.columns = pending_df.columns.str.strip()

    pending_df = pending_df[["Lot #", "Status", "Customer"]]
    main_df["Lot #"]    = main_df["Lot #"].astype(str).str.strip()
    pending_df["Lot #"] = pending_df["Lot #"].astype(str).str.strip()

    merged_df = pd.merge(main_df, pending_df, on="Lot #", how="left")

    cols = list(merged_df.columns)
    lot_index  = cols.index("Lot #")
    status_col = cols.pop(cols.index("Status"))
    cust_col   = cols.pop(cols.index("Customer"))
    cols.insert(lot_index + 1, status_col)
    cols.insert(lot_index + 2, cust_col)
    return merged_df[cols]


def get_size_group(cts):
    try:
        cts = float(cts)
    except (ValueError, TypeError):
        return ""

    if cts < 0.30:                  return "<0.30"
    elif 0.30 <= cts <= 0.39:       return "0.30 - 0.39"
    elif 0.40 <= cts <= 0.49:       return "0.40 - 0.49"
    elif 0.50 <= cts <= 0.59:       return "0.50 - 0.59"
    elif 0.60 <= cts <= 0.69:       return "0.60 - 0.69"
    elif 0.70 <= cts <= 0.79:       return "0.70 - 0.79"
    elif 0.80 <= cts <= 0.89:       return "0.80 - 0.89"
    elif 0.90 <= cts <= 0.99:       return "0.90 - 0.99"
    elif 1.00 <= cts <= 1.05:       return "1.00 - 1.05"
    elif 1.06 <= cts <= 1.10:       return "1.06 - 1.10"
    elif 1.11 <= cts <= 1.49:       return "1.11 - 1.49"
    elif 1.50 <= cts <= 1.55:       return "1.50 - 1.55"
    elif 1.55 <= cts <= 1.59:       return "1.55 - 1.59"
    elif 1.60 <= cts <= 1.99:       return "1.60 - 1.99"
    elif 2.00 <= cts <= 2.05:       return "2.00 - 2.05"
    elif 2.06 <= cts <= 2.10:       return "2.06 - 2.10"
    elif 2.11 <= cts <= 2.49:       return "2.11 - 2.49"
    elif 2.50 <= cts <= 2.55:       return "2.50 - 2.55"
    elif 2.56 <= cts <= 2.59:       return "2.55 - 2.59"
    elif 2.60 <= cts <= 2.99:       return "2.60 - 2.99"
    elif 3.00 <= cts <= 3.05:       return "3.00 - 3.05"
    elif 3.06 <= cts <= 3.10:       return "3.06 - 3.10"
    elif 3.11 <= cts <= 3.49:       return "3.11 - 3.49"
    elif 3.50 <= cts <= 3.55:       return "3.50 - 3.55"
    elif 3.56 <= cts <= 3.59:       return "3.56 - 3.59"
    elif 3.60 <= cts <= 3.99:       return "3.60 - 3.99"
    elif 4.00 <= cts <= 4.10:       return "4.00 - 4.10"
    elif 4.11 <= cts <= 4.49:       return "4.11 - 4.49"
    elif 4.50 <= cts <= 4.59:       return "4.50 - 4.59"
    elif 4.60 <= cts <= 4.99:       return "4.60 - 4.99"
    elif 5.00 <= cts <= 5.49:       return "5.00 - 5.49"
    elif 5.50 <= cts <= 5.99:       return "5.50 - 5.99"
    elif 6 <= cts < 25:
        lower = int(cts)
        upper = lower + 0.99
        return f"{lower:.2f} - {upper:.2f}"
    else:
        return "25+"

def add_size_group(df):
    cts_col = next(
        (c for c in df.columns if c.strip().lower().rstrip(".") == "cts"),
        None
    )
    if cts_col is None:
        raise ValueError(f"Column 'Cts' not found. Columns available: {list(df.columns)}")

    df["Size Group"] = df[cts_col].apply(get_size_group)
    cols = list(df.columns)
    cols.remove("Size Group")
    insert_at = cols.index(cts_col) + 1
    cols.insert(insert_at, "Size Group")
    return df[cols]


def update_status_and_cleanup(df):
    df["Customer"] = df["Customer"].fillna("").str.upper()
    df["Status"]   = df["Status"].fillna("").str.strip()

    mask = (
        df["Customer"].isin([
            "GOODS IN TRANSIT",
            "GOODS IN TRANSIT FROM OVERSEAS",
            "GOODS IN OFFICE - PARCEL PAPERS BEING MADE"
        ]) & (df["Status"].str.upper() == "ONMEMO")
    )

    df.loc[mask, "Status"] = "Inhand"
    return df.drop(columns=["Customer"], errors="ignore")


# ---------------- SESSION STATE ----------------
if "final_df" not in st.session_state:
    st.session_state.final_df = None


# ================================================================
#  MAIN PAGE
# ================================================================
if main_file and labgrown_file and pending_file:

    main_df = pd.read_excel(main_file)

    st.markdown('<hr class="gfp-divider">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Step 2 — Inventory preview</p>', unsafe_allow_html=True)
    st.caption(f"Showing first 5 rows · {len(main_df):,} total rows detected in your master stock file")
    st.dataframe(main_df.head(), use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("♦  Process & Reprice Inventory — Run All 7 Steps"):
        try:
            with st.spinner("Processing your inventory…"):
                main_df  = remove_unwanted_columns(main_df)
                main_df  = filter_lab(main_df)
                main_df  = fill_quality(main_df)
                main_df  = apply_vlookup_lab(main_df, labgrown_file)
                main_df  = apply_vlookup_pending(main_df, pending_file)
                main_df  = update_status_and_cleanup(main_df)
                final_df = add_size_group(main_df)

            st.session_state.final_df = final_df

            st.success(f"✦  Pipeline complete — {len(final_df):,} records processed across all 7 steps.")

            c1, c2, c3 = st.columns(3)
            c1.metric("Total Records",     f"{len(final_df):,}")
            c2.metric("Columns Retained",  f"{len(final_df.columns)}")
            c3.metric("Certified Labs",    "GIA · IGI · GCAL")

            st.markdown('<hr class="gfp-divider">', unsafe_allow_html=True)
            st.markdown('<p class="section-label">Step 3 — Output preview</p>', unsafe_allow_html=True)
            st.caption("Showing first 10 rows of your final merged & repriced file")
            st.dataframe(final_df.head(10), use_container_width=True)

            output = io.BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                final_df.to_excel(writer, index=False)

            st.markdown("<br>", unsafe_allow_html=True)

            st.download_button(
                label="↓  Export Final Report — Download .xlsx",
                data=output.getvalue(),
                file_name="gemflow_pro_output.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

        except Exception as e:
            st.error(f"Pipeline error: {e}")

elif main_file:
    main_df = pd.read_excel(main_file)
    st.markdown('<hr class="gfp-divider">', unsafe_allow_html=True)
    st.caption(f"{len(main_df):,} records detected. Upload the remaining two files to continue.")
    st.dataframe(main_df.head(), use_container_width=True)

else:
    st.markdown("<br>", unsafe_allow_html=True)
    st.info("♦  Upload all three source files above to begin processing.")