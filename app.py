import streamlit as st
import pandas as pd

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch

st.set_page_config(
    page_title="Career Recommendation System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎯 SkillBridge-AI Career Recommendation")

st.caption(
    "Find your strongest career match and discover the skills you can built next. "
)

st.write(
    "Discover suitable career paths based on your current skills "
    "and identify the skills you can learn next. "
)

with st.expander("About this project"):
    st.write(
        "This AI Career Recommendation System compares a user's skills "
        "with predefined career skill requirements and recommends the "
        "career with the strongest match. "
    )

# Load career and skill data from CSV
df = pd.read_csv("career_skills.csv")

# Create career -> skills dictionary
career_skills = (
    df.groupby("career")["skill"]
    .apply(lambda skills: [str(skill).strip().lower() for skill in skills])
    .to_dict()
)


career_description = {
    "AI Engineer" : "Designs and develops artificial intelligence and machine learning system. ",
    "AI/ML Researcher" : "Conducts research to develop new artificial intelligence and machine learning methods, models, and algorithms. ",
    "Data Scientist" : "Analyst data, builds predictive models, and discovers use full pattern and insights. ",
    "Machine Learning Engineer" : "Builds, trains, evaluates, and deploys machine learning models for real-world applications. ",
    "Software Developer" : "Designs, develops, tests, and maintains software applications. ",
    "Backend Developer" : "Develops and maintains server-side logic, database, APIs, and systems that power applications. ",
    "Data Analyst" : "Analyzes data and create reports and visualizations to supports better decision-making. "
}

st.sidebar.header("Career Goal")

career_options = ["-- select a career --"] + list(career_skills.keys())

career = st.sidebar.selectbox(
    "Choose your target career: ",
    options=career_options
)

if career == "-- select a career --":
    st.sidebar.info("Select a career to explore its required skills and description. ")

if career != "-- select a career --":
    st.write("### About This Career")
    description = career_description.get(
    career,
    "This career involves applying relevant technical and professional skills in its field."
    )

    st.write(description)

    st.write("**Required Skills:** " + ", ".join([s.title() for s in career_skills[career]]))

st.write("### Your Skills")

st.write(
    "Enter your current skills seperated by commas. "
    "For example: Python, Pandas, Machine Learning. "
)

def reset_skills():
    st.session_state.skills_input = ""

skills_input = st.text_input(
    "Enter your skills: ",
    placeholder = "Example: Python, Pandas, Machine Learning ",
    key = "skills_input"
)

st.button("Reset", on_click=reset_skills)

user_skills = [
    skill.strip().lower()
    for skill in skills_input.split(",")
    if skill.strip()
]

if skills_input.strip() and len(user_skills) < 2:
    st.info(
        "Please enter at least two skills to get a more reliable recommendation. "
    )

if user_skills:
    st.write("### Your Entered Skills")
    st.write(", ".join(user_skills))
else:
    st.info("Enter your skills above to get started. ")

career_scores = {}

for career_name, required_skills in career_skills.items():
    score = 0

    for skill in user_skills:
        if skill in required_skills:
            score += 1

    career_scores[career_name] = score

if user_skills:
    best_career = max(career_scores, key=career_scores.get)
    best_score = career_scores[best_career]

    if best_score > 0:
        recommended_career = best_career
        recommended_score = best_score
    else:
        recommended_career = None
        recommended_score = 0

else:
    recommended_career = None
    recommended_score = 0 

if recommended_career is not None:
    total_required_skills = len(career_skills[recommended_career])
    match_percentage = (
        recommended_score / total_required_skills
    ) * 100

else:
    match_percentage = 0 

