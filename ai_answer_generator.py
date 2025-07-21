# ai_answer_generator.py

import openai
from dotenv import load_dotenv
import os
from jinja2 import Template

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt_template():
    with open("prompts/base_prompt.txt", "r", encoding="utf-8") as f:
        return Template(f.read())

prompt_template = load_prompt_template()

def generate_answers_with_gpt(persona, question_blocks):
    answers = {}

    for qblock in question_blocks:
        question = qblock["question"]
        qtype = qblock["type"]
        options = qblock.get("options")

        rendered_prompt = prompt_template.render(
            name=persona['name'],
            background=persona['background'],
            goal=persona['goal'],
            question=question,
            options=options
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful student assistant."},
                    {"role": "user", "content": rendered_prompt}
                ],
                temperature=0.7,
                max_tokens=100
            )

            answer = response['choices'][0]['message']['content'].strip()

            # Checkbox support
            if qtype == "checkbox" and options:
                answer = [opt.strip() for opt in answer.split(",") if opt.strip() in options]

            answers[question] = answer

        except Exception as e:
            print(f"❌ Error generating answer for: {question} → {e}")
            answers[question] = "[ERROR]"

    return answers
