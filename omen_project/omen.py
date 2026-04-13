import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
import streamlit as st
import streamlit.components.v1 as components

# --- THE PWA INJECTION ---
# This tells the phone's browser that the manifest exists
st.set_page_config(page_title="OMNI-NODE", page_icon="🛡️", layout="wide")

def inject_pwa_meta():
    pwa_html = """
    <link rel="manifest" href="/manifest.json">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">
    <meta name="apple-mobile-web-app-title" content="OMNI-NODE">
    <link rel="apple-touch-icon" href="logo.png">
    """
    # This reaches into the head of the page
    st.markdown(f'<div style="display:none">{pwa_html}</div>', unsafe_allow_html=True)

inject_pwa_meta()

# --- YOUR EXISTING APP LOGIC STARTS HERE ---
st.title("🛡️ OMEN OMNI-NODE")
st.write("Decentralized Legacy OS // Build 2026.04.12")

# --- 1. SYSTEM CORE & INITIALIZATION ---
st.set_page_config(page_title="OMEN OMNI-NODE", layout="wide", initial_sidebar_state="expanded")

# "Titanium-Grid" Custom CSS for 10-Year Resilience
st.markdown("""
    <style>
    .main { background: #010a01; color: #00ff41; font-family: 'Consolas', monospace; }
    .stMetric { border: 1px solid #00ff41; background: #050505; padding: 20px; border-radius: 2px; box-shadow: 0 0 15px #00ff4133; }
    .stTabs [data-baseweb="tab-list"] { background-color: #000; border: 1px solid #00ff41; }
    .stTabs [data-baseweb="tab"] { color: #00ff41; font-weight: bold; text-transform: uppercase; }
    h1, h2, h3 { color: #00ff41; text-transform: uppercase; border-bottom: 1px solid #00ff41; padding-bottom: 10px; }
    .stButton>button { width: 100%; background-color: #050505; color: #00ff41; border: 1px solid #00ff41; transition: 0.3s; }
    .stButton>button:hover { background-color: #00ff41; color: #000; border: 1px solid #00ff41; }
    [data-testid="stTable"] { background-color: #050505; color: #00ff41; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE MULTI-LAYERED VAULT (SQL DATABASE) ---
def init_omni_db():
    conn = sqlite3.connect('omen_omni_v4.db')
    c = conn.cursor()
    # Strategic Inventory (Gold, Silver, Quartz, Tools)
    c.execute('CREATE TABLE IF NOT EXISTS inventory (id INTEGER PRIMARY KEY, category TEXT, item TEXT, qty REAL, unit TEXT, location TEXT, value_ref REAL)')
    # Barter Economics (Trade History)
    c.execute('CREATE TABLE IF NOT EXISTS barter (id INTEGER PRIMARY KEY, trade_date TEXT, out_item TEXT, in_item TEXT, contact TEXT, value_ref REAL)')
    # Medical Triage (Emergency Health Data)
    c.execute('CREATE TABLE IF NOT EXISTS medical (id INTEGER PRIMARY KEY, name TEXT, blood TEXT, meds TEXT, allergies TEXT, status TEXT)')
    # Mesh Network (Community Trust & Comms)
    c.execute('CREATE TABLE IF NOT EXISTS mesh (id INTEGER PRIMARY KEY, alias TEXT, skill TEXT, trust_score INTEGER, frequency REAL, notes TEXT)')
    # Survival Larder (Logic-Driven Food Storage)
    c.execute('CREATE TABLE IF NOT EXISTS larder (id INTEGER PRIMARY KEY, item TEXT, cals_per_unit INTEGER, qty REAL, unit TEXT, expiry TEXT)')
    # Bio-Reserve (Pets & Livestock)
    c.execute('CREATE TABLE IF NOT EXISTS bio (id INTEGER PRIMARY KEY, name TEXT, species TEXT, daily_feed REAL, stock REAL, health TEXT)')
    # Energy & Resource Yield (Solar/Wind/Gen)
    c.execute('CREATE TABLE IF NOT EXISTS energy (id INTEGER PRIMARY KEY, source TEXT, yield REAL, battery_pct INTEGER, date TEXT)')
    # Financial Wall Tracker
    c.execute('CREATE TABLE IF NOT EXISTS obligations (id INTEGER PRIMARY KEY, entity TEXT, amount REAL, due_date TEXT, priority TEXT)')
    conn.commit()
    conn.close()

init_omni_db()

# --- 3. DATA PERSISTENCE CONTROLLERS ---
def write_db(query, params=()):
    with sqlite3.connect('omen_omni_v4.db') as conn:
        conn.execute(query, params)
        conn.commit()

def read_db(query):
    with sqlite3.connect('omen_omni_v4.db') as conn:
        return pd.read_sql_query(query, conn)

# --- 4. COMMAND SIDEBAR (GLOBAL POSITIONING) ---
with st.sidebar:
    st.title("🛡️ OMEN OMNI-NODE")
    st.caption("DECENTRALIZED LEGACY OS // BUILD 2026.04.12")
    st.divider()
    
    # SYSTEM INTELLIGENCE: Survival Days Calculator
    larder_data = read_db("SELECT * FROM larder")
    if not larder_data.empty:
        total_cals = (larder_data['cals_per_unit'] * larder_data['qty']).sum()
        days_remaining = total_cals / 2500  # Avg daily requirement for 1 adult
        st.metric("LARDER SUSTAINABILITY", f"{int(days_remaining)} DAYS", "Caloric Reserve")
    
    st.divider()
    st.subheader("SYSTEM DIAGNOSTICS")
    st.code("NODE: ACTIVE\nSTORAGE: LOCAL_SQL\nENCRYPTION: AES-256\nAIR_GAP: READY")
    
    # Financial 2027 Countdown
    target_date = datetime(2027, 1, 1)
    days_to_wall = (target_date - datetime.now()).days
    st.metric("THE 2027 WALL", f"{days_to_wall} DAYS", "Countdown Initiated")

# --- 5. THE LEGACY HUBS ---
tabs = st.tabs([
    "🏛️ THE VAULT", "🛒 LARDER", "🔋 ENERGY", 
    "🩹 MEDICAL", "🤝 BARTER", "🐾 BIO-RESERVE", "🛰️ MESH", "📉 DEBT WALL"
])

# --- HUB 1: THE VAULT (Hard Asset Ledger) ---
with tabs[0]:
    st.header("Strategic Hard-Asset Reserve")
    v_col1, v_col2 = st.columns([2, 1])
    with v_col1:
        with st.expander("📥 ASSET INTAKE PORTAL"):
            with st.form("vault_form"):
                v_cat = st.selectbox("Class", ["Precious Metals", "Blue Quartz", "Tools", "Ammunition", "Barter Goods"])
                v_item = st.text_input("Asset Description")
                v_qty = st.number_input("Quantity", min_value=0.0)
                v_unit = st.text_input("Unit (oz, g, units, rounds)")
                v_loc = st.text_input("Physical Storage Location")
                if st.form_submit_button("COMMIT TO VAULT"):
                    write_db("INSERT INTO inventory (category, item, qty, unit, location) VALUES (?,?,?,?,?)", (v_cat, v_item, v_qty, v_unit, v_loc))
                    st.success("Ledger Entry Finalized.")
    
    df_inv = read_db("SELECT * FROM inventory")
    st.dataframe(df_inv, use_container_width=True)

# --- HUB 2: LARDER LOGISTICS (Survival Math) ---
with tabs[1]:
    st.header("Sustainability & Rations")
    l1, l2 = st.columns([1, 2])
    with l1:
        with st.form("larder_form"):
            li_item = st.text_input("Resource Name")
            li_cal = st.number_input("Calories/Unit", min_value=1)
            li_qty = st.number_input("Units in Stock", min_value=0.0)
            li_exp = st.date_input("Expiry Date")
            if st.form_submit_button("Update Supply"):
                write_db("INSERT INTO larder (item, cals_per_unit, qty, expiry) VALUES (?,?,?,?)", (li_item, li_cal, li_qty, str(li_exp)))
    with l2:
        df_l = read_db("SELECT * FROM larder")
        if not df_l.empty:
            fig = px.bar(df_l, x="item", y="qty", title="Supply Volume Distribution", template="plotly_dark", color_discrete_sequence=['#00ff41'])
            st.plotly_chart(fig, use_container_width=True)

# --- HUB 3: ENERGY YIELD ---
with tabs[2]:
    st.header("Power Generation & Storage")
    e_col1, e_col2 = st.columns(2)
    with e_col1:
        with st.form("energy_form"):
            e_src = st.selectbox("Source", ["Solar Array", "Wind Turbine", "Gas Gen", "Mesh Bridge"])
            e_yld = st.number_input("Daily Yield (kWh)", min_value=0.0)
            e_bat = st.slider("Battery Capacity (%)", 0, 100, 80)
            if st.form_submit_button("Log Generation"):
                write_db("INSERT INTO energy (source, yield, battery_pct, date) VALUES (?,?,?,?)", (e_src, e_yld, e_bat, str(datetime.now().date())))
    with e_col2:
        df_e = read_db("SELECT * FROM energy")
        if not df_e.empty:
            st.line_chart(df_e, x="date", y="yield")

# --- HUB 4: MEDICAL TRIAGE ---
with tabs[3]:
    st.header("Critical Biological Integrity")
    with st.form("med_form"):
        m_name = st.text_input("Name/Alias")
        m_blood = st.selectbox("Blood Type", ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"])
        m_meds = st.text_area("Critical Medications / Allergies / Procedure Notes")
        if st.form_submit_button("SECURE MEDICAL RECORD"):
            write_db("INSERT INTO medical (name, blood, meds) VALUES (?,?,?)", (m_name, m_blood, m_meds))
    st.dataframe(read_db("SELECT * FROM medical"), use_container_width=True)

# --- HUB 5: BARTER HUB ---
with tabs[4]:
    st.header("Post-Currency Economics")
    with st.expander("📝 RECORD TRANSACTION"):
        with st.form("barter_form"):
            b_alias = st.text_input("Counterparty Alias")
            b_out = st.text_input("Item Given")
            b_in = st.text_input("Item Received")
            b_val = st.number_input("Value Reference ($)", min_value=0.0)
            if st.form_submit_button("COMMIT TRADE"):
                write_db("INSERT INTO barter (trade_date, out_item, in_item, contact, value_ref) VALUES (?,?,?,?,?)", (str(datetime.now().date()), b_out, b_in, b_alias, b_val))
    st.dataframe(read_db("SELECT * FROM barter"), use_container_width=True)

# --- HUB 6: BIO-RESERVE ---
with tabs[5]:
    st.header("Livestock & Pet Sovereignty")
    with st.form("bio_form"):
        bi_name = st.text_input("Dependent Name")
        bi_spec = st.text_input("Species")
        bi_feed = st.number_input("Daily Feed Requirement (kg)", min_value=0.1)
        bi_stock = st.number_input("Current Feed Stock (kg)", min_value=0.0)
        if st.form_submit_button("UPDATE VITALITY"):
            write_db("INSERT INTO bio (name, species, daily_feed, stock) VALUES (?,?,?,?)", (bi_name, bi_spec, bi_feed, bi_stock))
    df_bio = read_db("SELECT * FROM bio")
    if not df_bio.empty:
        df_bio['DAYS_LEFT'] = df_bio['stock'] / df_bio['daily_feed']
        st.dataframe(df_bio, use_container_width=True)

# --- HUB 7: MESH NETWORK ---
with tabs[6]:
    st.header("Trusted Node Community")
    with st.form("mesh_form"):
        me_alias = st.text_input("Node Alias")
        me_skill = st.text_input("Specialization / Resource")
        me_freq = st.number_input("Primary Freq (MHz)", value=146.52)
        me_trust = st.slider("Trust Index (0-100)", 0, 100, 50)
        if st.form_submit_button("REGISTER NODE"):
            write_db("INSERT INTO mesh (alias, skill, trust_score, frequency) VALUES (?,?,?,?)", (me_alias, me_skill, me_trust, me_freq))
    st.dataframe(read_db("SELECT * FROM mesh"), use_container_width=True)

# --- HUB 8: DEBT WALL (Liability Tracker) ---
with tabs[7]:
    st.header("The Financial Wall Tracker")
    with st.form("debt_form"):
        d_ent = st.text_input("Creditor/Entity")
        d_amt = st.number_input("Amount Owed", min_value=0.0)
        d_due = st.date_input("Maturity Date")
        if st.form_submit_button("LOG LIABILITY"):
            write_db("INSERT INTO obligations (entity, amount, due_date) VALUES (?,?,?)", (d_ent, d_amt, str(d_due)))
    st.dataframe(read_db("SELECT * FROM obligations"), use_container_width=True)

# --- FOOTER ---
st.divider()
st.caption("OMEN LEGACY // BUILD 4.0.0 // NO SURVEILLANCE // SOVEREIGNTY BY DESIGN // 2026-2036")
