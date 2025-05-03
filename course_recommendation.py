import streamlit as st

def run():
    st.title("📚 Course Finder")
    st.write("Find the best courses to upskill in your career")

    field = st.selectbox("Select Career Field", ["Technology", "Business", "Design", "Art"])

    if field == "Technology":
        st.write("Recommended Courses: Python for Data Science (Coursera), Full Stack Development (Udemy)")
    elif field == "Business":
        st.write("Recommended Courses: Business Analytics (LinkedIn Learning), Marketing Strategy (Udemy)")
    elif field == "Design":
        st.write("Recommended Courses: UI/UX Design (Udemy), Graphic Design Masterclass (Skillshare)")
    elif field == "Art":
        st.write("Recommended Courses: Digital Painting (Udemy), Fine Art Photography (LinkedIn Learning)")
