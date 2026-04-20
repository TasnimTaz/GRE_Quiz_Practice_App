import os ,json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

def generate_quiz(subject,difficulty):
    prompt = f"""
            You are an expert GRE exam question generator.

            Generate exactly 4 GRE-level multiple choice questions.

            Subject: {subject}
            Difficulty: {difficulty}

            For English: reading comprehension, vocabulary in context, sentence equivalence, text completion.
            For Math: algebra, arithmetic, geometry, data interpretation.

            Return ONLY a valid JSON array. No explanation, no extra text, no markdown code fences.

            Use exactly this structure:
            [
            {{
                "id": 1,
                "question": "...",
                "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
                "answer": "B",
                "explanation": "..."
            }}
            ]

            Rules:
            - "answer" must be only a single letter: A, B, C, or D
            - Each question must have exactly one correct answer
            - "explanation" should be 1-2 sentences max
            - Questions must be exam-realistic and non-repetitive
            - Vary question types within the subject
            """
    
    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages=[
            {
                "role" : "user",
                "content" : prompt
            }
        ]
    )
    output = response.choices[0].message.content.strip()
    return json.loads(output)
