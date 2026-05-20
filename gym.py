import streamlit as st
from datetime import date
from database import get_conn


def show_gym(colors):
    c = colors
    st.markdown('<div class="main-title">🏋️ Gym Diary</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Log your workouts and track your gym progress</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    today = str(date.today())

    st.markdown('<div class="section-header">➕ Log New Exercise</div>', unsafe_allow_html=True)
    with st.form("workout_form"):
        col1, col2 = st.columns(2)
        with col1:
            exercise = st.text_input("💪 Exercise Name",
                                    placeholder="e.g. Bench Press, Squats")
            sets = st.number_input("🔢 Sets", 1, 20, value=3)
            reps = st.number_input("🔁 Reps per Set", 1, 100, value=10)
        with col2:
            weight_used = st.number_input("⚖️ Weight (kg)", 0.0, 500.0, value=0.0)
            duration = st.number_input("⏱️ Duration (minutes)", 1, 180, value=10)
            notes = st.text_area("📝 Notes",
                                placeholder="How did it feel? Any personal records?",
                                height=100)
        if st.form_submit_button("💾 Save Exercise"):
            if exercise:
                cal_burned = duration * 5
                conn = get_conn()
                conn.execute("INSERT INTO workouts VALUES (NULL,?,?,?,?,?,?,?,?)",
                            (today, exercise, sets, reps,
                             weight_used, duration, cal_burned, notes))
                conn.commit()
                conn.close()
                st.success(f"✅ {exercise} logged! 🔥 ~{cal_burned} cal burned!")
            else:
                st.error("Please enter exercise name!")

    st.markdown('<div class="section-header">📋 Today\'s Workout</div>', unsafe_allow_html=True)
    conn = get_conn()
    workouts = conn.execute(
        "SELECT * FROM workouts WHERE date=? ORDER BY id DESC", (today,)).fetchall()
    conn.close()

    if not workouts:
        st.markdown(f"""<div style="text-align:center;padding:32px;
            background:{c['card_bg']};border:1px dashed {c['card_border']};
            border-radius:16px;color:{c['sub_color']}">
            💪 No exercises logged today. Start your workout!
        </div>""", unsafe_allow_html=True)
    else:
        total_cal = sum(w[7] for w in workouts)
        total_time = sum(w[6] for w in workouts)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-icon">💪</div>
                <div class="metric-value">{len(workouts)}</div>
                <div class="metric-label">Exercises</div>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-icon">🔥</div>
                <div class="metric-value">{int(total_cal)}</div>
                <div class="metric-label">Cal Burned</div>
            </div>""", unsafe_allow_html=True)
        with col3:
            st.markdown(f"""<div class="metric-card">
                <div class="metric-icon">⏱️</div>
                <div class="metric-value">{total_time}m</div>
                <div class="metric-label">Total Time</div>
            </div>""", unsafe_allow_html=True)

        for w in workouts:
            st.markdown(f"""<div class="exercise-card">
                <div class="exercise-name">💪 {w[2]}</div>
                <div class="exercise-detail">
                    🔢 {w[3]} sets × 🔁 {w[4]} reps × ⚖️ {w[5]}kg<br>
                    ⏱️ {w[6]} min | 🔥 {int(w[7])} cal burned
                </div>
                {f'<div class="exercise-notes">📝 {w[8]}</div>' if w[8] else ''}
            </div>""", unsafe_allow_html=True)