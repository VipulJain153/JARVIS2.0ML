import speech_recognition as sr,pyttsx3
def TakeCommand():
    try:
        r = sr.Recognizer()
        r.pause_threshold = 0.6
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic)
            return r.recognize_google(r.listen(mic)).lower()
    except Exception as e:print(e);return 'error@44324324'
def speak(word):
    engine = pyttsx3.init()
    engine.setProperty('rate',146)
    engine.setProperty('volume',100.0)
    engine.say(word)
    engine.runAndWait()