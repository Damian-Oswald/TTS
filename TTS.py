from pathlib import Path
from openai import OpenAI
import sys

# read terminal arguments
arguments = sys.argv[1:len(sys.argv)]

# define which arguments are valid
valid = ["alloy","echo","fable","onyx","nova","shimmer"]

# check which voices are valid and define a voice list
voices = [i for i in arguments if i in valid]
if(len(voices)==0):
  voices = "alloy"
if("all" in arguments):
  voices = ["alloy","echo","fable","onyx","nova","shimmer"]

# open connection to
client = OpenAI(api_key = "<SECRET-API-KEY>")

# read video transcript
with open("transcript.txt") as f:
    transcript = f.readlines()

# read the transcript once in every available language
for voice in voices:
  filename = "speech-" + voice + ".mp3"
  speech_file_path = Path(__file__).parent / "speech" / filename
  response = client.audio.speech.create(
    model = "tts-1",
    voice = voice,
    input = "".join(transcript)
  )
  response.stream_to_file(speech_file_path)