if st.button("Get Career Recommendation"):
    if len(user_skills) < 2:
        st.warning("Please enter at least 2 skills. ")
    elif recommended_career:
        st.write("### Recommended Career")
        st.success(recommended_career)

        if match_percentage == 100:
            st.balloons()

        st.write(f"Skill Match: {match_percentage: .1f}%")
        st.write(
            f"Your strongest match is {recommended_career} because "
            f"your skills align with the requirements of this career. "
        )
    else:
        st.warning(
            "None of the entered skills matched our current database. "
            "Try skills such as Python, SQL, Pandas, Machine Learning, Java, "
            "Statistics, Excel, Programming, Deep Learning,or Research. "
        )

if user_skills:
    st.write("### Career Match Scores")

    for career_name, score in career_scores.items():
        percentage = (score / len(career_skills[career_name])) * 100
        st.write(f"**{career_name}: {percentage: .1f}%**")
        st.progress(int(percentage) / 100)

if user_skills:
    sorted_careers = sorted(
        career_scores.items(),
        key = lambda item: item[1],
        reverse=True
    )

    st.write("### Top Career Matches")

    for career_name, score in sorted_careers[:3]:
        percentage = (score / len(career_skills[career_name])) * 100
        st.write(f"**{career_name}: {percentage: .1f}%**")

if recommended_career:
    missing_skills = [
        skill
        for skill in career_skills[recommended_career]
        if skill not in user_skills
    ]

if recommended_career:
    matching_skills = [
        skill
        for skill in user_skills
        if skill in 
career_skills[recommended_career]
    ]

    matched_count = len(matching_skills)
    total_count = total_required_skills

    st.write(f"Skill Match: {matched_count}/{total_count}")

    st.write("### Matching Skills")
    st.write(",".join(matching_skills))
    
    st.write("### Skills to Improve")

    if missing_skills:
        for skill in missing_skills:
            st.write(f"· {skill.title()}")
    else:
        st.success(
            "You already have all the listed skills for this career! 🎉 "
        )

# ==========================================
# SKILLBRIDGE-AI PERSONALIZED ROADMAP
# ==========================================

