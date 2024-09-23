from speech_to_text import InterlocusWhisper
from response_generator import get_cohere_response
from text_to_speech import speak_text
import os

def run_voice_assistant():
    while True:
        assistant = InterlocusWhisper()
        transcription = assistant.listen_and_transcribe(duration=5)  # duration can be adjusted

        if "stop" in transcription.lower():
            print("SYSTEM: Goodbye!")
            break  
        else:
            print(f"JARVIS: You said: {transcription}")
        
        if "stop" in transcription.lower():
            print("SYSTEM: Goodbye!")
            break
        
        # Get response from Cohere
        response = get_cohere_response(transcription)
        
        # Speak the response
        speak_text(response)

if __name__ == "__main__":
    run_voice_assistant()




    # Continuously listen and transcribe until the user says "stop"
    