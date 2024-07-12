import webbrowser
import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Function to play random songs from a Spotify playlist
def play_random_song():
    playlist_link = "your spotify playlist" # Replace with your playlist link
    webbrowser.open(playlist_link)

# Example usage:
play_random_song()