skill_roadmap = {

    "python": {
        "learn": "Python fundamentals, functions, data structures, OOP, file handling and modules.",
        "course": "Python for Everybody - Coursera",
        "practice": "Solve Python problems and build small programs.",
        "project": "Build a Student Management System using Python.",
        "certification": "Python certification or completion certificate."
    },

    "machine learning": {
        "learn": "Supervised learning, unsupervised learning, feature engineering, model evaluation and ML algorithms.",
        "course": "Machine Learning Specialization - Coursera",
        "practice": "Train regression and classification models.",
        "project": "Build a machine learning prediction application.",
        "certification": "Machine learning course certificate."
    },

    "deep learning": {
        "learn": "Neural networks, activation functions, backpropagation, CNNs, RNNs and model training.",
        "course": "Deep Learning Specialization - Coursera",
        "practice": "Train a neural network using a small dataset.",
        "project": "Build an image classification system.",
        "certification": "Deep learning course certificate."
    },

    "tensorflow": {
        "learn": "TensorFlow, tensors, neural networks, model training and evaluation.",
        "course": "TensorFlow Developer learning resources",
        "practice": "Train a neural network using TensorFlow.",
        "project": "Build an image classifier using TensorFlow.",
        "certification": "TensorFlow learning certificate."
    },

    "pytorch": {
        "learn": "PyTorch tensors, datasets, neural networks, training loops and model evaluation.",
        "course": "PyTorch official tutorials",
        "practice": "Train a neural network using PyTorch.",
        "project": "Build an image classification model.",
        "certification": "PyTorch course certificate."
    },

    "numpy": {
        "learn": "Arrays, indexing, slicing, reshaping, mathematical operations and numerical computing.",
        "course": "NumPy beginner tutorials",
        "practice": "Perform numerical calculations using NumPy.",
        "project": "Build a numerical data analysis project.",
        "certification": "NumPy course completion certificate."
    },

    "pandas": {
        "learn": "Data loading, cleaning, filtering, grouping, merging and data analysis.",
        "course": "Pandas learning tutorials",
        "practice": "Analyze CSV datasets using Pandas.",
        "project": "Build a data analysis dashboard.",
        "certification": "Data analysis course certificate."
    },

    "sql": {
        "learn": "SELECT, filtering, joins, grouping, aggregation, subqueries and database concepts.",
        "course": "SQL beginner course",
        "practice": "Write SQL queries using sample databases.",
        "project": "Build a Student Database Management System.",
        "certification": "SQL course certificate."
    },

    "statistics": {
        "learn": "Probability, distributions, mean, median, variance, correlation and hypothesis testing.",
        "course": "Statistics fundamentals course",
        "practice": "Analyze statistics from real datasets.",
        "project": "Create a statistical analysis report.",
        "certification": "Statistics course certificate."
    },

    "scikit-learn": {
        "learn": "Preprocessing, train-test split, model training, evaluation and prediction.",
        "course": "Scikit-learn tutorials",
        "practice": "Train different ML models.",
        "project": "Build a machine learning prediction app.",
        "certification": "Machine learning course certificate."
    },

    "matplotlib": {
        "learn": "Line charts, bar charts, scatter plots, histograms and data visualization.",
        "course": "Matplotlib tutorials",
        "practice": "Visualize real datasets.",
        "project": "Create a data visualization dashboard.",
        "certification": "Data visualization course certificate."
    },

    "seaborn": {
        "learn": "Statistical visualization, distributions, heatmaps and categorical plots.",
        "course": "Seaborn tutorials",
        "practice": "Create statistical charts.",
        "project": "Build an exploratory data analysis report.",
        "certification": "Data visualization course certificate."
    },

    "git": {
        "learn": "Repositories, commits, branches, merging, pull requests and GitHub workflows.",
        "course": "Git and GitHub beginner course",
        "practice": "Create repositories and push projects.",
        "project": "Publish an AI project on GitHub.",
        "certification": "Git/GitHub course certificate."
    },

    "docker": {
        "learn": "Containers, images, Dockerfiles, volumes and networking.",
        "course": "Docker beginner course",
        "practice": "Containerize a small application.",
        "project": "Dockerize your AI/ML application.",
        "certification": "Docker course certificate."
    },

    "kubernetes": {
        "learn": "Pods, deployments, services, containers and Kubernetes architecture.",
        "course": "Kubernetes beginner course",
        "practice": "Deploy a containerized application.",
        "project": "Deploy an ML application using Kubernetes.",
        "certification": "Kubernetes course certificate."
    },

    "aws": {
        "learn": "EC2, S3, IAM, Lambda, networking and basic cloud architecture.",
        "course": "AWS Cloud Practitioner learning resources",
        "practice": "Deploy a simple application to AWS.",
        "project": "Deploy an AI application on AWS.",
        "certification": "AWS Certified Cloud Practitioner."
    },

    "azure": {
        "learn": "Azure compute, storage, networking, IAM and cloud services.",
        "course": "Microsoft Azure Fundamentals",
        "practice": "Deploy a simple application on Azure.",
        "project": "Deploy an AI application using Azure.",
        "certification": "Microsoft Azure Fundamentals."
    },

    "linux": {
        "learn": "Linux commands, filesystems, permissions, processes, networking and shell basics.",
        "course": "Linux fundamentals course",
        "practice": "Use Linux terminal commands daily.",
        "project": "Set up and manage a Linux server.",
        "certification": "Linux course certificate."
    },

    "java": {
        "learn": "Java syntax, OOP, collections, exception handling and file handling.",
        "course": "Java programming course",
        "practice": "Solve Java programming problems.",
        "project": "Build a Library Management System.",
        "certification": "Java course certificate."
    },

    "javascript": {
        "learn": "JavaScript fundamentals, functions, DOM, asynchronous programming and APIs.",
        "course": "JavaScript beginner course",
        "practice": "Build interactive web pages.",
        "project": "Build a JavaScript web application.",
        "certification": "JavaScript course certificate."
    },

    "html": {
        "learn": "HTML structure, semantic elements, forms, tables and accessibility.",
        "course": "HTML beginner course",
        "practice": "Create responsive web pages.",
        "project": "Build a personal portfolio website.",
        "certification": "HTML/CSS course certificate."
    },

    "css": {
        "learn": "Selectors, layouts, Flexbox, Grid, responsive design and animations.",
        "course": "CSS beginner course",
        "practice": "Recreate modern website layouts.",
        "project": "Build a responsive portfolio website.",
        "certification": "Web development course certificate."
    },

    "react": {
        "learn": "Components, props, state, hooks, routing and API integration.",
        "course": "React beginner course",
        "practice": "Build small React applications.",
        "project": "Build a React dashboard.",
        "certification": "React course certificate."
    },

    "c++": {
        "learn": "C++ syntax, OOP, STL, memory management and algorithms.",
        "course": "C++ programming course",
        "practice": "Solve algorithmic programming problems.",
        "project": "Build a C++ management application.",
        "certification": "C++ course certificate."
    },

    "c": {
        "learn": "C syntax, pointers, memory management, structures and algorithms.",
        "course": "C programming fundamentals",
        "practice": "Solve C programming problems.",
        "project": "Build an embedded or systems application.",
        "certification": "C programming course certificate."
    },

    "computer vision": {
        "learn": "Image processing, CNNs, object detection, segmentation and computer vision fundamentals.",
        "course": "Computer Vision course",
        "practice": "Work with image datasets.",
        "project": "Build an image classification application.",
        "certification": "Computer Vision course certificate."
    },

    "nlp": {
        "learn": "Text preprocessing, tokenization, embeddings, text classification and NLP models.",
        "course": "Natural Language Processing course",
        "practice": "Build text classification models.",
        "project": "Build a sentiment analysis application.",
        "certification": "NLP course certificate."
    },

    "transformers": {
        "learn": "Transformer architecture, attention, tokenization and transformer-based models.",
        "course": "Hugging Face NLP course",
        "practice": "Experiment with pretrained transformer models.",
        "project": "Build a text classification system using Transformers.",
        "certification": "NLP/Transformers course certificate."
    },

    "llms": {
        "learn": "Large language models, tokenization, prompting, embeddings, RAG and evaluation.",
        "course": "Large Language Models course",
        "practice": "Experiment with pretrained LLMs.",
        "project": "Build an AI chatbot.",
        "certification": "Generative AI course certificate."
    },

    "generative ai": {
        "learn": "Generative AI, LLMs, prompting, embeddings, RAG and AI application development.",
        "course": "Generative AI course",
        "practice": "Build small AI-powered applications.",
        "project": "Build a document-based AI chatbot.",
        "certification": "Generative AI course certificate."
    },

    "prompt engineering": {
        "learn": "Prompt design, few-shot prompting, structured outputs and prompt evaluation.",
        "course": "Prompt Engineering course",
        "practice": "Create and evaluate different prompts.",
        "project": "Build an AI prompt-based assistant.",
        "certification": "Generative AI course certificate."
    },

    "automation": {
        "learn": "Python automation, APIs, scripting, workflow automation and AI automation.",
        "course": "Python Automation course",
        "practice": "Automate repetitive tasks.",
        "project": "Build an AI-powered task automation tool.",
        "certification": "Automation course certificate."
    },

    "excel": {
        "learn": "Formulas, functions, sorting, filtering, charts and pivot tables.",
        "course": "Microsoft Excel course",
        "practice": "Analyze real datasets.",
        "project": "Build a Sales Analysis Dashboard.",
        "certification": "Microsoft Excel certification."
    },

    "power bi": {
        "learn": "Data modeling, Power Query, DAX, dashboards and visualization.",
        "course": "Microsoft Power BI learning",
        "practice": "Create interactive dashboards.",
        "project": "Build a Business Intelligence dashboard.",
        "certification": "Microsoft Power BI certification."
    },

    "tableau": {
        "learn": "Data connections, charts, dashboards, filters and data storytelling.",
        "course": "Tableau learning course",
        "practice": "Create interactive dashboards.",
        "project": "Build a business analytics dashboard.",
        "certification": "Tableau certification."
    },

    "research methods": {
        "learn": "Literature review, research methodology, experiments, analysis and scientific writing.",
        "course": "Research methodology course",
        "practice": "Read and summarize research papers.",
        "project": "Write a mini AI/ML research paper.",
        "certification": "Research methodology certificate."
    }
}


