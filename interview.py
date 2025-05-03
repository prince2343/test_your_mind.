import streamlit as st
import openai

def run():
    st.title("🎙️ Mock Interview Bot")
    role = st.selectbox("Select Role", ["Developer", "HR", "Marketing", "Designer"])
    
    st.write("Answer the following question:")
    question = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Ask me one question for the role of {role}"}]
    )
    question_text = question['choices'][0]['message']['content']
    st.write(question_text)
    
    answer = st.text_area("Your Answer")
    if st.button("Submit Answer"):
        feedback = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"My answer: {answer}. Please provide feedback."}]
        )
        feedback_text = feedback['choices'][0]['message']['content']
        st.write(feedback_text)
