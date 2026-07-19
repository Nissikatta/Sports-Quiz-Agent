# 🏆 AI Powered Sports Quiz Generator

## Project Overview

This project is an AI-powered Sports Quiz Generator that creates multiple-choice sports quizzes using Retrieval-Augmented Generation (RAG).

The application combines:

- ChromaDB Vector Database for historical sports facts
- DuckDuckGo Web Search for recent sports news
- Groq LLM (Llama 3.3 70B Versatile) for quiz generation
- Streamlit for the user interface

The generated quizzes are based on retrieved knowledge to reduce hallucinations and improve factual accuracy.

---

## Features

- Select Sport
- Select Difficulty
- Generate AI-powered quizzes
- Retrieve historical facts using ChromaDB
- Retrieve recent sports news from the web
- Regenerate quiz
- Download generated quiz as PDF
- Simple Streamlit dashboard


----

## Technologies Used

- Python
- Streamlit
- ChromaDB
- DuckDuckGo Search
- Groq API
- Llama 3.3 70B Versatile

---

## Project Structure


Sports-Quiz-Agent/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── sports_facts.json
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── generator.py
│   └── search.py
│
└── chroma_db/


---

## Setup Instructions

### Clone the project

bash
git clone <repository_url>


### Install dependencies

bash
pip install -r requirements.txt


### Create .env file


GROQ_API_KEY=your_api_key


### Run the application

bash
streamlit run app.py


---

## Output

The application generates:

- Sport Name
- Difficulty Level
- 5 Multiple Choice Questions
- Four Options
- Correct Answer
- Explanation
- Historical Facts
- Recent Sports News

---

## AI Workflow

1. User selects Sport and Difficulty.
2. Historical facts are retrieved from ChromaDB.
3. Latest sports news is retrieved using DuckDuckGo Search.
4. Retrieved context is passed to the Groq LLM.
5. The AI generates accurate quiz questions.
6. Quiz is displayed in the Streamlit dashboard.

---

## Author

Nissi Katta