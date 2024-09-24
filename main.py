from speech_to_text import InterlocusWhisper
from response_generator import get_cohere_response
from text_to_speech import speak_text
from assistant import Assistant
import os

def run_voice_assistant():
    while True:
        assistant_listen = InterlocusWhisper()
        transcription = assistant_listen.listen_and_transcribe(duration=5)  # duration can be adjusted

        if "stop" in transcription.lower():
            print("SYSTEM: Goodbye!")
            break  
            
        else:
            print(f"You said: {transcription}")
        
        if "stop" in transcription.lower():
            print("SYSTEM: Goodbye!")
            break
        
        assistant = Assistant()

        if len(transcription.strip()) == 0:
            response = "Hello! Feel free to ask me any question. I am here to help you."
        else:
            response = assistant.handle_prompt(transcription)
        
        speak_text(response)

if __name__ == "__main__":
    run_voice_assistant()




    
    