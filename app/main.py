import streamlit as st
import plotly.express as px
from utils import load_data, filter_data

st.title("Africa Climate Dashboard")

df = load_data()
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["YEAR"].min()),
    int(df["YEAR"].max()),
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

filtered_df = filter_data(df, countries, year_range)

st.subheader("Climate Trend Over Time")

fig1 = px.line(
    filtered_df,
    x="DATE",
    y=variable,
    color="Country",
    title=f"{variable} Trend Over Time"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Precipitation Distribution")

fig2 = px.box(
    filtered_df,
    x="Country",
    y="PRECTOTCORR",
    color="Country"
)

st.plotly_chart(fig2, use_container_width=True)
