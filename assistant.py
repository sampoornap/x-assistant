import cohere
import os
from dotenv import load_dotenv
from time_date_module import get_system_time, get_system_date
from conversation_tracker import ConversationHistory
import pywhatkit as kit

load_dotenv()

COHERE_API_KEY = os.getenv('COHERE_API_KEY')

class Assistant:
    def __init__(self):
        self.history_tracker = ConversationHistory()
        self.cohere_client = cohere.Client(COHERE_API_KEY)

    def handle_prompt(self, prompt):
        if self.is_play_command(prompt):
            return self.handle_play_command(prompt)
        elif self.is_system_time_query(prompt):
            return self.get_time_response()
        elif self.is_system_date_query(prompt):
            return self.get_date_response()
        else:
            return self.get_llm_response(prompt)
    
    def is_system_time_query(self, prompt):
        time_phrases = ["current time", "time is it", "what time", "now", "system time", "what is the time now"]
        return any(phrase in prompt.lower() for phrase in time_phrases)
    
    def is_system_date_query(self, prompt):
        date_phrases = ["today's date", "what date is it", "current date", "system date"]
        return any(phrase in prompt.lower() for phrase in date_phrases)

    def get_time_response(self):
        system_time = get_system_time()
        response = f"The current time is {system_time}."
        print(f"SYSTEM: {response}")
        return response
    
    def get_date_response(self):
        system_date = get_system_date()
        response = f"Today's date is {system_date}."
        print(f"SYSTEM: {response}")
        return response
    
    def is_play_command(self, prompt):
        return prompt.lower().strip().startswith("play ")

    def handle_play_command(self, prompt):
        search_query = prompt.lower().replace("play ", "")
        print(f"SYSTEM: Playing '{search_query}' on YouTube...")
        kit.playonyt(search_query)
        return f"Playing '{search_query}' on YouTube."
    
    def get_llm_response(self, prompt):
    
        # co = cohere.Client(COHERE_API_KEY)
        conversation_history = self.history_tracker.get_conversation_history()

        modified_prompt = f"{conversation_history} User: Answer this in short and precisely in 1-2 sentences {prompt}"
        # print(f"SYSTEM: Sending prompt to Cohere: {prompt}")
        response = self.cohere_client.generate(prompt = modified_prompt)
        
        text_response = response.generations[0].text.strip()
        # print(f"SYSTEM: Response from Cohere: {text_response}")
        self.history_tracker.add_interaction(prompt, text_response)
        return text_response

