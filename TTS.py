from pathlib import Path
from openai import OpenAI

# open connection to
client = OpenAI(api_key = "<SECRET-API-KEY>")

# read video transcript
with open("transcript.txt") as f:
    transcript = f.readlines()

print(transcript)

# read the transcript once in every available language
for voice in ["alloy","echo","fable","onyx","nova","shimmer"]:
  filename = "speech-" + voice + ".mp3"
  speech_file_path = Path(__file__).parent / "speech" / filename
  response = client.audio.speech.create(
    model = "tts-1",
    voice = voice,
    input = "".join(transcript)
  )
  response.stream_to_file(speech_file_path)
