import streamlit as st
from jinja2 import Template
import pdfkit
import tempfile

def run():
    st.title("📄 ResumeCraft AI")
    st.subheader("Create your professional resume in seconds")

    # Input Form
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    summary = st.text_area("Professional Summary")
    skills = st.text_area("Skills (comma separated)")
    education = st.text_area("Education (e.g., B.Tech in CSE, AKTU, 2025)")
    experience = st.text_area("Experience (e.g., 6-month internship at XYZ)")

    # Resume Generation Logic
    html_template = """<html>...your HTML template here...</html>"""  # same template from earlier

    if st.button("Generate Resume"):
        if not name or not email or not phone:
            st.warning("Please fill in all required fields.")
        else:
            template = Template(html_template)
            rendered_html = template.render(
                name=name, email=email, phone=phone, summary=summary, skills=skills, education=education, experience=experience
            )

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmpfile:
                pdfkit.from_string(rendered_html, tmpfile.name)
                st.success("✅ Resume generated successfully!")
                with open(tmpfile.name, "rb") as f:
                    st.download_button("📥 Download Resume", f, file_name="resume.pdf")
