import streamlit as st
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

job_role = st.text_input("Enter Job Role (e.g. Data Scientist, Java Developer)")

if uploaded_file and job_role:
    with st.spinner("Analyzing Resume..."):
        result = analyze_resume(uploaded_file, job_role)

    st.subheader("📊 Analysis Result")

    st.write(f"**Score:** {result['score']} / 100")
    st.write(f"**Matched Skills:** {', '.join(result['matched_skills'])}")
    st.write(f"**Missing Skills:** {', '.join(result['missing_skills'])}")

    st.subheader("💡 Suggestions")
    for s in result['suggestions']:
        st.write(f"- {s}")
