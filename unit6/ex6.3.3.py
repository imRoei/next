from gtts import gTTS
import os
import pyttsx3


# def text_to_speech(text):
#     # Initialize gTTS with the text to convert
#     speech = gTTS(text)

#     # Save the audio file to a temporary file
#     speech_file = 'speech.mp3'
#     speech.save(speech_file)

#     # Play the audio file
#     os.system(speech_file)

def main():

    engine = pyttsx3.init()
    engine.say("first time i'm using a package in next.py course")
    engine.runAndWait()
    #text_to_speech("first time i'm using a package in next.py course")

if __name__ == '__main__':
    main()