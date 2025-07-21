# form_filler.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def fill_form(form_url, question_blocks, answers):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(form_url)
        time.sleep(3)

        blocks = driver.find_elements(By.CSS_SELECTOR, 'div[role="listitem"]')

        for i, block in enumerate(blocks):
            if i >= len(question_blocks):
                break

            qblock = question_blocks[i]
            qtype = qblock["type"]
            qtext = qblock["question"]
            answer = answers.get(qtext)

            try:
                if qtype == "text":
                    input_field = block.find_element(By.CSS_SELECTOR, 'input, textarea')
                    input_field.send_keys(answer)

                elif qtype == "radio":
                    radio_buttons = block.find_elements(By.CSS_SELECTOR, 'div[role="radiogroup"] span')
                    for btn in radio_buttons:
                        if btn.text.strip().lower() == answer.lower():
                            btn.click()
                            break

                elif qtype == "checkbox":
                    checkbox_labels = block.find_elements(By.CSS_SELECTOR, 'span')
                    if isinstance(answer, list):
                        for val in answer:
                            for label in checkbox_labels:
                                if label.text.strip().lower() == val.lower():
                                    label.click()
                                    break

                elif qtype == "dropdown":
                    dropdown = block.find_element(By.CSS_SELECTOR, 'div[role="listbox"]')
                    dropdown.click()
                    time.sleep(1)
                    options = block.find_elements(By.CSS_SELECTOR, 'div[role="option"]')
                    for opt in options:
                        if opt.text.strip().lower() == answer.lower():
                            opt.click()
                            break

                print(f"Filled: {qtext} ✅")

            except Exception as e:
                print(f"Failed to fill: {qtext} ❌ → {e}")

        # Click submit button
        submit_btn = driver.find_element(By.XPATH, '//span[contains(text(), "Submit")]/ancestor::div[@role="button"]')
        submit_btn.click()
        print("Form submitted successfully ✅")

        time.sleep(2)

    finally:
        driver.quit()
