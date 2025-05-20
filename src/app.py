import streamlit as st
import pandas as pd
from mood_logger import get_sheet, log_mood, get_all_moods
from mood_plotter import filter_today, plot_moods

st.set_page_config(page_title="Mood of the Queue", layout="centered")
st.title("🧠 Mood of the Queue")

# Get Google Sheet
sheet = get_sheet()

# --- Mood Entry ---
st.subheader("Log Mood")
mood = st.selectbox("Mood", ["😊", "😠", "😕", "🎉"])
note = st.text_input("Optional note")
if st.button("Submit"):
    log_mood(sheet, mood, note)
    st.success("Mood logged!")

st.divider()

# --- Mood Visualization ---
st.subheader("Today’s Mood Trend")
records = get_all_moods(sheet)
df = pd.DataFrame(records)

if not df.empty:
    df_today = filter_today(df)
    if not df_today.empty:
        fig = plot_moods(df_today)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No moods logged today.")
else:
    st.info("No data yet.")
