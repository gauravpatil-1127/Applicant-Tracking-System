from pdf_parser import pdf_parser
from groq_env import client
from system_prompt import prompt
from IPython.display import Markdown, display
import streamlit as st
from io import StringIO
from langchain_community.document_loaders import PyMuPDFLoader

file_path = r"C:\Users\Admin\Downloads\Gaurav_Patil_AI.pdf"

# input_text = pdf_parser(file_path)
# jd = """
# OB DESCRIPTION 

# Job Summary:

# As a Data Scientist at Emerson, you will be responsible for analyzing complex data sets to identify trends, develop predictive models, and provide actionable insights. You will work closely with cross-functional teams to understand business needs and deliver data-driven solutions that enhance decision-making and drive business growth.

# In this Role, Your Responsibilities Will Be:

# Analyze large, complex data sets using statistical methods and machine learning techniques to extract significant insights.
# Develop and implement predictive models and algorithms to solve business problems and improve processes.
# Create visualizations and dashboards to effectively communicate findings and insights to team members.
# Work with data engineers, product managers, and other team members to understand business requirements and deliver solutions.
# Clean and preprocess data to ensure accuracy and completeness for analysis.
# Prepare and present reports on data analysis, model performance, and key performance indicators to customers and management.
# Participate in regular Scrum events such as Sprint Planning, Sprint Review, and Sprint Retrospective
# Stay updated with the latest industry trends and advancements in data science and machine learning techniques 

# Who You Are:

# You quickly and conclusively act in constantly evolving, unexpected situations. You adjust communication content and style to meet the needs of diverse partners. You always keep the end in sight; puts in extra effort to meet deadlines. You analyze multiple and diverse sources of information to define problems accurately before moving to solutions. You observe situational and group dynamics and select best-fit approach.

# For This Role, You Will Need:

# Minimum of 5-7 years of industry experience
# More than 3 years proven experience in a data science or analytics role, with a proven track record of building and deploying models.
# Excellent understanding of machine learning techniques and algorithms, such as GPTs, CNN, RNN, k-NN, Naive Bayes, SVM, Decision Forests, etc.
# Experience with NLP, NLG, and Large Language Models like – BERT, LLaMa, LaMDA, GPT, BLOOM, PaLM, DALL-E, etc.
# Proficiency in programming languages such as Python or R, and experience with data manipulation libraries (e.g., pandas, NumPy).
# Experience with machine learning frameworks and libraries such as Go, TensorFlow, PyTorch
# Familiarity with data visualization tools (e.g., Tableau, Power BI, Matplotlib, Seaborn).
# Experience with SQL and NoSQL databases such as MongoDB, Cassandra, Vector databases 

# Preferred Qualifications that Set You Apart:

# Bachelor’s degree in computer science, Data Science, Statistics, or a related field or a master's degree or equivalent experience or higher is preferred.
# Strong analytical and problem-solving skills, with the ability to work with complex data sets and extract actionable insights.
# Excellent verbal and written communication skills, with the ability to present complex technical information to non-technical collaborators. 

# Our Offer To You:

# By joining Emerson, you will be given the opportunity to make a difference through the work you do.

# Emerson's compensation and benefits programs are designed to be driven within the industry and local labor markets. We also offer a comprehensive medical and insurance coverage to meet the needs of our employees.

# We are committed to creating a global workplace that supports diversity, equity and accepts inclusion. We welcome foreign nationals to join us through our Work Authorization Sponsorship.

# We attract, develop, and retain exceptional people in an inclusive environment, where all employees can reach their greatest potential. We are dedicated to the ongoing development of our employees because we know that it is critical to our success as a global company.

# We have established our Remote Work Policy steadfast for eligible roles to promote Work-Life Balance through a hybrid work set up where our team members can take advantage of working both from home and at the office.

# Safety is paramount to us, and we are steadfast in our pursuit to provide a Safe Working Environment across our global network and facilities.

# Through our benefits, development opportunities, and an inclusive and safe work environment, we aim to create an organization our people are proud to represent.

# Our Commitment to Diversity, Equity & Inclusion

# At Emerson, we are committed to fostering a culture where every employee is valued and respected for their unique experiences and perspectives. We believe a diverse and inclusive work environment gives to the rich exchange of ideas and diversity of thoughts, that inspires innovation and brings the best solutions to our customers.

# This philosophy is fundamental to living our company’s values and our responsibility to leave the world in a better place. Learn more about our Culture & Values and about Diversity, Equity & Inclusion at Emerson .

# If you have a disability and are having difficulty accessing or using this website to apply for a position, please contact: idisability.administrator@emerson.com .

# WHY EMERSON

# Our Commitment to Our People

# At Emerson, we are motivated by a spirit of collaboration that helps our diverse, multicultural teams across the world drive innovation that makes the world healthier, safer, smarter, and more sustainable. And we want you to join us in our bold aspiration.

