import streamlit as st
import ollama
from database import get_conn


def show_harshi(colors):
    st.title("🤖 Harshi")
    st.caption("Harshi — Your personal AI fitness advisor powered by Llama 3.2")
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    if "ai_messages" not in st.session_state:
        st.session_state.ai_messages = []
    if "ai_history" not in st.session_state:
        st.session_state.ai_history = []

    conn = get_conn()
    profile = conn.execute("SELECT * FROM profile WHERE id=1").fetchone()
    conn.close()

    system_prompt = """You are Harshi, an expert AI fitness coach and nutritionist.
Your name is Harshi. Always introduce yourself as Harshi.
Give personalized, practical advice about workouts, nutrition, and healthy habits.
Keep responses concise, friendly and motivating. Use emojis."""

    if profile:
        system_prompt += f"""
User: {profile[1]}, Age: {profile[2]}, Weight: {profile[3]}kg,
Height: {profile[4]}cm, Goal: {profile[5]}, Activity: {profile[6]}"""

    if not st.session_state.ai_messages:
        welcome = "👋 Hi! I'm **Harshi**, your personal AI Fitness Coach! Ask me anything about workouts, nutrition, or healthy habits. I'm here to help you reach your goals! 💪"
        st.session_state.ai_messages.append({"role": "assistant", "content": welcome})

    for msg in st.session_state.ai_messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask Harshi anything about fitness..."):
        st.session_state.ai_messages.append({"role": "user", "content": prompt})
        st.session_state.ai_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("🤔 Harshi is thinking..."):
                response = ollama.chat(
                    model="llama3.2",
                    messages=[{"role": "system", "content": system_prompt}] +
                             st.session_state.ai_history
                )
                bot_msg = response["message"]["content"]
            st.markdown(bot_msg)
        st.session_state.ai_history.append({"role": "assistant", "content": bot_msg})
        st.session_state.ai_messages.append({"role": "assistant", "content": bot_msg})
        st.rerun()