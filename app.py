import streamlit as st
#from resume_parser import load_resume_data
#from job_scraper import scrape_job_description
#from cover_letter_generator import generate_cover_letter
#from pdf_exporter import save_cover_letter_as_pdf

st.title("AI Cover Letter Generator 🤖")

# Upload Resume JSON
st.subheader("Upload Your Resume")
resume_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

# Input Job URL
st.subheader("Enter Job URL")
job_url = st.text_input("Paste the job posting URL (e.g., LinkedIn, Indeed)")

if resume_file and job_url:
    resume_data = resume_file.read().decode("utf-8")


# calls scrape_job_description function
#job_description = scrape_job_description(job_url)

# calls generate_cover_letter function
#cover_letter = generate_cover_letter(resume_data, job_description)

