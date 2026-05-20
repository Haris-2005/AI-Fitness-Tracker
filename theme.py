def get_theme_colors(theme):
    if theme == "dark":
        return {
            "bg": "linear-gradient(135deg, #0a0a0f 0%, #1a1a2e 50%, #16213e 100%)",
            "text": "#ccd6f6",
            "card_bg": "rgba(255,255,255,0.05)",
            "card_border": "rgba(0,210,255,0.2)",
            "sidebar_bg": "rgba(10,10,15,0.95)",
            "input_bg": "rgba(255,255,255,0.05)",
            "divider": "rgba(0,210,255,0.3)",
            "sub_color": "#8892b0",
        }
    else:
        return {
            "bg": "linear-gradient(135deg, #f0f4ff 0%, #e8eeff 50%, #dde8ff 100%)",
            "text": "#1a1a2e",
            "card_bg": "rgba(0,0,0,0.04)",
            "card_border": "rgba(123,47,247,0.25)",
            "sidebar_bg": "rgba(240,244,255,0.98)",
            "input_bg": "rgba(0,0,0,0.04)",
            "divider": "rgba(123,47,247,0.2)",
            "sub_color": "#4a5568",
        }


def apply_theme(colors):
    import streamlit as st
    c = colors
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
        * {{ font-family: 'Poppins', sans-serif !important; }}
        .stApp {{ background: {c['bg']}; min-height: 100vh; }}
        p, div, span, label {{ color: {c['text']} !important; }}
        .main-title {{
            text-align: center; font-size: 3rem; font-weight: 800;
            background: linear-gradient(90deg, #00d2ff, #7b2ff7, #ff6b6b, #00d2ff);
            background-size: 300% 300%;
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            animation: gradient 3s ease infinite;
        }}
        @keyframes gradient {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        .subtitle {{ text-align: center; color: {c['sub_color']}; font-size: 14px; margin-bottom: 20px; }}
        .metric-card {{
            background: {c['card_bg']}; border: 1px solid {c['card_border']};
            border-radius: 20px; padding: 24px 16px; text-align: center; margin: 8px 0;
            transition: all 0.3s ease;
        }}
        .metric-card:hover {{ transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,210,255,0.15); }}
        .metric-icon {{ font-size: 28px; margin-bottom: 8px; }}
        .metric-value {{
            font-size: 36px; font-weight: 800;
            background: linear-gradient(90deg, #00d2ff, #7b2ff7);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .metric-label {{ font-size: 11px; color: {c['sub_color']}; text-transform: uppercase; letter-spacing: 2px; }}
        .section-header {{
            font-size: 18px; font-weight: 700; color: #00d2ff;
            margin: 24px 0 12px 0; padding-left: 12px;
            border-left: 3px solid #00d2ff;
        }}
        .progress-label {{
            display: flex; justify-content: space-between;
            font-size: 13px; color: {c['text']}; margin-bottom: 4px; margin-top: 12px;
        }}
        .progress-percent {{ color: #00d2ff; font-weight: 600; }}
        .stButton > button {{
            background: linear-gradient(90deg, #00d2ff, #7b2ff7) !important;
            color: white !important; border: none !important;
            border-radius: 14px !important; font-weight: 600 !important;
            padding: 12px 20px !important; width: 100% !important;
            transition: all 0.3s ease !important;
        }}
        .stButton > button:hover {{
            transform: translateY(-3px) !important;
            box-shadow: 0 10px 30px rgba(0,210,255,0.4) !important;
        }}
        [data-testid="stSidebar"] {{
            background: {c['sidebar_bg']} !important;
            border-right: 1px solid {c['divider']} !important;
        }}
        .sidebar-title {{
            font-size: 20px; font-weight: 800;
            background: linear-gradient(90deg, #00d2ff, #7b2ff7);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            text-align: center; padding: 16px 0 4px 0;
        }}
        .sidebar-date {{ text-align: center; font-size: 12px; color: {c['sub_color']}; margin-bottom: 8px; }}
        .custom-divider {{
            height: 1px;
            background: linear-gradient(90deg, transparent, {c['divider']}, transparent);
            margin: 12px 0;
        }}
        .exercise-card {{
            background: {c['card_bg']}; border: 1px solid {c['card_border']};
            border-radius: 16px; padding: 16px; margin: 10px 0;
        }}
        .exercise-name {{ font-size: 16px; font-weight: 700; color: #00d2ff; margin-bottom: 6px; }}
        .exercise-detail {{ font-size: 13px; color: {c['sub_color']}; line-height: 1.8; }}
        .exercise-notes {{
            font-size: 12px; color: {c['sub_color']}; font-style: italic;
            margin-top: 6px; padding-top: 6px; border-top: 1px solid {c['divider']};
        }}
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input,
        .stTextArea > div > div > textarea {{
            background: {c['input_bg']} !important;
            border: 1px solid {c['card_border']} !important;
            border-radius: 12px !important; color: {c['text']} !important;
        }}
        .stSelectbox > div > div {{
            background: {c['input_bg']} !important;
            border: 1px solid {c['card_border']} !important;
            border-radius: 12px !important;
        }}
        .stChatMessage {{
            background: {c['card_bg']} !important;
            border: 1px solid {c['card_border']} !important;
            border-radius: 16px !important;
        }}
        #MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}}
    </style>
    """, unsafe_allow_html=True)