import streamlit as st
import random

# ------------------ Title ------------------
st.set_page_config(page_title="PrinceX.ai - Upgrade Yourself")
st.title("👑 PrinceX.ai - Your Personal Confidence Coach")

# ------------------ Confidence Quiz ------------------
st.header("🧠 Confidence Check")
st.write("Answer a few quick questions to check your confidence level.") 

questions = [
    ("Do you feel nervous speaking in front of people?", ["Yes", "No"]),
    ("Do you avoid eye contact during conversation?", ["Yes", "No"]),
    ("Do you often doubt your abilities?", ["Yes", "No"]),
    ("Can you introduce yourself boldly to a stranger?", ["Yes", "No"]),
    ("Are you comfortable speaking on a stage or camera?", ["Yes", "No"]),
    ("Do you feel comfortable making decisions on your own?", ["No", "Yes"]),
    ("Do you feel at ease giving feedback to others?", ["No", "Yes"]),
    ("Do you often feel positive about your future?", ["No", "Yes"]),
    ("Do you speak up in meetings or group discussions?", ["No", "Yes"]),
    ("Do you feel proud of your achievements, big or small??", ["No", "Yes"]),
]

score = 0
for i, (q, options) in enumerate(questions):
    answer = st.radio(q, options, key=i)
    if answer == "No":
        score += 1

# ------------------ Result ------------------
if st.button("Check Confidence Score"):
    st.subheader("🧾 Your Result:")
    if score <= 2:
        st.error("😟 Confidence Level: Low")
        st.write("Don't worry! PrinceX will help you boost your confidence every day.")
    elif score <= 4:
        st.warning("🙂 Confidence Level: Moderate")
        st.write("You're on your way! Just a little more practice and mindset shift.")
    else:
        st.success("🔥 Confidence Level: High")
        st.write("You're already a rising star! Keep shining with PrinceX ✨")

# ------------------ Daily Tip ------------------
st.header("📆 PrinceX's Daily Growth Tip")
daily_tips = [
    "Walk with your back straight and chest slightly out. Posture builds presence.",
    "Practice your name intro in the mirror with a smile for 3 minutes.",
    "Record your voice today and listen to how you sound. Improve tone & pace.",
    "Talk to a new person today — even a small conversation counts!",
    "Dress sharp today — the way you dress reflects your inner state.",
    "Look people in the eye for at least 3 seconds while speaking."
]
st.info(random.choice(daily_tips))

# ------------------ Footer ------------------
st.markdown("---")
st.caption("Made with 💙 by Prince & AI ✨")

 



