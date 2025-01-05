import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import tkinter as tk 
from tkinter import Entry, Button, Label, Radiobutton, StringVar

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello, my name is PAA, how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User-said: {query}\n")
        update_input(query)  
        return query 
    except Exception as e:
        print("Tell something valid")
        update_input("None")
        return "None"

def update_output(output_text):
    output_label.config(text=output_text)

def update_input(input_text):
    input_label.config(text=f"User-said: {input_text}")

def execute_command():
    if audio_input_mode:
        user_input = takeCommand().lower()  # Use the recognized audio input
    else:
        user_input = entry.get().lower()  

    if user_input:
        if 'wikipedia' in user_input:
            speak('Searching Wikipedia...')
            query = user_input.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            update_output(results)
        elif 'open youtube' in user_input:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in user_input:
            webbrowser.open("https://www.google.com")
        elif 'open stackoverflow' in user_input:
            webbrowser.open("https://www.stackoverflow.com")
        elif 'time' in user_input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"The time is {strTime}")
            update_output(f"The time is {strTime}")
        elif 'weather' in user_input:
            webbrowser.open("https://www.accuweather.com")
        elif 'spotify' in user_input or 'play music' in user_input:
            # Call your Spotify function here (e.g., run("spotify"))
            pass
        elif 'calculator' in user_input:
            # Call your calculator function here
            pass
        elif 'camera' in user_input or 'take photo' in user_input:
            # Call your camera function here
            pass
        elif 'what all' in user_input:
            speak('I can tell you results from Wikipedia, open a few important apps and websites')
            update_output('I can tell you results from Wikipedia, open a few important apps and websites')
    else:
        speak("Please enter a valid command.")

def toggle_input_mode():
    global audio_input_mode
    audio_input_mode = input_mode_var.get()
    if audio_input_mode:
        entry.config(state=tk.DISABLED)
    else:
        entry.config(state=tk.NORMAL)

app = tk.Tk()
app.title("Voice Assistant")

entry = Entry(app, width=40)
entry.pack()

button = Button(app, text="Execute", command=execute_command)
button.pack()

input_label = Label(app, text="", wraplength=400)
input_label.pack()

output_label = Label(app, text="", wraplength=400)
output_label.pack()

input_mode_var = StringVar()
input_mode_var.set("Text Input")
input_mode_radiobutton = Radiobutton(app, text="Text Input", variable=input_mode_var, value="Text Input", command=toggle_input_mode)
input_mode_radiobutton.pack()
input_mode_radiobutton = Radiobutton(app, text="Audio Input", variable=input_mode_var, value="Audio Input", command=toggle_input_mode)
input_mode_radiobutton.pack()

audio_input_mode = False

wishMe()

app.mainloop()
