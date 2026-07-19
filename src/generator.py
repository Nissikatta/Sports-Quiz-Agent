from groq import Groq
from src.config import GROQ_API_KEY
from src.database import query_historic_facts
from src.search import search_recent_sports_news

client = Groq(api_key=GROQ_API_KEY)


def generate_quiz(sport: str, difficulty: str):
    
    print("generate_quiz function started")
    print("Step 1: Getting historical facts...")
    historical_facts = query_historic_facts(sport)

    print("Step 2: Searching recent news...")

    queries = {
        "Cricket": "ICC Cricket latest news",
        "Football": "FIFA Football latest news",
        "Tennis": "ATP Tennis latest news",
        "Basketball": "NBA Basketball latest news"
    }

    recent_news = search_recent_sports_news(
        queries.get(sport, f"{sport} sports latest news")
    )

    print(recent_news)

    history_context = "\n".join(historical_facts)

    news_context = "\n".join(
        [f"{item['title']} - {item['body']}" for item in recent_news]
    )

    prompt = f"""
You are an expert sports quiz generator.

Use ONLY the information below.

Historical Facts:
{history_context}

Recent Sports News:
{news_context}

Generate 5 multiple-choice questions about {sport}.

Difficulty: {difficulty}

For each question provide:

Question:
A)
B)
C)
D)

Correct Answer:
Explanation:
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
    )

    return {
        "quiz": response.choices[0].message.content,
        "historical_facts": historical_facts,
        "recent_news": recent_news,
    }