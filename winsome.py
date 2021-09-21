import pyttsx3
import datetime
import wikipedia
import webbrowser # to open browser
import ssl
import certifi
import os # remove the audio files
import speech_recognition as sr #to recognize speech
import smtplib
import playsound # to play audio
import random
import subprocess
from PIL import Image
import pyautogui #for screensort
import bs4 as bs
import urllib.request
from gtts import gTTS #google text to speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Maam!")

    elif hour >= 12 and hour <18:
        speak("Good Afternoon Maam!")

    else:
        speak("Good Evening Maam!")
    
    speak("Winsome is waithing for your command Maam. Tell me, how may I help you?")
def takecommand():
    # it will take microphonic input from the user and then it will return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.phrase_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rajyashi0209@gmail.com','ayushiiit')
    server.sendmail('rajyashi0209@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
    # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverfolw' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            webbrowser.open("spotify.com")
        elif 'open pinterest' in query:
            webbrowser.open("pinterest.com")
        elif 'play music' in query:
            music_dir = 'D:\\Musicfav'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" Maam, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\Yashi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to Abhishek' in query:
            try:
                speak('What should I say?')
                content = takecommand()
                to = "abhishekjjp23012000@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry maam, I am not able to send this email")
        elif 'email to Zaid' in query:
            try:
                speak('What should I say?')
                content = takecommand()
                to = "mohammadzaidahmedkhan@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry maam, I am not able to send this email")
        elif 'email to Aarushi' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "rajshekhararushi@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry maam, I am not able to send this email")
        elif 'quit' in query:
            exit()#jjj
        






    

