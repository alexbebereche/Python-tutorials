import pyttsx3


def speak(text):
    pyttsx3.speak(text)


name = input("What's ur name? ")
speak("Hello " + name + " , How are you today?")