# We have built an engaged community of inquisitive, dedicated people who thrive knowing they are welcomed, trusted, celebrated, and empowered to tackle the world’s most complex problems for our customers, our communities, and the planet. You’ll give to this vital work while further developing your skills through our award-winning employee development programs. We are a proud corporate citizen in every city where we operate and are committed to our people, our communities, and the world at large. We take this responsibility seriously and strive to make a positive impact through every endeavor.

# At Emerson, you’ll see firsthand that our people are at the center of everything we do. So, let’s go. Let’s think differently. Learn, collaborate, and grow. Seek opportunity. Push boundaries. Be empowered to make things better. Speed up to break through. Let’s go, together.

# ABOUT EMERSON

# Emerson is a global leader in automation technology and software. Through our deep domain expertise and legacy of magnificent execution, Emerson helps customers in critical industries like life sciences, energy, power and renewables, chemical and sophisticated factory automation operate more sustainably while improving productivity, energy security and reliability.

# With global operations and a comprehensive portfolio of software and technology, we are helping companies implement digital transformation to measurably improve their operations, conserve valuable resources and enhance their safety.

# We offer equitable opportunities, celebrate diversity, and embrace challenges with confidence that, together, we can make an impact across a broad spectrum of countries and industries. Whether you’re an established professional looking for a career change, an undergraduate student exploring possibilities, or a recent graduate with an advanced degree or equivalent experience, you’ll find your chance to make a difference with Emerson. Join our team – let’s go!

#  ABOUT US 

# WHY EMERSON

# Our Commitment to Our People

# At Emerson, we are motivated by a spirit of collaboration that helps our diverse, multicultural teams across the world drive innovation that makes the world healthier, safer, smarter, and more sustainable. And we want you to join us in our bold aspiration.

# We have built an engaged community of inquisitive, dedicated people who thrive knowing they are welcomed, trusted, celebrated, and empowered to solve the world’s most complex problems — for our customers, our communities, and the planet. You’ll contribute to this vital work while further developing your skills through our award-winning employee development programs. We are a proud corporate citizen in every city where we operate and are committed to our people, our communities, and the world at large. We take this responsibility seriously and strive to make a positive impact through every endeavor.

# At Emerson, you’ll see firsthand that our people are at the center of everything we do. So, let’s go. Let’s think differently. Learn, collaborate, and grow. Seek opportunity. Push boundaries. Be empowered to make things better. Speed up to break through. Let’s go, together.

# Accessibility Assistance or Accommodation

# If you have a disability and are having difficulty accessing or using this website to apply for a position, please contact: idisability.administrator@emerson.com .

# ABOUT EMERSON

# Emerson is a global leader in automation technology and software. Through our deep domain expertise and legacy of flawless execution, Emerson helps customers in critical industries like life sciences, energy, power and renewables, chemical and advanced factory automation operate more sustainably while improving productivity, energy security and reliability.

# With global operations and a comprehensive portfolio of software and technology, we are helping companies implement digital transformation to measurably improve their operations, conserve valuable resources and enhance their safety.

# We offer equitable opportunities, celebrate diversity, and embrace challenges with confidence that, together, we can make an impact across a broad spectrum of countries and industries. Whether you’re an established professional looking for a career change, an undergraduate student exploring possibilities, or a recent graduate with an advanced degree, you’ll find your chance to make a difference with Emerson. Join our team – let’s go!

# No calls or agencies please.
# """

def invoke_llama(input_text,jd):
    chat_completion = client.chat.completions.create(
        messages=[ prompt,
                
            {   "role": "user",
                "content": input_text
            },
            {   "role": "user",
                "content": jd
            
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    response = chat_completion.choices[0].message.content
    return response

## streamlit app
st.set_page_config(layout="wide")
st.title("Applicant Tracking System")
st.text("Improve Your Resume ATS")


col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Job Description Area")
    jd=st.text_area("Paste the Job Description",height=500)
with col2:
    st.subheader("upload your resume")
    uploaded_file=st.file_uploader("Upload Your Resume",type=["pdf"],help="Please uplaod the pdf")
    submit = st.button("Submit")
    if submit:
        if uploaded_file is not None:
        # Save the file temporarily to work with PyMuPDFLoader
            with open("temp_uploaded_file.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Use PyMuPDFLoader to extract text
            loader = PyMuPDFLoader("temp_uploaded_file.pdf")
            documents = loader.load()
            
            # Combine all pages into a single text output
            extracted_text = "\n\n".join([doc.page_content for doc in documents])
            # Display extracted text
            st.write("Your Parsed Resume Text")
            st.text_area("Extracted Text:", extracted_text,height=300)
            with col3:
                st.subheader("Response from LLM")
                response=invoke_llama(input_text=extracted_text,jd=jd)
                st.markdown(response)
        else:
            st.warning("Please upload a PDF file.")


    # input_text=pdf_parser(uploaded_file)
    
    # Display extracted text
    # st.text_area("Extracted Text:", extracted_text)

    

# if submit:
#     if uploaded_file is not None:
#         st.write("file uploaded")
#         input_text=pdf_parser(uploaded_file)
#         response=invoke_llama(input_text,jd)
#         st.subheader(response)
        


# print(response)
# display(Markdown(response))