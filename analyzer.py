from utils import extract_text_from_pdf, extract_skills

def analyze_resume(file, job_role):

    text = extract_text_from_pdf(file)
    resume_skills = extract_skills(text)

    job_skills_map = {
        "data scientist": ["python", "machine learning", "pandas", "numpy", "sql"],
        "java developer": ["java", "spring", "hibernate", "sql"],
        "web developer": ["html", "css", "javascript", "react"]
    }

    job_skills = job_skills_map.get(job_role.lower(), [])

    matched = [skill for skill in job_skills if skill in resume_skills]
    missing = [skill for skill in job_skills if skill not in resume_skills]

    score = int((len(matched) / len(job_skills)) * 100) if job_skills else 0

    suggestions = []
    if missing:
        suggestions.append(f"Add missing skills: {', '.join(missing)}")
    if score < 70:
        suggestions.append("Improve project experience related to this role")
        suggestions.append("Add measurable achievements in resume")

    return {
        "score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "suggestions": suggestions
    }
