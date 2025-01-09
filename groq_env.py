from groq import Groq
import os
from system_prompt import prompt
from pdf_parser import pdf_parser

## load all our environment variables
from dotenv import load_dotenv
load_dotenv() 
key=os.getenv("GROQ_API_KEY")
# api_key


client = Groq(
    api_key="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",
)


