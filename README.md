# What is this program doing?

This code only serves the purpose to test OpenAIs new text-to-speech (TTS) model.

Based on the text in the file `transcript.txt`, the program will generate an MP3 file for [every available voice](https://platform.openai.com/docs/quickstart?context=python) and save these in the `speech` folder.

# How can I run the program?

Before running, the string `"<SECRET-API-KEY>"` needs to be replaced by your own OpenAI API key. After that, the script is ready to be run.

You can run the script directly from the console as follows.

```
python3 TTS.py
```

By default, the `alloy` voice will be used. However, you can set any number of other voices via command line arguments.

```
python3 TTS.py nova fable
```

Or, if you'd like to generate all possible voices at once, simply use the `all` argument.

```
python3 TTS.py all
```