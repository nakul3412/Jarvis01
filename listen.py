import speech_recognition as sr
import colorama
from colorama import Fore, Back, Style
colorama.init()




def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(Fore.GREEN +"Listening ....")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source,0.5)
    try:
        print(Fore.RED+"Recognizing....")
        query = r.recognize_google(audio,language='en-in').lower()
        print(Fore.BLACK + f"User -> {query}\n")
    except Exception as e:
        return ''
    query = str(query)
    return query



