# 🚀 AI Career Roadmap Generator

An AI-powered web application that generates **personalized career roadmaps** for students and beginners based on their education, interests, and career goals, using **Google Gemini**.

This project is built as part of an **Open Innovation Hackathon** and focuses on solving the real-world problem of career confusion among students.

---

## 🌐 Live MVP Link

👉 https://ai-career-roadmap.onrender.com

---

## 🧠 Problem Statement

Many students struggle to decide:
- What skills to learn  
- Which career path suits them  
- How to plan their learning journey step-by-step  

Most online advice is generic and not personalized.

---

## 💡 Solution

The **AI Career Roadmap Generator** uses **Google Gemini** to create a **custom, beginner-friendly roadmap** tailored to each user’s:
- Education level  
- Field of study  
- Interests  
- Career goals  

The application also includes a **demo fallback mode**, ensuring the app works even if the AI API is unavailable.

---

## ✨ Key Features

- 🎯 Personalized AI-generated career roadmaps  
- 🤖 Powered by Google Gemini  
- 🧑‍🎓 Beginner-friendly guidance  
- 🔐 Secure API key handling using environment variables  
- 🌍 Cloud deployed (accessible from anywhere)  
- 🛡️ Demo mode for reliability  

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS
- Jinja Templates

### AI & Cloud
- Google Gemini API
- Google AI Studio
- Render (Deployment)

---

## 🤖 Google Technologies Used

- **Google Gemini API**
- **Google AI Studio**

---

## 🧪 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ai-career-roadmap.git
cd ai-career-roadmap
pip install -r requirements.txt
GEMINI_API_KEY=your_api_key_here
python app.py
http://127.0.0.1:5000

🌍 Deployment

The application is deployed on Render using:

Gunicorn as the production server

Environment variables for secure API key management

👤 Author

Ashimjyoti Nath
B.Tech Computer Science Engineering Student
Hackathon Project – Open Innovation
