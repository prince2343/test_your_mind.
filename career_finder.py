import streamlit as st

def run():
    st.title("🧭 Career Path Finder")
    st.write("Find the best career path based on your interests")

    interest = st.selectbox("What are you interested in?", ["Technology", "Business", "Design", "Art", "Education"])
    
    if interest == "Technology":
        st.write("Recommended Careers: Software Engineer, Data Scientist, AI Specialist")
    elif interest == "Business":
        st.write("Recommended Careers: Marketing Manager, Financial Analyst, Entrepreneur")
    elif interest == "Design":
        st.write("Recommended Careers: Graphic Designer, UI/UX Designer, Animator")
    elif interest == "Art":
        st.write("Recommended Careers: Painter, Sculptor, Art Director")
    elif interest == "Education":
        st.write("Recommended Careers: Teacher, Educational Consultant, Trainer")
