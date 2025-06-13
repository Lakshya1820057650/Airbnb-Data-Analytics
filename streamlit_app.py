import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Airbnb.csv")

st.title("Airbnb Data Dashboard")

st.sidebar.header("Filter")
room_type = st.sidebar.multiselect("Room Type", df["room_type"].unique(), default=df["room_type"].unique())

filtered_df = df[df["room_type"].isin(room_type)]

st.subheader("Room Type Distribution")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x="room_type", ax=ax)
st.pyplot(fig)

st.subheader("Price Distribution")
fig, ax = plt.subplots()
sns.histplot(data=filtered_df, x="price", bins=30, kde=True, ax=ax)
st.pyplot(fig)
