from gtts import gTTS
import os

def generate_audio(texts):
    for i, text in enumerate(texts):
        tts = gTTS(text)
        tts.save("./audio/audio"+str(i)+".mp3")
        

#texts = ["Hello how are you i am very much fine love you", "The same goes for you", "Text 3"]
#generate_audio(texts)
