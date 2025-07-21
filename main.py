# main.py

import json
from form_scraper import scrape_form_structure
from ai_answer_generator import generate_answers_with_gpt
from form_filler import fill_form


def load_personas():
    """
    Load personas from a JSON file.
    """
    with open("personas.json", "r") as f:
        return json.load(f)


def process_form(form_url, personas):
    """
    Scrape the form, generate answers, and fill it for each persona.
    """
    # Scrape the form structure (questions, types, options)
    question_blocks = scrape_form_structure(form_url)

    # Loop through each persona and fill the form
    for persona in personas:
        print(f"Filling the form for: {persona['name']}")

        # Generate answers for this persona
        answers = generate_answers_with_gpt(persona, question_blocks)

        # Fill the form with generated answers
        fill_form(form_url, question_blocks, answers)


if __name__ == "__main__":
    # Your form URL here (the view-only URL)
    form_url = "https://docs.google.com/forms/d/1HoO1Lo9lh7GaqlRql0KnIcWDmyBiwzA8uUGeOjSuo_E/viewform"

    # Load personas
    personas = load_personas()

    # Process the form
    process_form(form_url, personas)
