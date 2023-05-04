import datetime
import pyttsx3
from speak import Command
from requests_html import HTMLSession
import random
import requests
import colorama
from colorama import Fore, Back, Style
colorama.init()

s = HTMLSession()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',200)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()





class Non_INPUT:
    def __init__(self):
        self.date = Date()
    def non_input(self,reply):
        if(reply == 'date'):
            self.date.dates()







class INPUT:
    def __init__(self):
        self.whea = Wheather()
        self.passw = PassWord()
    def input(self,reply):
        if(reply == 'wheather'):
            self.whea.wheather()
        elif(reply == 'password'):
            self.passw.extends()








class Date:
    def __init__(self):
        pass
    def dates(self):
        date = datetime.date.today()
        speak(date)



"""Get Wheather Detail"""




class Wheather:
    def __init__(self):
        self.command = Command()
    def wheather(self):
        google_search = 'https://www.google.com/search?q=weather in '
        speak("sir tell me  the location")
        location = self.command.takecommand()
        hole_id = google_search+location
        r = s.get(hole_id)


        temperature = (r.html.find('span#wob_tm',first=True).text)
        humidity = (r.html.find('span#wob_hm',first=True).text)
        wind = (r.html.find('span#wob_ws',first=True).text)
        precipation = (r.html.find('span#wob_pp',first=True).text)
        weather = (r.html.find('span#wob_dc',first=True).text)



        print(f'Temperature in {location} is {temperature} Degree Celicus')
        speak(f'Temperature in {location} is {temperature} Degree Celicus')
        print(f'weather is {weather}')
        speak(f'weather is {weather}')
        print(f'precipitation is {precipation}')
        speak(f'precipitation is {precipation}')
        print(f'humidity is {humidity}')
        speak(f'humidity is {humidity}')
        print(f'wind is {wind}')
        speak(f'wind is {wind}')




"""Create Password"""



class PassWord:
    def __init__(self):
        self.Upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.Lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.Special = ['!','@','#','$','%','^','&','*']
        self.digit = ['1','2','3','4','5','6','7','8','9']
      
    def extends(self):
        self.Upper.extend(self.Lower+self.Special)
        random.shuffle(self.Upper)
        speak("sir enter the lenght of password")
        len = int(input("enter lenght"))
        password = self.Upper[:len]
        d = ''.join(password)
        print(d)
        
        with open('password.txt','a') as f:
            f.write(f'\n\nPassword :{d}')
        return True
    







""" Daily News  """







class Daily_News():
    def __init__(self):
        self.API_KEY = '9e7243fdaa284a5facbf1f5652261393'
        self.date = (datetime.datetime.now().strftime('%y-%m-%d'))
        self.take_article_title
    def taking_url(self):
        url = (f'https://newsapi.org/v2/top-headlines?country=in&from={self.date}&sortBy=popularity&apiKey={self.API_KEY}')
        response = requests.get(url)
        d = (response.json())
        self.take_article_title(d)
    def take_article_title(self,d):
        for i in range(1,20):
            print(Fore.RED +f'{i+1}) ',d['articles'][i]['title'])
            print(Fore.GREEN +'  ',  d['articles'][i]['description'],'\n\n\n')
            

