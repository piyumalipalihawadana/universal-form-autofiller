# form_scraper.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def scrape_form_structure(form_url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    questions_data = []

    try:
        driver.get(form_url)
        time.sleep(3)

        # Get all question blocks
        question_blocks = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')

        for block in question_blocks:
            try:
                question_text = block.find_element(By.CSS_SELECTOR, '.M7eMe').text.strip()
                question_type = "unknown"
                options = []

                # Check for input types
                if block.find_elements(By.CSS_SELECTOR, 'input[type="text"], textarea'):
                    question_type = "text"

                # Check for radio buttons
                elif block.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"]'):
                    question_type = "radio"
                    option_spans = block.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"] span')
                    options = [opt.text.strip() for opt in option_spans if opt.text.strip() != '']

                # Check for checkboxes
                elif block.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]'):
                    question_type = "checkbox"
                    checkbox_spans = block.find_elements(By.CSS_SELECTOR, 'span')
                    options = [opt.text.strip() for opt in checkbox_spans if opt.text.strip() != '']

                # Check for dropdowns
                elif block.find_elements(By.CSS_SELECTOR, 'div[role="listbox"]'):
                    question_type = "dropdown"
                    option_spans = block.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
                    options = [opt.text.strip() for opt in option_spans if opt.text.strip() != '']

                questions_data.append({
                    "question": question_text,
                    "type": question_type,
                    "options": options if options else None
                })

            except Exception as e:
                print(f"Error reading a question block: {e}")

    finally:
        driver.quit()

    return questions_data
