# whenever i will upload any resume then this func will help me out to fetch the data from pdf,so need this library fitz
import fitz 
import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv() 
# Load environment variables from .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Get the API key from environment variable
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY  # Set the API key as an environment variable for OpenAI
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

client = OpenAI(api_key=OPENAI_API_KEY)  # Initialize the OpenAI client

# apify_client = ApifyClient(os.getenv("APIFY_API_TOKEN"))  # Initialize the Apify client with the API token from environment variable




def extract_text_from_pdf(uploaded_file):
    # Open the PDF file
    document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    # Initialize an empty string to hold the extracted text
    extracted_text = ""
    
    # Iterate through each page in the PDF
    for page in document:
        # Extract text from the current page and append it to the extracted_text string
        extracted_text += page.get_text()
    return extracted_text


# this function is initialized for LLM for resume summary,gaps and missing areas,future roadmap and prep strategies obv job keywords
# i am using openai LLM
# sends the prompt to openai and get the response and return it to the caller function
def ask_openai(prompt,max_tokens=500):
  
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
       temperature=0.5,
       max_tokens=max_tokens
    )
    return response.choices[0].message.content