# ==========================================
# GENERATE PERSONALIZED ROADMAP
# ==========================================

if recommended_career and missing_skills:

    st.write("### 🗺️ Personalized Learning Roadmap")

    st.write(
        f"Your roadmap for becoming a **{recommended_career}** "
        "is based on the skills you are currently missing."
    )

    for number, skill in enumerate(missing_skills, start=1):

        st.write(f"## Step {number}: {skill.title()}")

        if skill in skill_roadmap:

            roadmap = skill_roadmap[skill]

            st.write("📚 **What to Learn**")
            st.write(roadmap["learn"])

            st.write("🎓 **Recommended Course / Resource**")
            st.write(roadmap["course"])

            st.write("🛠️ **Practice**")
            st.write(roadmap["practice"])

            st.write("🚀 **Recommended Project**")
            st.write(roadmap["project"])

            st.write("🏆 **Certification**")
            st.write(roadmap["certification"])

        else:

            st.write("📚 **What to Learn**")
            st.write(
                f"Learn the fundamentals of **{skill.title()}** "
                f"and understand how it is used in **{recommended_career}**."
            )

            st.write("🛠️ **Practice**")
            st.write(
                f"Complete practical exercises using {skill.title()}."
            )

            st.write("🚀 **Recommended Project**")
            st.write(
                f"Build a small project using {skill.title()} "
                f"related to {recommended_career}."
            )

            st.write("🏆 **Certification**")
            st.write(
                f"Consider completing a recognized {skill.title()} course "
                "or certification."
            )

        st.divider()

