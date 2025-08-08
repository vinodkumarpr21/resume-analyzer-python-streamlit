import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills, extract_experience

# Define job description keywords
with open("job_description.txt", "r") as f:
    job_desc = f.read()

JD_KEYWORDS = ['python', 'sql', 'streamlit', 'pandas', 'numpy', 'rest api', 'ml', 'machine learning', 'data science']

st.title("📄 Resume Analyzer App")

# File upload
resume_file = st.file_uploader("Upload Resume (PDF, Max 2MB)", type=["pdf"])

if resume_file is not None:
    # Check file size in bytes (2MB = 2 * 1024 * 1024 = 2,097,152 bytes)
    if resume_file.size > 2 * 1024 * 1024:
        st.error("❌ File size exceeds 2MB. Please upload a smaller file.")
    else:
        resume_text = extract_text_from_pdf(resume_file)

        st.subheader("🔍 Candidate Summary:")

        skills = extract_skills(resume_text, JD_KEYWORDS)
        experience = extract_experience(resume_text)
        
        match_score = int((len(skills) / len(JD_KEYWORDS)) * 100)

        st.write("**Skills Found:**", ', '.join(skills) if skills else "No relevant skills found")
        st.write("**Years of Experience:**", experience)
        st.write("**Match Score:**", f"{match_score} %")

        st.progress(match_score)

        with st.expander("📑 Full Resume Text"):
            st.text(resume_text)
