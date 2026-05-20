import streamlit as st
from datetime import date
from database import get_conn, calculate_nutrition


def show_home(colors):
    c = colors
    st.markdown('<div class="main-title">💪 AI Fitness Tracker</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Your personal AI-powered health & fitness companion</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    conn = get_conn()
    profile = conn.execute("SELECT * FROM profile WHERE id=1").fetchone()
    today = str(date.today())
    nut = conn.execute("SELECT * FROM nutrition WHERE date=?", (today,)).fetchone()
    wo_count = conn.execute("SELECT COUNT(*) FROM workouts WHERE date=?", (today,)).fetchone()[0]
    conn.close()

    if not profile:
        st.markdown(f"""<div style="text-align:center;padding:40px;
            background:{c['card_bg']};border:1px solid {c['card_border']};
            border-radius:20px;margin:20px 0">
            <div style="font-size:48px">👋</div>
            <div style="font-size:20px;font-weight:700;color:#00d2ff;margin:12px 0">
                Welcome to AI Fitness Tracker!</div>
            <div style="color:{c['sub_color']}">Please set up your profile to get started</div>
            <div style="margin-top:12px;color:{c['text']}">
                Click <b>👤 My Profile</b> in the sidebar</div>
        </div>""", unsafe_allow_html=True)
    else:
        goals = calculate_nutrition(
            profile[3], profile[4], profile[2], profile[5], profile[6])
        water = nut[2] if nut else 0
        calories = nut[3] if nut else 0
        protein = nut[4] if nut else 0
        fibre = nut[6] if nut else 0

        # Metric Cards
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-icon">💧</div>
                <div class="metric-value">{water}L</div>
                <div class="metric-label">Water Today</div>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-icon">🔥</div>
                <div class="metric-value">{int(calories)}</div>
                <div class="metric-label">Calories</div>
            </div>""", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-icon">🏋️</div>
                <div class="metric-value">{wo_count}</div>
                <div class="metric-label">Exercises</div>
            </div>""", unsafe_allow_html=True)
        with col4:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-icon">⚖️</div>
                <div class="metric-value">{profile[3]}kg</div>
                <div class="metric-label">Weight</div>
            </div>""", unsafe_allow_html=True)

        # Progress
        st.markdown('<div class="section-header">🎯 Daily Goals Progress</div>',
                   unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            w_pct = min(int((water / goals["water"]) * 100), 100)
            st.markdown(f'<div class="progress-label"><span>💧 Water</span><span class="progress-percent">{w_pct}%</span></div>',
                       unsafe_allow_html=True)
            st.progress(w_pct / 100)
            c_pct = min(int((calories / goals["calories"]) * 100), 100)
            st.markdown(f'<div class="progress-label"><span>🔥 Calories</span><span class="progress-percent">{c_pct}%</span></div>',
                       unsafe_allow_html=True)
            st.progress(c_pct / 100)
        with col2:
            p_pct = min(int((protein / goals["protein"]) * 100), 100)
            st.markdown(f'<div class="progress-label"><span>🥩 Protein</span><span class="progress-percent">{p_pct}%</span></div>',
                       unsafe_allow_html=True)
            st.progress(p_pct / 100)
            f_pct = min(int((fibre / goals["fibre"]) * 100), 100)
            st.markdown(f'<div class="progress-label"><span>🥦 Fibre</span><span class="progress-percent">{f_pct}%</span></div>',
                       unsafe_allow_html=True)
            st.progress(f_pct / 100)