if recommended_career:
    st.divider()

    st.subheader("Your Career Recommendation")

    st.write(
        f"Based on the skills you entered, "
        f"**{recommended_career}** is your strongest career match. "
    )

    st.metric(
        "Best Skill Match",
        f"{match_percentage: .1f}%"
    )

    st.progress(int(match_percentage) / 100)

if recommended_career:
    st.write("### About Your Recommended Career ")
    st.write(
    career_description.get(
        recommended_career,
        "Description for this career is currently unavailable."
        )
    )

if recommended_career:
    st.info(
        "This recommendation is based on the skills provided and is "
        "intended as a guidance tool. You can explore multiple careers "
        "and continue developing your skills. "
    )

    st.divider()

    st.caption("Career Recommendation System | Built with python and streamlit")

if recommended_career:

    from io import BytesIO

    pdf_buffer = BytesIO()

    doc = SimpleDocTemplate(
        pdf_buffer,
        pagesize=A4,
        rightMargin=50,
        leftMargin=50,
        topMargin=50,
        bottomMargin=50
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "TitleStyle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "HeadingStyle",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=8
    )

    normal_style = styles["BodyText"]

    story = []

    # ==========================================
    # TITLE
    # ==========================================

    story.append(
        Paragraph("SKILLBRIDGE-AI", title_style)
    )

    story.append(
        Paragraph(
            "Personalized Career Report",
            heading_style
        )
    )

    story.append(Spacer(1, 10))

    # ==========================================
    # CAREER
    # ==========================================

    story.append(
        Paragraph(
            f"<b>Recommended Career:</b> {recommended_career}",
            normal_style
        )
    )

    story.append(Spacer(1, 8))

    story.append(
        Paragraph(
            f"<b>Skill Match:</b> {match_percentage:.1f}%",
            normal_style
        )
    )

    story.append(Spacer(1, 15))

    # ==========================================
    # MATCHING SKILLS
    # ==========================================

    story.append(
        Paragraph(
            "Matching Skills",
            heading_style
        )
    )

    for skill in matching_skills:
        story.append(
            Paragraph(
                f"✓ {skill.title()}",
                normal_style
            )
        )

    # ==========================================
    # SKILLS TO IMPROVE
    # ==========================================

    story.append(
        Paragraph(
            "Skills to Improve",
            heading_style
        )
    )

    if missing_skills:

        for skill in missing_skills:
            story.append(
                Paragraph(
                    f"• {skill.title()}",
                    normal_style
                )
            )

    else:

        story.append(
            Paragraph(
                "You already have all the required skills!",
                normal_style
            )
        )

    # ==========================================
    # CAREER DESCRIPTION
    # ==========================================

    story.append(
        Paragraph(
            "About Your Recommended Career",
            heading_style
        )
    )

    description = career_description.get(
        recommended_career,
        "This career involves applying relevant technical and professional skills in its field."
    )

    story.append(
        Paragraph(
            description,
            normal_style
        )
    )

    # ==========================================
    # PERSONALIZED ROADMAP
    # ==========================================

    story.append(
        Paragraph(
            "Personalized Learning Roadmap",
            heading_style
        )
    )

    if missing_skills:

        for number, skill in enumerate(
            missing_skills,
            start=1
        ):

            story.append(
                Paragraph(
                    f"Step {number}: {skill.title()}",
                    heading_style
                )
            )

            # ----------------------------------
            # CUSTOM ROADMAP
            # ----------------------------------

            if skill in skill_roadmap:

                roadmap = skill_roadmap[skill]

                story.append(
                    Paragraph(
                        f"<b>What to Learn:</b> {roadmap['learn']}",
                        normal_style
                    )
                )

                story.append(Spacer(1, 5))

                story.append(
                    Paragraph(
                        f"<b>Recommended Course / Resource:</b> {roadmap['course']}",
                        normal_style
                    )
                )

                story.append(Spacer(1, 5))

                story.append(
                    Paragraph(
                        f"<b>Practice:</b> {roadmap['practice']}",
                        normal_style
                    )
                )

                story.append(Spacer(1, 5))

                story.append(
                    Paragraph(
                        f"<b>Recommended Project:</b> {roadmap['project']}",
                        normal_style
                    )
                )

                story.append(Spacer(1, 5))

                story.append(
                    Paragraph(
                        f"<b>Certification:</b> {roadmap['certification']}",
                        normal_style
                    )
                )

            # ----------------------------------
            # DEFAULT ROADMAP
            # ----------------------------------

            else:

                story.append(
                    Paragraph(
                        f"<b>What to Learn:</b> Learn the fundamentals of {skill.title()} and understand how it is used in {recommended_career}.",
                        normal_style
                    )
                )

                story.append(Spacer(1, 5))

                story.append(
                    Paragraph(
                        f"<b>Practice:</b> Complete practical exercises using {skill.title()}.",
                        normal_style
                    )
                )

                story.append(Spacer(1, 5))

                story.append(
                    Paragraph(
                        f"<b>Recommended Project:</b> Build a small project using {skill.title()} related to {recommended_career}.",
                        normal_style
                    )
                )

                story.append(Spacer(1, 5))

                story.append(
                    Paragraph(
                        f"<b>Certification:</b> Consider completing a recognized {skill.title()} course or certification.",
                        normal_style
                    )
                )

            story.append(Spacer(1, 15))

    else:

        story.append(
            Paragraph(
                "No additional skills are required. You have completed the listed skill requirements!",
                normal_style
            )
        )

    # ==========================================
    # BUILD PDF
    # ==========================================

    doc.build(story)

    pdf_data = pdf_buffer.getvalue()

    # ==========================================
    # DOWNLOAD BUTTON
    # ==========================================

    st.download_button(
        label="📥 Download Career Report (PDF)",
        data=pdf_data,
        file_name="SkillBridge_AI_Career_Report.pdf",
        mime="application/pdf"
    )