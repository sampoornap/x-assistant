import cohere
import os
from dotenv import load_dotenv
from time_date_module import get_system_time, get_system_date

load_dotenv()

COHERE_API_KEY = os.getenv('COHERE_API_KEY')

class Assistant:
    def __init__(self):
        self.cohere_client = cohere.Client(COHERE_API_KEY)

    def handle_prompt(self, prompt):
        """Determine if prompt is a system query or needs to be sent to the LLM."""
        if self.is_system_time_query(prompt):
            return self.get_time_response()
        elif self.is_system_date_query(prompt):
            return self.get_date_response()
        else:
            return self.get_llm_response(prompt)
    
    def is_system_time_query(self, prompt):
        """Check if the prompt is asking for the current system time."""
        time_phrases = ["current time", "time is it", "what time", "now", "system time", "what is the time now"]
        return any(phrase in prompt.lower() for phrase in time_phrases)
    
    def is_system_date_query(self, prompt):
        """Check if the prompt is asking for the current system date."""
        date_phrases = ["today's date", "what date is it", "current date", "system date"]
        return any(phrase in prompt.lower() for phrase in date_phrases)

    def get_time_response(self):
        """Handle system time-related queries."""
        system_time = get_system_time()
        response = f"The current time is {system_time}."
        print(f"SYSTEM: {response}")
        return response
    
    def get_date_response(self):
        """Handle system date-related queries."""
        system_date = get_system_date()
        response = f"Today's date is {system_date}."
        print(f"SYSTEM: {response}")
        return response

    # def get_llm_response(self, prompt):
    #     """Send the prompt to Cohere LLM and return the response."""
    #     # Adding explicit instruction for a short response
    #     short_prompt = f"Answer this question in 1-2 sentences: {prompt}"
    #     print(f"SYSTEM: Sending prompt to Cohere: {short_prompt}")
        
    #     response = self.cohere_client.generate(
    #         model='command-xlarge-nightly',
    #         prompt=short_prompt,
    #         max_tokens=50,
    #         temperature=0.7
    #     )
        
    #     text_response = response.generations[0].text.strip()
    #     print(f"SYSTEM: Response from Cohere: {text_response}")
    #     return text_response
    
    def get_llm_response(self, prompt):
    
        co = cohere.Client(COHERE_API_KEY)
        modified_prompt = f"Answer this in short and precisely in 1-2 sentences {prompt}"
        print(f"SYSTEM: Sending prompt to Cohere: {prompt}")
        response = co.generate(prompt = modified_prompt)
        
        text_response = response.generations[0].text.strip()
        print(f"SYSTEM: Response from Cohere: {text_response}")
        return text_response

