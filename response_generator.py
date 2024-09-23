import cohere
import os
from dotenv import load_dotenv

load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

def get_cohere_response(prompt):
    
    co = cohere.Client(COHERE_API_KEY)
    modified_prompt = f"Answer this in short and precisely in 1-2 sentences {prompt}"
    print(f"SYSTEM: Sending prompt to Cohere: {prompt}")
    response = co.generate(prompt = modified_prompt)
    
    text_response = response.generations[0].text.strip()
    print(f"SYSTEM: Response from Cohere: {text_response}")
    return text_response
