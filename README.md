SkillBridge-AI 🚀

AI-Powered Career Guidance and Skill Gap Analysis Platform

SkillBridge-AI is an AI-powered career guidance platform designed to help students understand their career readiness, identify skill gaps, and plan what they should learn next.

The platform analyzes a student's current skills against different career paths, calculates skill-match percentages, identifies missing skills, and provides a personalized learning roadmap.

---

🎯 Problem Statement

Many students are unsure about:

- Which career is suitable for their skills
- Whether they are ready for a particular career
- Which skills they are missing
- What they should learn next
- How to build a roadmap toward their target career

Students often have to search through multiple websites and resources to find this information.

SkillBridge-AI brings these career guidance features together in one platform.

---

💡 Solution

SkillBridge-AI allows students to:

1. Create an account and log in securely.
2. Select a target career.
3. Enter their existing technical skills.
4. Analyze their career readiness.
5. Compare their skills with career requirements.
6. Identify missing skills.
7. View their skill gap.
8. Get recommended next actions.
9. Follow a step-by-step career roadmap.
10. Generate and download a career analysis report.

---

✨ Key Features

🔐 User Authentication

- User registration
- Login system
- Password reset functionality
- User-specific access

🎯 Career Selection

Students can select a target career from available career options.

📊 Skill Progress

The application compares the student's current skills with the skills required for the selected career.

📈 Career Readiness

A percentage-based readiness score helps students understand how prepared they are for their selected career.

🔍 Skill Gap Analysis

The application identifies skills that the student still needs to learn.

💼 Career Recommendation

When enough skills are provided, SkillBridge-AI can identify career options that best match the student's current skill set.

🗺️ Learning Roadmap

Students receive a step-by-step roadmap showing what they can learn next.

⚡ Next Action

The application provides a practical next step based on the student's current skill gap.

📄 PDF Career Report

Students can generate and download a career analysis report containing their career readiness and skill information.

🤖 AI Assistance

The application uses AI capabilities to provide additional career guidance and personalized assistance.

🔄 Reset

Students can reset their current skill selection and start a new analysis.

---

🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- OpenAI API
- ReportLab
- SQLite
- Git & GitHub

---

🧠 How It Works

Student
   ↓
Create Account / Login
   ↓
Select Target Career
   ↓
Enter Current Skills
   ↓
Skill Analysis
   ↓
Career Readiness Score
   ↓
Skill Gap Detection
   ↓
Career Recommendation
   ↓
Learning Roadmap
   ↓
Next Action
   ↓
Download Career Report

---

📊 Example

Suppose a student has:

Python
Machine Learning
NumPy
Pandas
Scikit-learn

A selected career may require 10 skills.

If the student has 6 of the required skills:

Career Readiness = 60%
Skill Gap = 40%

The application then identifies the missing skills and suggests what the student can learn next.

---

📁 Project Structure

SkillBridge-AI/
│
├── app.py
├── auth.py
├── careers.csv
├── requirements.txt
├── README.md
│
├── src/
│   └── ...
│
└── .gitignore

---

⚙️ Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the project

cd SkillBridge-AI

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

For Windows PowerShell:

venv\Scripts\Activate.ps1

5. Install dependencies

pip install -r requirements.txt

---

🔑 OpenAI API Configuration

Create a Streamlit secrets file:

.streamlit/secrets.toml

Add:

OPENAI_API_KEY = "your_api_key_here"

Never upload your API key to GitHub.

Make sure ".streamlit/secrets.toml" is included in ".gitignore".

---

▶️ Run the Application

Start the Streamlit application using:

python -m streamlit run app.py

The application will open in your browser.

---

🌐 Deployment

SkillBridge-AI can be deployed as a web application using Streamlit-compatible hosting.

Before deployment:

1. Upload the project to GitHub.
2. Add all required dependencies to "requirements.txt".
3. Configure the required secrets/API keys on the hosting platform.
4. Select "app.py" as the main application file.
5. Deploy the application.

---

🔒 Security

- API keys should be stored using environment variables or Streamlit secrets.
- Passwords should not be stored as plain text.
- Sensitive configuration files should be excluded from GitHub.
- User authentication should be handled securely.

---

🚀 Future Enhancements

Future versions of SkillBridge-AI could include:

- AI-powered career chatbot
- More career options
- Resume analysis
- Personalized course recommendations
- Internship recommendations
- Job recommendations
- Skill verification
- Learning progress tracking
- Integration with online learning platforms
- Advanced AI career recommendations
- User dashboard and analytics
- Personalized project recommendations

---

🎓 Target Users

SkillBridge-AI is mainly designed for:

- College students
- Beginners entering technology careers
- Students learning AI/ML
- Students preparing for internships
- Students exploring different technology career paths

---

🌟 Project Goal

The goal of SkillBridge-AI is to bridge the gap between a student's current skills and their desired career by providing personalized career guidance, skill-gap analysis, and actionable learning paths.

---

👩‍💻 Developer

Developed as an AI/ML portfolio and hackathon project.

SkillBridge-AI — Build Skills. Bridge Careers.