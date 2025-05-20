import pandas as pd
import plotly.express as px
from datetime import date


def filter_today(df):
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df[df["timestamp"].dt.date == date.today()]


def plot_moods(df_today):
    mood_counts = df_today["mood"].value_counts().reset_index()
    mood_counts.columns = ["Mood", "Count"]
    fig = px.bar(mood_counts, x="Mood", y="Count", color="Mood", text="Count",
                 title="Mood Count Today", height=400)
    fig.update_traces(textposition="outside")
    return fig
