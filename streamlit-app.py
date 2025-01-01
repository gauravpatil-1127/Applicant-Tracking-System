import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
load_dotenv()  #load all the evironment variable

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Gemini Pro Response

def get_gemini_response(input):
    model = genai.GenerativeModel(model_name='gemini-pro')
    response = model.generate_content(input)
    return response.text


def input_pdf_txt(uploaded_file):
    # Initialize an empty string for the extracted text
    text = ""
    
    # Create a PdfReader object
    reader = pdf.PdfReader(uploaded_file)
    
    # Iterate over all pages in the PDF
    for page in reader.pages:
        # Extract and append the text from each page
        text += page.extract_text() or ""  # Handle cases where extract_text returns None
    
    return text



## streamlit app
st.title("Application Tracking System")
st.text("Improve your resume using this tool")
job_description = st.text_area("Paste the Job Description Here")
upload_file = st.file_uploader("upload your resume",type="pdf",help="Please upload the pdf only")


submit = st.button("Submit")

if submit:
    if upload_file is not None:
        text = input_pdf_txt(uploaded_file=upload_file)
        #Prompt Template
        input_prompt =f'''
        I have a job description and a candidate's resume. I need the model to provide the following outputs:

        Percentage Match: Calculate the percentage match between the job description and the candidate's resume.
        Profile Summary: Summarize how well the candidate's resume aligns with the job description, highlighting key strengths or areas of alignment.
        Missing Keywords: Identify keywords or key skills from the job description that are not present in the candidate's resume and suggest them for inclusion.
        Job Description: {job_description}

        Candidate Resume: {text}

        Please provide the results as follows:

        Percentage Match: [Calculated match percentage]
        Profile Summary: [Summary of match]
        Missing Keywords: [List of missing keywords]

        Do not hallicunate with anything else also don't generate any random response you need to compare job description and candidate resume text if you are not getting any text please say "provide text"

        '''
        response = get_gemini_response(input_prompt)
        st.subheader(response)
