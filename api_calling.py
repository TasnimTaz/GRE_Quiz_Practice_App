import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

def generate_quiz(subject,difficulty):
    prompt = f"""
            You are an expert GRE exam question generator.

            Generate MULTIPLE GRE-level questions.

            STRICT REQUIREMENTS:
            - Subject: {subject}
            - Difficulty: {difficulty}
            - Questions MUST be from official GRE syllabus areas
            - Include different question types within the subject
            - Ensure exam-standard quality

            For English:
            - Reading comprehension
            - Vocabulary in context
            - Sentence equivalence
            - Text completion

            For Math:
            - Algebra
            - Arithmetic
            - Geometry
            - Data interpretation

            OUTPUT FORMAT (STRICT):

            Question 1:
            <question>

            Options:
            A. ...
            B. ...
            C. ...
            D. ...

            Question 2:
            <question>

            Options:
            A. ...
            B. ...
            C. ...
            D. ...

            (Generate 3 to 5 questions)

            IMPORTANT RULES:
            - DO NOT provide answers
            - DO NOT provide explanations
            - Each question must have exactly one correct answer
            - Vary difficulty within selected level
            - Make questions exam-realistic and non-repetitive
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
    return response.choices[0].message.content