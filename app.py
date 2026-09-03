import streamlit as st

st.title("Job Portal")

if st.button("Login"):
    st.switch_page("pages/login.py")

if st.button("Register"):
    st.switch_page("pages/register.py")