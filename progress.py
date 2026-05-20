import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_conn


def show_progress(colors):
    c = colors
    st.markdown('<div class="main-title">📈 Progress</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Track your fitness journey over time</div>', unsafe_allow_html=True)
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

    conn = get_conn()
    nut_df = pd.read_sql(
        "SELECT * FROM nutrition ORDER BY date DESC LIMIT 7", conn)
    wo_df = pd.read_sql(
        "SELECT date, COUNT(*) as exercises, SUM(calories_burned) as calories FROM workouts GROUP BY date ORDER BY date DESC LIMIT 7", conn)
    conn.close()

    plot_bg = "rgba(0,0,0,0)"
    font_col = c['text']

    if nut_df.empty:
        st.markdown(f"""<div style="text-align:center;padding:40px;
            background:{c['card_bg']};border:1px dashed {c['card_border']};
            border-radius:16px;color:{c['sub_color']}">
            📊 No data yet! Start logging to see progress charts.
        </div>""", unsafe_allow_html=True)
    else:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="section-header">💧 Water Intake</div>', unsafe_allow_html=True)
            fig = px.bar(nut_df, x="date", y="water",
                        color_discrete_sequence=["#00d2ff"])
            fig.update_layout(plot_bgcolor=plot_bg,
                             paper_bgcolor=plot_bg,
                             font_color=font_col,
                             showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.markdown('<div class="section-header">🔥 Calories</div>', unsafe_allow_html=True)
            fig2 = px.line(nut_df, x="date", y="calories",
                          color_discrete_sequence=["#7b2ff7"], markers=True)
            fig2.update_layout(plot_bgcolor=plot_bg,
                              paper_bgcolor=plot_bg,
                              font_color=font_col,
                              showlegend=False)
            st.plotly_chart(fig2, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="section-header">🥩 Protein</div>', unsafe_allow_html=True)
            fig3 = px.bar(nut_df, x="date", y="protein",
                         color_discrete_sequence=["#ff6b6b"])
            fig3.update_layout(plot_bgcolor=plot_bg,
                              paper_bgcolor=plot_bg,
                              font_color=font_col,
                              showlegend=False)
            st.plotly_chart(fig3, use_container_width=True)
        with col2:
            if not wo_df.empty:
                st.markdown('<div class="section-header">💪 Workout Calories</div>', unsafe_allow_html=True)
                fig4 = px.bar(wo_df, x="date", y="calories",
                             color_discrete_sequence=["#34d399"])
                fig4.update_layout(plot_bgcolor=plot_bg,
                                  paper_bgcolor=plot_bg,
                                  font_color=font_col,
                                  showlegend=False)
                st.plotly_chart(fig4, use_container_width=True)