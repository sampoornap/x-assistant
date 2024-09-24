import whisper
import os
import pyaudio
import wave
import time
from tempfile import NamedTemporaryFile

model = whisper.load_model("base")


class InterlocusWhisper:
    def __init__(self):
        # PyAudio settings
        self.chunk = 1024  # Record in chunks of 1024 samples
        self.sample_format = pyaudio.paInt16  # 16 bits per sample
        self.channels = 1  # Mono
        self.rate = 16000  # Record at 16000 samples per second
        self.p = pyaudio.PyAudio()

    def record_audio(self, duration=5):
        """Record audio from the microphone for the specified duration."""
        print("SYSTEM: Recording...")

        # For open a stream to the microphone
        stream = self.p.open(format=self.sample_format,
                             channels=self.channels,
                             rate=self.rate,
                             frames_per_buffer=self.chunk,
                             input=True)
        frames = []

        # Record for the given duration (in seconds)
        for _ in range(0, int(self.rate / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()

        print("SYSTEM: Recording finished.")

        # Saving the recorded audio to a temporary file
        with NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
            wf = wave.open(temp_wav_file.name, 'wb')
            wf.setnchannels(self.channels)
            wf.setsampwidth(self.p.get_sample_size(self.sample_format))
            wf.setframerate(self.rate)
            wf.writeframes(b''.join(frames))
            wf.close()

            return temp_wav_file.name

    def transcribe_audio(self, audio_file):
        """Use Whisper model to transcribe recorded audio."""
        print("SYSTEM: Transcribing audio...")
        result = model.transcribe(audio_file)
        print(f"YOU: {result['text']}")
        return result['text']

    def listen_and_transcribe(self, duration=5):
        """Record and transcribe the user's voice."""
        audio_file = self.record_audio(duration)
        transcription = self.transcribe_audio(audio_file)
        os.remove(audio_file)  
        return transcription


# Main function to test the assistant
# if __name__ == "__main__":
#     assistant = InterlocusWhisper()

#     # Continuously listen and transcribe until the user says "stop"
#     while True:
#         transcription = assistant.listen_and_transcribe(duration=5)  # duration can be adjusted

#         if "stop" in transcription.lower():
#             print("SYSTEM: Goodbye!")
#             break  
#         else:
#             print(f"JARVIS: You said: {transcription}")
