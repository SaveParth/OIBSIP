import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
recognizer = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        print("Sorry, I couldn't request results. Please check your internet connection.")
        return ""

    return command

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {current_time}")
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {current_date}")
    elif "search" in command:
        speak("What do you want to search for?")
        search_query = listen()
        if search_query:
            search_url = "https://www.google.com/search?q=" + search_query.replace(" ", "+")
            webbrowser.open(search_url)
            speak(f"Here are the search results for {search_query}")
    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't catch that. Can you repeat?")
speak("Hello! How can I help you today?")
while True:
    command = listen()
    if command:
        process_command(command)
