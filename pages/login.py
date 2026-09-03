import streamlit as st
import json
st.title("Login Page Loaded")
st.title("LoginForm")
with st.form("LoginForm"):
    
    e=st.text_input("Email",placeholder="Enter Email here")
    p=st.text_input("Password",placeholder="Enter Password here",type="password")
    btn=st.form_submit_button("Login")


    if btn:
    
            with open("users.json", "r") as r_file:
                all_users = json.load(r_file)
    
            for user in all_users:
    
                if user["email"] == e and user["password"] == p:
    
                    # Store logged-in user
                    st.session_state["loggedin_user"] = {
                        "email": user["email"],
                        "role": user["role"]
                    }
    
                    # Redirect according to role
                    if user["role"] == "Recruiter":
    
                        st.success("Logged in as Recruiter")
                        st.switch_page("pages/RecruiterDashboard.py")
    
                    elif user["role"] == "JobSeeker":
    
                        st.success("Logged in as JobSeeker")
                        st.switch_page("pages/JobSeekerDashboard.py")
    
                    break
    
            else:
                st.error("Invalid email or password")