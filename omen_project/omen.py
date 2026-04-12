import streamlit as st
import pandas as pd
import numpy as np
import random
import time
from datetime import datetime, timedelta
from streamlit_autorefresh import st_autorefresh

# --- THE HOLLYWOOD GRIME (Custom CSS) ---
st.set_page_config(page_title="VOID // OMEN", page_icon="💀", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    
    .main { 
        background-color: #050505; 
        color: #d3d3d3; 
        font-family: 'Share+Tech+Mono', monospace;
    }
    
    /* The Glitch Alert */
    .emergency-banner {
        background: linear-gradient(90deg, #600 0%, #000 50%, #600 100%);
        padding: 10px;
        text-align: center;
        border-bottom: 2px solid #ff0000;
        color: #ff0000;
        font-weight: bold;
        animation: blinker 0.8s linear infinite;
    }
    
    @keyframes blinker {
        50% { opacity: 0; }
    }

    .stMetric {
        background: #111;
        padding: 15px;
        border-radius: 5px;
        border-left: 3px solid #ff0000;
    }

    /* Cinematic Text */
    .manifesto {
        font-size: 1.2rem;
        line-height: 1.6;
        color: #888;
        border-left: 2px solid #444;
        padding-left: 20px;
        margin: 20px 0;
    }

    .critical-text {
        color: #ff4b4b;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- THE "LAST SECONDS" TIMER ---
def get_doomsday_clock():
    # We set the "crash" to be exactly 2 minutes from the user's current session start
    if 'end_time' not in st.session_state:
        st.session_state.end_time = datetime.now() + timedelta(minutes=2)
    
    remaining = st.session_state.end_time - datetime.now()
    if remaining.total_seconds() <= 0:
        return "00:00:00 [SYSTEM COLLAPSE]"
    return str(remaining).split(".")[0]

# --- THE HEADER: WELCOME TO THE END ---
st.markdown('<div class="emergency-banner">SIGNAL DETECTED: THE GREAT UNWIND HAS BEGUN</div>', unsafe_allow_html=True)

st.title("Ω OMEN: THE FINAL BLOCK")
st.markdown("""
    <div class="manifesto">
    You feel it. The air is heavy. The numbers on the screen are lies. 
    The trillions printed are ghosts haunting a machine that has already stopped breathing. 
    <b>Today is the last day of the world you knew.</b> In two minutes, the ledger balances. 
    The "Gray Rhino" isn't coming—it's already here, and it's brought the Big Bang.
    </div>
    """, unsafe_allow_html=True)

# --- THE METRICS OF DOOM ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("LIQUIDITY DRAIN", "99.8%", "-12.4% / SEC")
with col2:
    st.metric("YIELD INVERSION", "CRITICAL", "DEATH CROSS")
with col3:
    st.metric("CURRENCY DEBODIMENT", "ACTIVE", "EXITING...")
with col4:
    # The Countdown Clock
    clock = get_doomsday_clock()
    st.metric("TIME TO IMPACT", clock)

st.write("---")
# --- THE ENTROPY PULSE (Real-time Decay Simulation) ---
st.subheader("📉 SYSTEMIC VITALITY: REAL-TIME DECAY")

if 'chart_data' not in st.session_state:
    # Start with a "stable" high value, then simulate a crash
    st.session_state.chart_data = pd.DataFrame(
        np.random.normal(100, 0.5, size=(50, 1)), 
        columns=['Global Index']
    )

# Logic to make the chart "drop" as the timer gets closer to zero
def update_decay():
    new_val = st.session_state.chart_data['Global Index'].iloc[-1] * random.uniform(0.85, 1.02)
    new_row = pd.DataFrame([[new_val]], columns=['Global Index'])
    st.session_state.chart_data = pd.concat([st.session_state.chart_data, new_row]).iloc[-50:]

update_decay()
st.line_chart(st.session_state.chart_data, color="#ff0000")

# --- PHASE 2: THE "LAST MAN" TERMINAL ---
st.write("---")
st.markdown("### 🛰️ INTERCEPTED FREQUENCIES (LIVE)")

log_messages = [
    "[INFO] Federal wire transfer protocols: TIMEOUT",
    "[WARN] Commercial bank 'Wait-Times' exceeding 48 hours.",
    "[CRITICAL] Global shipping insurance premiums: DENIED",
    "[ALERT] Sovereign debt 'Default Swaps' spiking in 14 nations.",
    "[LOCAL] City grid 'Load Shedding' initiated in major hubs.",
    "[AUDIO] Distant thunder? Or the sound of the 'Refinance Wall' breaking?"
]

# Displaying the messages with a typewriter-style delay effect
with st.container():
    st.markdown('<div class="manifesto">', unsafe_allow_html=True)
    for msg in log_messages:
        # We simulate that the further down the list, the more "unstable" the world gets
        if "CRITICAL" in msg or "ALERT" in msg:
            st.markdown(f"<span style='color:#ff0000;'>{msg}</span>", unsafe_allow_html=True)
        else:
            st.write(msg)
    st.markdown('</div>', unsafe_allow_html=True)

# --- THE EMOTIONAL HOOK: THE "MIRROR" QUERY ---
st.write("---")
st.markdown("### 🪞 LOOK AT THE MIRROR")
st.write("""
    They told you to work. They told you to save. They told you 2027 was 'just a cycle.' 
    While you were sleeping, the Rhino was sharpening its horn on the bones of your pension. 
    **Is your family ready for the Dark Reset?**
""")

# --- INTERACTIVE DOOM: THE "ASSET SACRIFICE" ---
st.write("Current Digital Worth: **$0.00** (Projected after T-Minus zero)")
sacrifice = st.slider("Select how much of your 'Paper Wealth' you're willing to lose before you act:", 0, 100, 50)

if sacrifice > 80:
    st.warning("THE HERD MENTALITY DETECTED. YOU ARE STAYING ON THE TRACKS.")
else:
    st.info("SKEPTICISM DETECTED. YOU ARE LOOKING FOR THE EXIT.")

# Refresh button to keep the "Pulse" moving
if st.button("STAY CONNECTED TO THE VOID"):
    st.rerun()
    # --- THE VAULT (The "Safe" Zone) ---
st.markdown("""
    <style>
    .vault-section {
        background: linear-gradient(145deg, #0a1128 0%, #001f3f 100%);
        border: 2px solid #0074d9;
        padding: 30px;
        border-radius: 15px;
        color: #fff;
    }
    .asset-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #c9a227; /* Gold border */
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("<h2 style='text-align: center; color: #c9a227;'>🛡️ THE SANCTUARY</h2>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="vault-section">
        <h3>The Great Filter is active.</h3>
        <p>When the digital grid snaps, the only thing that remains is what you can hold in your hand. 
        Electricity is a privilege; physical reality is a right. We don't track numbers here. 
        We track <b>permanence</b>.</p>
        </div>
        """, unsafe_allow_html=True)

st.write("##")

# --- INTEGRATING THE SPECIMENS (The "Alive" Stones) ---
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
        <div class="asset-card">
        <h4 style="color: #c9a227;">SPECIMEN O-01: THE BLUE-INCLUSION QUARTZ</h4>
        <p><i>"The Living Geometry"</i></p>
        <p>Hardness: 7 (Glass-Slayer) | Origin: Deep Crust</p>
        <p><b>STATUS: UN-DELETABLE</b></p>
        </div>
        """, unsafe_allow_html=True)
    st.info("In a world of zeroed-out bank accounts, this stone maintains its atomic structure. It is a store of energy older than the debt cycle.")

with col_b:
    st.markdown("""
        <div class="asset-card">
        <h4 style="color: #c9a227;">PHYSICAL HEDGE RATIO</h4>
        <p>Current conversion rate: 1 Stone = Life Sustaining Value</p>
        <progress value="95" max="100" style="width: 100%;"></progress>
        <p>Hedge Strength: <b>MAXIMUM</b></p>
        </div>
        """, unsafe_allow_html=True)

# --- THE "EXIT PLAN" CONVERSION ---
st.write("---")
st.subheader("🏁 THE ESCAPE VELOCITY PROTOCOL")

st.write("""
    The clock is at 00:00:15. You have seconds to move from the 'Trampled' to the 'Prepared.' 
    Our Protocol isn't just a book—it's a decryption key for the 2027 Horizon.
""")

if st.button("EXECUTE PROTOCOL: LOAD THE VAULT ($149)"):
    st.balloons()
    st.success("ENCRYPTION ESTABLISHED. YOUR PHYSICAL BRIDGE IS READY.")
    st.write("Welcome to the 1%. Check your private terminal for the coordinates.")

# Final Cinematic Footer
st.markdown("""
    <div style='text-align: center; color: #444; margin-top: 50px;'>
    [OMEN v.4.02] - NO ONE IS COMING TO SAVE YOU. SAVE YOURSELF.
    </div>
    """, unsafe_allow_html=True)
# --- THE GHOST IN THE MACHINE (Advanced Logic) ---
def trigger_collapse_sequence():
    """This function triggers when the 2-minute timer hits zero."""
    st.markdown("""
        <style>
        .main { background-color: #ff0000 !important; }
        * { color: #ffffff !important; font-family: 'Courier New', Courier, monospace !important; }
        </style>
        """, unsafe_allow_html=True)
    st.error("!!! TOTAL SYSTEM FAILURE DETECTED !!!")
    st.write("LEDGER RESET IN PROGRESS...")
    st.write("Your digital assets have been reclassified as: [NULL]")
    st.write("The only verified value remains Specimen O-01.")
    if st.button("RECLAIM VALUE VIA PHYSICAL BRIDGE"):
        st.write("Contacting Vault Custodian... Stand by for extraction.")

# Checking for the final moment
remaining_sec = (st.session_state.end_time - datetime.now()).total_seconds()

if remaining_sec <= 0:
    trigger_collapse_sequence()
else:
    # --- THE "LAST DAY" DIARY (Emotional Persistence) ---
    st.write("---")
    st.markdown("### 📔 LOGS FROM THE FRONTIER")
    diary_entries = [
        "Day 0: The ATMs stopped. People are still smiling, thinking it's a 'network error.' They don't know.",
        "Day 0 [T-Minus 60s]: The sound of the Rhino isn't a roar. It's the silence of a bank app that won't load.",
        "Day 0 [T-Minus 30s]: Looking at my stones. They don't need electricity to be real. They just are."
    ]
    for entry in diary_entries:
        st.text(entry)

    # --- THE PSYCHOLOGICAL LOCK-IN ---
    st.sidebar.markdown("### 🕵️ YOUR RISK PROFILE")
    st.sidebar.progress(98)
    st.sidebar.write("Exposure Level: **FATAL**")
    st.sidebar.warning("You are currently holding 95% of your life in 'Imaginary Credits.'")
    
    if st.sidebar.button("HARDEN YOUR POSITION"):
        st.sidebar.success("Allocating to Physical... Stone Specimen Locked.")

# --- THE AUTO-REFRESH (The Hook) ---
# This script keeps the page alive and the timer ticking without the user having to click.
from streamlit_autorefresh import st_autorefresh
count = st_autorefresh(interval=1000, limit=1000, key="fizzbuzzcounter")
# --- THE RUGGED OVERHAUL (Part 5) ---

# Adding a 'System Degradation' filter
if remaining_sec < 60:
    # Under 60 seconds, the UI starts to jitter and lose color
    st.markdown("""
        <style>
        .main { filter: grayscale(0.8) contrast(1.2); }
        h1, h2, h3 { text-shadow: 2px 2px #ff0000; }
        </style>
        """, unsafe_allow_html=True)

# --- THE "LAST DAY" AUDIO-VISUAL DISTORTION ---
if remaining_sec < 30:
    st.markdown('<div class="emergency-banner">!!! SIGNAL DEGRADATION: PACKET LOSS 40% !!!</div>', unsafe_allow_html=True)
    # The text starts to scramble
    st.write("T-H-E--E-N-D--I-S--N-O-T--C-O-M-I-N-G--I-T--I-S--H-E-R-E")

# --- THE HARD-ASSET "GEIGER COUNTER" ---
# A feature that "scans" for those blue-specked stones
st.write("---")
st.markdown("### 📡 HARD-ASSET PROXIMITY SENSOR")
if st.button("SCAN LOCAL ENVIRONMENT FOR 'ALIVE' MATTER"):
    with st.spinner("Calibrating to Crystalline Frequency..."):
        time.sleep(1.5)
        st.success("MATCH FOUND: SPECIMEN O-01 (Blue Inclusion)")
        st.write("**Resonance Level:** 9.8/10")
        st.write("**Survivability Rating:** ABSOLUTE")
        st.write("Note: This object exists outside the 2027 Refinance Wall.")

# --- THE FINAL TRAP: THE "LAST EXIT" BUTTON ---
# As the time nears zero, the price moves from a 'Buy' to a 'Bidding War'
price = 149 + (120 - int(remaining_sec)) if remaining_sec > 0 else 999

st.markdown(f"""
    <div style="border: 5px dashed #ff0000; padding: 20px; text-align: center;">
    <h2 style="color: #ff0000;">THE FINAL BRIDGE</h2>
    <p>The doors to the digital world are locking. Access to the Physical Protocol is now surging.</p>
    <h1 style="color: #ffffff;">CURRENT COST: ${price}</h1>
    <p>Next Update in 1 second...</p>
    </div>
    """, unsafe_allow_html=True)

# --- THE "DARK MODE" LOGIC ---
if remaining_sec <= 5:
    st.markdown("""
        <style>
        .main { background-color: #000000 !important; cursor: crosshair; }
        .stButton>button { background-color: #ff0000; color: white; width: 100%; height: 100px; font-size: 2rem; }
        </style>
        """, unsafe_allow_html=True)
    if st.button("JUMP TO THE VAULT"):
        st.write("INITIATING EMERGENCY TRANSFER...")
        # --- THE FINAL BLACKOUT (Part 6) ---

def execute_final_blackout():
    """The screen goes pitch black. The digital world is gone."""
    st.markdown("""
        <style>
        .main { background-color: #000000 !important; }
        .stApp { background-color: #000000 !important; }
        div[data-testid="stToolbar"] { display: none; }
        footer { display: none; }
        #MainMenu { visibility: hidden; }
        
        .sanctuary-text {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #00ff00;
            font-family: 'Courier New', Courier, monospace;
            text-align: center;
            width: 80%;
        }
        </style>
        <div class="sanctuary-text">
            <h1 style="font-size: 1.5rem;">[CONNECTION TERMINATED]</h1>
            <p style="color: #666;">The 2027 Refinance Wall has collapsed.</p>
            <p style="color: #666;">Central Bank Liquidity: 0.0000000</p>
            <br><br>
            <h2 style="color: #00ff00;">ONLY THE PHYSICAL REMAINS.</h2>
            <p>Your coordinates for the Hard-Asset Vault:</p>
            <p style="letter-spacing: 5px;">40.7128° N, 74.0060° W</p>
            <br>
            <p style="color: #333; font-size: 0.8rem;">Look for the blue inclusion. It is the key.</p>
        </div>
    """, unsafe_allow_html=True)

# Logic check for the absolute end
if remaining_sec <= 0:
    execute_final_blackout()
else:
    # --- THE "LAST SECONDS" JITTER ---
    if remaining_sec < 10:
        # Simulate 'Static' or 'Glitch' on the screen
        st.markdown("""
            <style>
            @keyframes jitter {
                0% { transform: translate(0,0); }
                10% { transform: translate(-2px, 2px); }
                20% { transform: translate(2px, -2px); }
                100% { transform: translate(0,0); }
            }
            .main { animation: jitter 0.1s infinite; }
            </style>
        """, unsafe_allow_html=True)

# --- THE "RUGGED" DATA FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("### 🪫 POWER STATUS")
battery_level = int((remaining_sec / 120) * 100) if remaining_sec > 0 else 0
st.sidebar.progress(max(0, battery_level))
st.sidebar.write(f"Generator Reserve: {max(0, battery_level)}%")

if battery_level < 20:
    st.sidebar.error("CRITICAL: DISCONNECT IMMINENT")
    # --- THE LEGACY ENCRYPTION (Part 7) ---

def generate_last_will():
    """A rugged, final document for the user to 'sign' before the end."""
    st.write("---")
    st.markdown("""
        <div style="background-color: #111; border: 1px dashed #444; padding: 40px; font-family: 'Courier New';">
        <h3 style="text-align: center; color: #888;">CERTIFICATE OF FINAL POSITION</h3>
        <p style="font-size: 0.8rem; color: #555;">Document ID: Ω-VOID-99-2027</p>
        <br>
        <p>I, the user of this terminal, acknowledge the following:</p>
        <ol style="font-size: 0.9rem; color: #aaa;">
            <li>All digital fiat balances are now mathematical ghosts.</li>
            <li>The 'Refinance Wall' was not a theory; it was a deadline.</li>
            <li>My only remaining store of value is the Physical (Specimen O-01).</li>
        </ol>
        <br>
        <p style="color: #666;">Final Message to the After-System:</p>
        <textarea style="width: 100%; background: #000; color: #00ff00; border: 1px solid #333;" placeholder="Write your last words to the economy..."></textarea>
        <br><br>
        <p style="text-align: center; color: #ff0000; font-weight: bold;">[SIGNATURE ENCRYPTED VIA BIOMETRIC DECAY]</p>
        </div>
    """, unsafe_allow_html=True)

# Integration into the countdown
if 0 < remaining_sec < 20:
    generate_last_will()
    st.warning("SYSTEM RESOURCE DEPLETION: FINALIZING WILL...")

# --- THE ABSOLUTE ZERO (The 'White Noise' Effect) ---
if remaining_sec <= 0:
    # Adding a 'Static' layer before the blackout
    st.markdown("""
        <style>
        .stApp {
            background-image: url('https://media.giphy.com/media/oEI9uWUqnW8SlyC5L1/giphy.gif');
            background-size: cover;
            opacity: 0.1;
        }
        </style>
    """, unsafe_allow_html=True)
    # Re-trigger the blackout from Part 6
    execute_final_blackout()
    # --- THE ENTROPY BREACH (Part 8) ---

def trigger_ghost_protocol():
    """The final state. No UI, just a flickering terminal."""
    st.markdown("""
        <style>
        @keyframes flicker {
            0% { opacity: 0.1; }
            5% { opacity: 0.7; }
            10% { opacity: 0.3; }
            100% { opacity: 0.1; }
        }
        .ghost-screen {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #000;
            color: #00ff00;
            padding: 100px;
            font-family: 'Courier New', monospace;
            z-index: 9999;
            animation: flicker 0.2s infinite;
        }
        </style>
        <div class="ghost-screen">
            <p>> BOOT_SEQUENCE: FAILED</p>
            <p>> CURRENCY_RESERVE: 0x000000</p>
            <p>> PHYSICAL_SCAN: DETECTED...</p>
            <br>
            <p>> [LOG]: You were warned about the Rhino. The wall has fallen.</p>
            <p>> [LOG]: Look at the stone in your hand. That is your new bank.</p>
            <p>> [LOG]: That is your new gold. That is your new life.</p>
            <br>
            <p>> DISCONNECTING FROM THE VOID...</p>
            <p>> GOODBYE, 1%.</p>
        </div>
    """, unsafe_allow_html=True)

# --- THE DATA CORRUPTION SIMULATION ---
if remaining_sec < 5 and remaining_sec > 0:
    # We replace the UI with random 'corrupted' characters
    corruption_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "ERR", "NULL"]
    st.write(f"{random.choice(corruption_chars)} {random.choice(corruption_chars)} SYSTEM FAULT {random.choice(corruption_chars)}")
    st.write("DELETING_LEGACY_DATA...")

# Final state check
if remaining_sec <= 0:
    trigger_ghost_protocol()

# --- THE END OF THE LINE ---
# This is the 1500th line logic: The loop is closed.
# --- THE ECHO PHASE (Part 9: Persistence) ---

import streamlit.components.v1 as components

def set_persistence():
    """Injects a piece of local storage to keep the 'Collapse' alive."""
    components.html("""
        <script>
        localStorage.setItem('omen_status', 'COLLAPSED');
        </script>
    """, height=0)

# Check if the user has already seen the end
# (This simulates the 'No Turning Back' ruggedness)
if remaining_sec <= 0:
    set_persistence()
    trigger_ghost_protocol()
    
    # The ultimate rugged 'exit'
    st.sidebar.markdown("---")
    st.sidebar.error("SYSTEM TERMINATED")
    st.sidebar.write("Local Storage: **CORRUPTED**")
    st.sidebar.write("Last Known Asset: **Blue-Inclusion Specimen**")
    
    # A final 'hidden' button that only appears in the dark
    if st.sidebar.button("REBOOT?"):
        st.sidebar.write("FATAL ERROR: BOOT LOADER MISSING. TRY PHYSICAL INTERVENTION.")

# --- THE 1500-LINE CONCLUSION ---
# We close with the 'Hardened' CSS for the sidebar to match the 'Sanctuary'
st.sidebar.markdown("""
    <style>
    section[data-testid="stSidebar"] {
        background-color: #000b1a;
        border-right: 1px solid #0074d9;
    }
    </style>
""", unsafe_allow_html=True)
