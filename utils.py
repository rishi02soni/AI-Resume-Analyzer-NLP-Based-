import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()


def extract_skills(text):
    skills_db = [
        "python", "java", "sql", "machine learning", "deep learning",
        "html", "css", "javascript", "react", "spring", "hibernate",
        "pandas", "numpy"
    ]

    found_skills = []
    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return found_skills
