from flask import Flask, render_template, request
from google import genai
import os

# Load environment variables manually (simple way)
if os.path.exists(".env"):
    with open(".env") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os.environ[key] = value

app = Flask(__name__)

# Read API key from environment
API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client only if key exists
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

Career Path: Software Developer (Python)

Skills to Learn:
- Python fundamentals
- Flask web development
- SQL databases
- Git & GitHub

3-Month Plan:
Month 1: Python basics + Git
Month 2: Flask + SQL + small project
Month 3: APIs + final project

(This output is shown when API quota or key is unavailable.)
"""
            return render_template("index.html", roadmap=roadmap)

        # 🔹 Gemini Prompt
        prompt = f"""
You are a professional career counselor.

Student details:
Education: {education}
Branch: {branch}
Interests: {interests}
Career Goal: {goal}

Create a beginner-friendly career roadmap including:
1. Suitable career paths
2. Skills to learn step-by-step
3. Free learning resources
4. A 3-month learning plan
"""

        try:
            response = client.models.generate_content(
                model="models/gemini-flash-lite-latest",
                contents=prompt
            )
            roadmap = response.text

        except Exception as e:
            roadmap = f"⚠️ Error generating roadmap. Please try again later.\n\n{e}"

    return render_template("index.html", roadmap=roadmap)


if __name__ == "__main__":
    app.run(debug=True)
