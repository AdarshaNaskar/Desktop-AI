import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello!Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello!Good Afternoon!")

    else:
        speak("Hello!Good Evening!")
    
    speak("I am Daskas. Sir, Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from user and returns srting output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"   
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        #Logic foe executive tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'hello' in query:
            speak("Hello Sir")

        elif 'what can you do' in query:
            speak(" ...I can do anything. Just ask")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            
        elif 'open python' in query:
            codePath = "C:\\Users\\Adarsha\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\idlelib\\idle.pyw"
            os.startfile(codePath)

        elif 'open vs code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        else:
            speak(" Thank you Sir. Good Bye...")
            break

        if __name__ == "__main__":
            continue
