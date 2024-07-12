from bs4 import BeautifulSoup
import requests
import pyttsx3
import speech_recognition
import datetime


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query




def temp():
    speak("location please: ")
    cm = takeCommand().lower()
    search=f"temperature in {cm}"
    url=(f"https://www.google.com/search?q= {search}")
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temp=data.find("div",class_="BNeawe").text
    speak(f"current {search} is {temp} : ")
    print(f"current{search} is {temp} : ")

def weather():
    speak("location please: ")
    city= takeCommand().lower()

    if city:
        search=f"weather in {city}"
        url=(f"https://www.google.com/search?q= {search}")
        r=requests.get(url)
        data=BeautifulSoup(r.text,"html.parser")
        temp=data.find("div",class_="BNeawe").text
        speak(f"current{search} is {temp} : ")
        print(f"current{search} is {temp} : ")

def time():
    Time=datetime.datetime.now().strftime("%H:%M")
    speak(f"Sir,the time is{Time}")