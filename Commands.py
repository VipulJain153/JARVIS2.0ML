from AI import chat,ai
import os,webbrowser,wikipedia,datetime,pygame
from nlp import speak

pygame.init()

with open('memory.txt', 'r+') as f:
    chatStr = f.read()

def Operator(query):
    global chatStr
    if 'open' in query:
            if 'google' in query:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            elif 'code' in query:
                os.system("code")
            elif 'pycharm' in query:
                os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.3\\bin\\pycharm64.exe")
            elif 'explorer' in query:
                os.system("explorer")
            elif 'youtube' in query:
                webbrowser.open('youtube.com')
            elif 'github' in query:
                webbrowser.open('github.com')
            elif 'stackoverflow' in query:
                webbrowser.open('stackoverflow.com')
            elif 'spotify' in query:
                webbrowser.open('open.spotify.com')
            elif 'chatgpt' in query:
                webbrowser.open('openai.com')
    elif 'wikipedia' in query:
            try:
                wiki = wikipedia.summary(query.replace('wikipedia', '').strip(),sentences=2)
                print('Jarvis: ',wiki)
                speak(wiki)
            except Exception as e:
                print("Jarvis: Not Found!")
                speak("Not Found!")
    elif 'time' in query:
            now = datetime.datetime.now().strftime("%H %S %p")
            print('Jarvis: ', now)
            speak(now)
    elif 'play music' in query:
            pygame.mixer.Sound('music.mp3').play()
    elif 'play background music' in query:
            bgmusic = pygame.mixer.Sound('music.mp3')
            bgmusic.play(loops=-1)
    elif 'stop music' in query:
            bgmusic.stop()
    elif 'search' in query:
            webbrowser.open(f"https://www.google.com/search?q={query.replace('search','').strip()}")
    elif 'watch' in query:
            webbrowser.open(f"https://www.youtube.com/results?search_query={query.replace('watch','').strip()}")
    elif 'using artificial intelligence' in query:
            ai(query.split('using artificial intelligence')[1])
            speak("Completed, Sir!")
    elif 'bye' in query or pygame.QUIT in [event.type for event in pygame.event.get()]:
            speak('Good Bye Sir.')
            with open("memory.txt","w") as f:
                f.write(chatStr)
            exit()
    elif 'reset chat' in query:
            chatStr = ""
    else:
            chatStr = chat(query,chatStr)