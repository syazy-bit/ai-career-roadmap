from flask import Flask, render_template, request
from google import genai
import os

# Load environment variables from .env
if os.path.exists(".env"):
    with open(".env") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

app = Flask(__name__)

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client if API key exists
client = genai.Client(api_key=API_KEY) if API_KEY else None


@app.route("/", methods=["GET", "POST"])
def index():
    roadmap = ""

    if request.method == "POST":
        education = request.form.get("education")
        branch = request.form.get("branch")
        interests = request.form.get("interests")
        goal = request.form.get("goal")

        # 🔹 DEMO MODE (Hackathon safe)
        if not API_KEY:
            roadmap = """
DEMO MODE ENABLED ✅

CAREER PATH: SOFTWARE DEVELOPER (PYTHON)

SKILLS TO LEARN:
- Python fundamentals
- Flask web development
- SQL databases
- Git and GitHub

3-MONTH PLAN:
Month 1: Python basics and Git
Month 2: Flask, SQL, and a small project
Month 3: APIs and a final project
"""
            return render_template("index.html", roadmap=roadmap)

        # 🔹 Gemini Prompt (NO MARKDOWN)
        prompt = f"""
You are a professional career counselor.

STUDENT DETAILS:
Education: {education}
Branch: {branch}
Interests: {interests}
Career Goal: {goal}

TASK:
Create a beginner-friendly career roadmap.

IMPORTANT RULES:
- Do NOT use Markdown
- Do NOT use **, ##, or tables
- Use plain text only
- Use headings in CAPITAL LETTERS
- Use simple bullet points using hyphens (-)
"""

        try:
            response = client.models.generate_content(
                model="models/gemini-flash-lite-latest", contents=prompt
            )
            roadmap = response.text

        except Exception as e:
            roadmap = f"⚠️ Error generating roadmap.\n\n{e}"

    return render_template("index.html", roadmap=roadmap)


if __name__ == "__main__":
    app.run(debug=True)
