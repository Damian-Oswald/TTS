This code only serves the purpose to test OpenAIs new text-to-speech (TTS) model. Before running, the string `"<SECRET-API-KEY>"` needs to be replaced by your own OpenAI API key. After that, the script is ready to be run.

Based on the text in the file `transcript.txt`, the program will generate an MP3 file for [every available voice](https://platform.openai.com/docs/quickstart?context=python) and save these in the "speech" folder.

You can run the script simply with:

```
python3 TTS.py
```