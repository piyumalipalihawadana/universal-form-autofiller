<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Form AI Autofiller</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/css/bootstrap.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f7f6;
            margin-top: 50px;
        }
        .container {
            max-width: 800px;
        }
        h1, h2, h3 {
            margin-bottom: 20px;
        }
        .btn-primary {
            width: 100%;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1 class="text-center">Google Form AI Autofiller</h1>
        <p class="text-center">AI-powered Google Form Autofiller is a Python-based tool that automates the process of filling out Google Forms using AI. It scrapes the form structure, generates realistic answers based on predefined personas, and automatically fills out the form with context-aware responses powered by OpenAI's GPT. It supports a variety of question types such as text, multiple-choice, checkboxes, and dropdowns.</p>

        <h2>Features</h2>
        <ul>
            <li>Scrapes Google Form questions dynamically.</li>
            <li>Generates answers using OpenAI GPT based on custom personas.</li>
            <li>Supports multiple question types: text, multiple-choice, checkboxes, dropdowns.</li>
            <li>Automatically fills out and submits the form.</li>
        </ul>

        <h2>Technologies Used</h2>
        <ul>
            <li><strong>Python</strong>: Core language used for implementation.</li>
            <li><strong>Selenium</strong>: For automating the scraping and filling of Google Forms.</li>
            <li><strong>OpenAI GPT</strong>: To generate AI-based responses.</li>
            <li><strong>Jinja2</strong>: For rendering prompt templates.</li>
            <li><strong>BeautifulSoup</strong>: For HTML parsing of Google Forms.</li>
        </ul>

        <h2>Setup Instructions</h2>
        <h3>1. Clone the Repository</h3>
        <pre><code>git clone https://github.com/yourusername/google-form-ai-autofiller.git</code></pre>

        <h3>2. Install Dependencies</h3>
        <pre><code>cd google-form-ai-autofiller
pip install -r requirements.txt</code></pre>

        <h3>3. Set Up Your .env File</h3>
        <p>Create a .env file in the root directory of the project and add your OpenAI API key:</p>
        <pre><code>OPENAI_API_KEY=your-openai-api-key-here</code></pre>

        <h3>4. Configure Personas</h3>
        <p>Edit the <code>personas.json</code> file to add custom personas (name, background, career goal). Example:</p>
        <pre><code>[
    {
        "name": "Amina",
        "background": "Final-year Data Science student passionate about ML",
        "goal": "Wants to become an AI researcher at Google"
    },
    {
        "name": "Ravi",
        "background": "Software Engineering undergraduate focused on DevOps",
        "goal": "Hopes to build cloud-native infrastructure at Meta"
    }
]</code></pre>

        <h3>5. Run the Script</h3>
        <pre><code>python main.py</code></pre>
        <p>The script will scrape the Google Form, generate answers for the selected personas, and automatically fill and submit the form.</p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.1.3/js/bootstrap.bundle.min.js"></script>
</body>
</html>
