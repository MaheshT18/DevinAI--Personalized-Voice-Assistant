import wikipedia
import pywhatkit as kit
import webbrowser
import speech_recognition
import pyttsx3



engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        # r.energy_threshold=300
        audio=r.listen(source,5,5)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"You Said:{query}")

    except Exception as e:
        speak("Say that Again please...")
        return "none"
    return query




def yt_song():
    speak("sir,which song should I play")
    cm = takecommand().lower()
    kit.playonyt(f"{cm}")


def search_google():
    speak("sir,what should I search on Google")
    cm = takecommand().lower()
    kit.search(f"{cm}")


import wikipedia

def searchWikipedia(query):
    try:
        if "wikipedia" in query:
            speak("Searching from Wikipedia....")
            query = query.replace("wikipedia", "")
            query = query.replace("search wikipedia", "")
            query = query.replace("jarvis", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia..")
            print(results)
            speak(results)
    except wikipedia.exceptions.DisambiguationError as e:
        # If the query is ambiguous, provide options
        options = e.options[:5]  # Limiting to first 5 options
        speak("Wikipedia found multiple results. Please specify:")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
            speak(f"{idx}. {option}")
    except wikipedia.exceptions.PageError as e:
        # If the page does not exist, notify the user
        speak(f"Sorry, Wikipedia does not have any information on {query}. Please try another query.")
    except Exception as e:
        # Handle any other unexpected errors
        speak("Sorry, I encountered an error while searching Wikipedia. Please try again later.")
        print(e)
