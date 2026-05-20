import streamlit as st
from datetime import date
from database import get_conn


def show_nutrition(colors):
    c = colors
    st.markdown('<div class="main-title">💧 Water & Nutrition</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Track your daily nutrition intake</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    today = str(date.today())
    conn = get_conn()
    existing = conn.execute("SELECT * FROM nutrition WHERE date=?", (today,)).fetchone()
    conn.close()

    water = existing[2] if existing else 0.0
    calories = existing[3] if existing else 0.0
    protein = existing[4] if existing else 0.0
    carbs = existing[5] if existing else 0.0
    fibre = existing[6] if existing else 0.0
    probiotics = existing[7] if existing else "Not taken"

    st.markdown('<div class="section-header">💧 Water Tracker</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🥛 +250ml"):
            water = round(water + 0.25, 2)
    with col2:
        if st.button("🍶 +500ml"):
            water = round(water + 0.5, 2)
    with col3:
        if st.button("🪣 +1 Litre"):
            water = round(water + 1.0, 2)
    with col4:
        if st.button("🔄 Reset"):
            water = 0.0

    water_pct = min(int((water / 3.0) * 100), 100)
    st.markdown(f'<div class="progress-label"><span>💧 {water}L consumed</span><span class="progress-percent">{water_pct}%</span></div>',
               unsafe_allow_html=True)
    st.progress(water_pct / 100)

    st.markdown('<div class="section-header">🥗 Nutrition Log</div>', unsafe_allow_html=True)
    with st.form("nutrition_form"):
        col1, col2 = st.columns(2)
        with col1:
            calories = st.number_input("🔥 Calories (kcal)", 0.0, 5000.0, value=float(calories))
            protein = st.number_input("🥩 Protein (g)", 0.0, 500.0, value=float(protein))
            carbs = st.number_input("🍚 Carbs (g)", 0.0, 1000.0, value=float(carbs))
        with col2:
            fibre = st.number_input("🥦 Fibre (g)", 0.0, 100.0, value=float(fibre))
            probiotics = st.selectbox("🦠 Probiotics", ["Not taken", "Taken"],
                                     index=1 if probiotics == "Taken" else 0)
        if st.form_submit_button("💾 Save Nutrition"):
            conn = get_conn()
            conn.execute("DELETE FROM nutrition WHERE date=?", (today,))
            conn.execute("INSERT INTO nutrition VALUES (NULL,?,?,?,?,?,?,?)",
                        (today, water, calories, protein, carbs, fibre, probiotics))
            conn.commit()
            conn.close()
            st.success("✅ Nutrition saved for today!")