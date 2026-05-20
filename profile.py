import streamlit as st
from database import get_conn, calculate_nutrition


def show_profile(colors):
    c = colors
    st.markdown('<div class="main-title">👤 My Profile</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Set up your profile for personalized AI recommendations</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    conn = get_conn()
    profile = conn.execute("SELECT * FROM profile WHERE id=1").fetchone()
    conn.close()

    with st.form("profile_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("👤 Your Name",
                                value=profile[1] if profile else "")
            age = st.number_input("🎂 Age", 10, 100,
                                 value=profile[2] if profile else 25)
            weight = st.number_input("⚖️ Weight (kg)", 30.0, 200.0,
                                    value=float(profile[3]) if profile else 70.0)
        with col2:
            height = st.number_input("📏 Height (cm)", 100.0, 250.0,
                                    value=float(profile[4]) if profile else 170.0)
            goal = st.selectbox("🎯 Fitness Goal",
                               ["Lose Weight", "Gain Muscle", "Stay Fit"],
                               index=["Lose Weight", "Gain Muscle", "Stay Fit"].index(profile[5]) if profile else 0)
            activity = st.selectbox("⚡ Activity Level",
                                   ["Sedentary", "Lightly Active",
                                    "Moderately Active", "Very Active"],
                                   index=["Sedentary", "Lightly Active",
                                          "Moderately Active", "Very Active"].index(profile[6]) if profile else 1)

        if st.form_submit_button("💾 Save Profile"):
            conn = get_conn()
            conn.execute("DELETE FROM profile WHERE id=1")
            conn.execute("INSERT INTO profile VALUES (1,?,?,?,?,?,?)",
                        (name, age, weight, height, goal, activity))
            conn.commit()
            conn.close()
            st.success(f"✅ Profile saved! Welcome, {name}! 🎉")

            goals = calculate_nutrition(weight, height, age, goal, activity)
            st.markdown('<div class="section-header">🤖 Your AI-Calculated Daily Goals</div>',
                       unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("🔥 Calories", f"{goals['calories']} kcal")
                st.metric("🥩 Protein", f"{goals['protein']}g")
            with col2:
                st.metric("🍚 Carbs", f"{goals['carbs']}g")
                st.metric("🥦 Fibre", f"{goals['fibre']}g")
            with col3:
                st.metric("💧 Water", f"{goals['water']}L")
                st.metric("🦠 Probiotics", goals['probiotics'])