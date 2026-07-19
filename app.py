import streamlit as st
import time 
from fpdf import FPDF
from src.generator import generate_quiz
from src.generator import generate_quiz
from src.database import setup_and_populate_db

setup_and_populate_db()

st.set_page_config(
    page_title="Sports Quiz Generator",
    page_icon="🏆"
)

st.title("🏆 AI Powered Sports Quiz Generator")

sport = st.selectbox(
    "Select Sport",
    ["Cricket", "Football", "Tennis", "Basketball"]
)

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy", "Medium", "Hard"]
)

if st.button("Generate Quiz"):
    st.write("Calling generate_quiz...")
    with st.spinner("Generating Quiz..."):
        quiz = generate_quiz(sport, difficulty)
    
    st.write(f"*Sport:* {sport}")
    st.write(f"*Difficulty:* {difficulty}")
    
    st.subheader("Generated Quiz")
    st.markdown(quiz["quiz"])

    st.subheader("Historical Facts")
    for fact in quiz["historical_facts"]:
      st.write(f"- {fact}")

    st.subheader("Recent Sports News")
    for news in quiz["recent_news"]:
      st.write(f"*{news['title']}*")
      st.write(news["body"])
      st.write(news["link"])

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 10, quiz["quiz"])

    pdf.output("sports_quiz.pdf")

    with open("sports_quiz.pdf", "rb") as file:
      st.download_button(
        "📄 Download PDF",
        file,
        file_name="sports_quiz.pdf",
        mime="application/pdf"
    )
    
    if st.button("🔄 Regenerate Quiz"):
       st.rerun()