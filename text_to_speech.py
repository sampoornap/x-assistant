from elevenlabs import play
from elevenlabs.client import ElevenLabs
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
client = ElevenLabs(
  api_key=ELEVENLABS_API_KEY
)

def speak_text(text):

    print(f"SYSTEM: {text}")
    audio = client.generate(
        text=text,
        voice="Chris",
        model="eleven_turbo_v2"
    )
    play(audio)


