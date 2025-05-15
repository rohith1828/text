from gtts import gTTS
import os

telugu_text = "హలో! ఇది తెలుగు వాయిస్ ఉదాహరణ."
tts = gTTS(text=telugu_text, lang='te')
tts.save("telugu_output.mp3")
os.system("start telugu_output.mp3") 