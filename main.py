import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer=sr.Recognizer()
engine=pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    pass    



if __name__ =="__main__":
    speak("initalizing jarvis...")
    while True:
        r=sr.Recognizer()
        print("recognising...")
        try:
            with sr.Microphone() as sourse:
                print("listining...")
                audio=r.listen(sourse,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("ya")
                with sr.Microphone() as sourse:
                    print("jarvis active...")
                    audio=r.listen(sourse,timeout=2,phrase_time_limit=1)
                    command=r.recognize_google(audio)
                    processCommand()
        except Exception as e:
            print("Error; {0}".format(e))            
