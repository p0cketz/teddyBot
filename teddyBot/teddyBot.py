import requests, base64, os, time, re, translate, asyncio, pyaudio
import playsound
import tiktokvoice
import textgenstream
import os
from dotenv import load_dotenv
import time
import speech_recognition as sr
import pyttsx3
import numpy as np
from gtts import gTTS
import chunker
SESSION = "3f54de0e52fefe022d7dc78a1bf36465"
tempfile = "temp.mp3"


mytext = 'Welcome to me'
language = 'en'
load_dotenv()
# Set up the speech recognition and text-to-speech engines
r = sr.Recognizer()



#Im removing the engine here

#engine = pyttsx3.init()
#voices = engine.getProperty('voices')[1]
#engine.setProperty('voice', voices.id)
#engine.setProperty('rate', 150)
name = "Morgan"
greetings = [f"Whats up miss {name}",
            "Can I help you dear?",
            "Well, hello there, booger butt?",
            "What can I do for you?",
            f"Ahoy there, Captain {name}! How's the ship sailing?",
            "HI",
            "what can I do for you?",
            "Can I help you?" ]
tiktokvoice.tts(SESSION, "en_female_emotional", np.random.choice(greetings), "temp.mp3", True)
# Listen for the wake word "hey pos"
def listen_for_wake_word(source):
    print("Listening for 'Hey'...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if "hey" or "hello" or "hi" or "cupcake" in text.lower():
                print("Wake word detected.")
                tiktokvoice.tts(SESSION, "en_female_emotional", np.random.choice(greetings), "temp.mp3", True)
                listen_and_respond(source)
                break
        except sr.UnknownValueError:
            pass
# Listen for input and respond with OpenAI API
def listen_and_respond(source):
    print("Listening...")

    while True:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if not text:
                continue

            # Send input to OpenAI API
            pattern = r'[^a-zA-Z0-9\s.]'

            #RIGHT HERE SHIKKY!
            #--------------------------------------------
            textgenstream.print_response_stream(text)
            #--------------------------------------------
            #response = re.sub(pattern, "", response)
            #if response == "":
                #response = "Thats really nice."

            #This should work right out of the box

            #response_text = response.replace('\'', "")
            #response_text = response_text.replace('\"', "")
            #response_text = response_text.replace('\n', " ")
            #response_text = response_text.replace('/n', " ")
            #response_text = response_text.replace(',', ".")
            #response_text = response_text.replace('!', ".")
            # Speak the response
            print("speaking")
            #chunker.chunkerton(response)

            if not audio:
                listen_for_wake_word(source)
        except sr.UnknownValueError:
            time.sleep(0.5)
            print("Silence found, shutting up, listening...")
            listen_for_wake_word(source)
            break

        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            listen_for_wake_word(source)
            break

# Use the default microphone as the audio source
with sr.Microphone() as source:
    listen_for_wake_word(source)









#Fix the responses from teddybot.