from datetime import date
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 - male 1 - female

activationWord = 'shmel'

def parseCommand():
    listener = sr.Recognizer()
    print('Слушаю')

    with sr.Microphone() as course:
        listener.pause_threshold = 2
