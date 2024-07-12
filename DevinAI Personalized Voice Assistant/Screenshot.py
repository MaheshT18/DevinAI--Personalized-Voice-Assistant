import speech_recognition
import pyttsx3
import pyautogui
import time

#------------------------Text to Speak-----------------------------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#--------------------------Speak to Text----------------------------------------
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



def screnshot():
    speak("sir,please tell me the name for this screenshot file")
    name = takeCommand().lower()
    speak("please sir hold the screen for few seconds,i am taking screenshot")
    time.sleep(3)
    img = pyautogui.screenshot()
    img.save(f"{name}.png")
    speak("Done sir,the screenshot is saved in our main folder.Now i am ready for next command")