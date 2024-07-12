# -------------------Importing all Modules-----------------------------------

import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser
from plyer import notification
from pygame import mixer  # playing sound
import speedtest

# -------------------- password protection-------------------------------------
for i in range(3):
    a = input("Enter Password to open DevinAI :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try Again")

# ------------------------Text to Speak-----------------------------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# --------------------------Speak to Text----------------------------------------
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


# -------------------Alarm------------------------------------------------------
def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


# ------------------Main Function-----------------------------------------------
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can me call anytime")
                    break

                # ------------Normal Conversations----------------------------------------------
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query or "how r u" in query:
                    speak("Perfect, sir")
                elif "thank you" in query or "thank" in query:
                    speak("you are welcome, sir")

                elif "alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("jarvis", "")
                    speak("You told me " + rememberMessage)
                    remember = open("Remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do you remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me to remember that" + remember.read())

                elif "screenshot" in query:
                    from Screenshot import screnshot

                    screnshot()

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
                    download_net = wifi.download() / 1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ", download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

                # -----------Keyboard Controls(mute,volumeup,volumedown,open any desktop app,etc)---

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup

                    speak("Turning volume up,sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown

                    speak("Turning volume down, sir")
                    volumedown()


                elif "open" in query:  # EASY METHOD
                    query = query.replace("open", "")
                    query = query.replace("devin", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")


                elif "click my photo" in query:
                    pyautogui.press("super")

                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                # ----playing random song while we are tried & jokes while you are bored--------------
                elif "tired" in query:
                    speak("Listen your Favourite song, sir")
                    from Tired_play_song import play_random_song

                    play_random_song()

                elif "joke" in query:
                    from Jokes import jokes

                    speak(jokes())



                # --------------Opening & Closing all apps,Webbrowser---------------------------------
                # elif "open" in query:
                #     from Dictapp import openappweb
                #     openappweb(query)

                elif "close" in query:
                    from Dictapp import closeappweb

                    closeappweb(query)

                # ---------------Searching anything on Google,Youtube,Wikipedia,send msg on whatsapp----

                elif "hey google" in query:
                    from SearchNow import search_google

                    search_google()

                elif "hey youtube" in query:
                    from SearchNow import yt_song

                    yt_song()

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia

                    searchWikipedia(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage

                    sendMessage()


                # --------------------------Latest News(API) -------------------------------------------
                elif "news" in query:
                    from NewsRead import latestnews

                    latestnews()

                # --------------------------Calculate Anything(API)---------------------------------------
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc

                    query = query.replace("calculate", "")
                    query = query.replace("jarvis", "")
                    Calc(query)

                # ----------------------IPL SCORE,Temperature,Wheather(web scraping)----------------------
                elif "ipl score" in query:
                    from plyer import notification  # pip install plyer
                    import requests  # pip install requests
                    from bs4 import BeautifulSoup  # pip install bs4

                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")

                    team1_elem = soup.find(class_="cb-ovr-flo cb-hmscg-tm-nm")
                    team2_elem = soup.find(class_="cb-ovr-flo cb-hmscg-tm-nm")
                    team1_score_elem = soup.find(class_="cb-ovr-flo")
                    team2_score_elem = soup.find_all(class_="cb-ovr-flo")

                    if team1_elem and team2_elem and team1_score_elem and team2_score_elem:
                        team1 = team1_elem.get_text()
                        team2 = team2_elem.get_text()
                        team1_score = team1_score_elem[8].get_text()
                        team2_score = team2_score_elem[10].get_text()

                        a = print(f"{team1} : {team1_score}")
                        b = print(f"{team2} : {team2_score}")

                        notification.notify(
                            title="IPL SCORE :- ",
                            message=f"{team1} : {team1_score}\n {team2} : {team2_score}",
                            timeout=15
                        )
                    else:
                        print("Could not retrieve IPL scores at the moment.")

                elif 'temperature' in query:
                    from Temperature_Weather_Time import temp

                    temp()

                elif 'weather' in query:
                    from Temperature_Weather_Time import weather

                    weather()

                elif 'time' in query:
                    from Temperature_Weather_Time import time

                    time()


                # -----------------------if you want to Change the Password--------------------------------
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                # --------------------Scheduling the Day---------------------------------------------------
                elif "schedule my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

                # -----------------Show my schedule------------------------------------------------------------
                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )

                # ------------------Chatgpt Integration(Huggingface)-------------------------------------------
                elif "devin" in query or "deven" in query or "david" in query or "devon" in query:
                    query = query.replace("gpt", "")
                    query = query.replace("search", "")
                    query = query.replace("chatgpt", "")
                    query = query.replace("deven", "")
                    query = query.replace("devin", "")
                    query = query.replace("david", "")
                    query = query.replace("devon", "")
                    from Chatgpt import chatBot

                    chatBot(query)

                # ------------------Google Translator----------------------------------------------------------
                elif "translate" in query:
                    from Translator import translategl

                    query = query.replace("jarvis", "")
                    query = query.replace("translate", "")
                    translategl()

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                # -------------------Exit from program--------------------------------------------------------
                elif "finally sleep" in query or "finally slip" in query:
                    speak("Going to sleep,sir Have a Good Day...! ")
                    exit()
