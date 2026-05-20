import streamlit as st
from datetime import date
from database import init_db
from theme import get_theme_colors, apply_theme
from home import show_home
from profile import show_profile
from nutrition import show_nutrition
from gym import show_gym
from progress import show_progress
from harshi import show_harshi

st.set_page_config(
    page_title="AI Fitness Tracker",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Init ──────────────────────────────────────────────────────────────────────
init_db()

if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# ── Theme ─────────────────────────────────────────────────────────────────────
colors = get_theme_colors(st.session_state.theme)
apply_theme(colors)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("💪 AI Fitness Tracker")
    st.markdown(f'<div class="sidebar-date">📅 {date.today().strftime("%A, %B %d %Y")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Theme toggle
    st.markdown("### 🎨 Theme")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌙 Dark", use_container_width=True):
            st.session_state.theme = "dark"
            st.rerun()
    with col2:
        if st.button("☀️ Light", use_container_width=True):
            st.session_state.theme = "light"
            st.rerun()

    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    # Navigation
    pages = ["🏠 Home", "👤 My Profile", "💧 Water & Nutrition",
             "🏋️ Gym Diary", "📈 Progress", "🤖 Harshi AI Coach"]
    for p in pages:
        if st.button(p, use_container_width=True):
            st.session_state.page = p

    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ── Page Router ───────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "🏠 Home":
    show_home(colors)
elif page == "👤 My Profile":
    show_profile(colors)
elif page == "💧 Water & Nutrition":
    show_nutrition(colors)
elif page == "🏋️ Gym Diary":
    show_gym(colors)
elif page == "📈 Progress":
    show_progress(colors)
elif page == "🤖 Harshi AI Coach":
    show_harshi(colors)