import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Voice engine setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Male/Female voice select karne ke liye

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nSuno rha hoon (Listening)...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Samajh rha hoon (Recognizing)...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User ne kaha: {query}\n")
    except Exception as e:
        print("Kripya fir se boliye...")
        return "None"
    return query.lower()

def main():
    speak("Hello Divya, Oasis Infobyte Voice Assistant is ready. How can I help you today?")
    
    while True:
        query = take_command()

        if 'hello' in query:
            speak("Hello! Hope you are doing well.")
            
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            
        elif 'date' in query:
            strDate = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {strDate}")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak("Opening Google")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening Youtube")

        elif 'offline' in query or 'stop' in query:
            speak("Thank you for using me. Goodbye Divya!")
            break

if __name__ == "__main__":
    main()