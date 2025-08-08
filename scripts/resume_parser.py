import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_skills(text, skill_keywords):
    found_skills = [skill for skill in skill_keywords if skill.lower() in text.lower()]
    return list(set(found_skills))

def extract_experience(text):
    match = re.findall(r'(\d+)\+?\s*(years|yrs)', text, re.IGNORECASE)
    if match:
        return max([int(m[0]) for m in match])
    return 0
