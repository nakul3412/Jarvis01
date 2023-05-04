import pyttsx3

import speech_recognition as sr
import colorama
from colorama import Fore, Back, Style
colorama.init()




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',200)



class Speaker():
    def __init__(self):
        pass
    def speak(audio):
        engine.say("A.I :",audio)
        engine.runAndWait()






class Command:
    def __init__(self):
        pass
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(Fore.GREEN +"Listening ....")
            r.pause_threshold = 1
            r.energy_threshold = 1000
            audio = r.listen(source)
        try:
            print(Fore.RED+"Recognizing....")
            query = r.recognize_google(audio,language='en-in').lower()
            print(Fore.BLACK + f"User -> {query}\n")
        except Exception as e:
            return ''
        query = str(query)
        return query



