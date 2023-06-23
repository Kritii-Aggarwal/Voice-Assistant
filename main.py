import random
import wmi, sys
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser, random
import os, pyautogui, time, wmi
#
# import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        res ="Say that again, please."    
        print("Say that again please...") 
        speak(res)
        return "None"
    return query

def writeit(content):
    pyautogui.write(content)

def pressit(content):
    content=content[7:]
    if "escape" in content:
        pyautogui.keyUp("esc")
        exit
    pyautogui.hotkey(content)

'''def searchit(content):
    f = wmi.WMI()
    flag = 0
    for process in f.Win32_Process():
        if "chrome.exe" == process.Name or "msedge.exe"==process.Name:
            webbrowser.open_new_tab(content)

    if flag == 0:
        webbrowser.open(content)
        print("Application is not Running")
    pass'''

'''def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()'''

def show_tab():
    pyautogui.keyDown("alt")
    pyautogui.keyDown("tab")

def hide_tab():
    pyautogui.keyUp("alt")
    pyautogui.keyUp("tab")

def hold(content):
    content=content[6:]
    if "escape" in content:
        pyautogui.keyUp("esc")
        exit
    pyautogui.keyDown(content)

def release(content):
    content=content[9:]
    if "escape" in content:
        pyautogui.keyUp("esc")
        exit
    pyautogui.keyUp(content)

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query or "open browser" in query or "open web browser" in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open code' in query or "vs code" in query or "visual code" in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open instagram' in query: 
            speak('opening insta gram...') 
            webbrowser.open_new('https://www.instagram.com/') 
        
        elif 'open whatsapp web' in query:
            speak('opening whatsapp...') 
            webbrowser.open_new('https://web.whatsapp.com/') 

        elif 'open github' in query: 
            speak('opening git hub...') 
            webbrowser.open_new('https://github.com/')
        
        elif 'open spotify' in query:
            speak('opening spotify enjoy your music..')
            webbrowser.open_new('https://open.spotify.com/')

        elif query in ['bye',"quit","leave"]:
            li=["Alright, have a nice day.","Okay, i hope you will be enjoying you day","Ok, I will be shutting off myself."]
            speak(random.choice(li)) 
            sys.exit() 

        elif 'thank you' in query: 
            speak('you are welcome')

        elif "write" in query:
            query=query[7:]
            writeit(query)
        
        elif "press" in query:
            pressit(query) 

        elif "hold" in query:
            if "press and hold" in query:
                query=query[10:]
            hold(query)
        
        elif "release" in query:
            release(query)


        elif 'play music' in query:
            #youtube
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "open incognito" in query:
            webbrowser.open("google.com")
            time.sleep(1)
            pyautogui.hotkey("Ctrl","Shift","N")
            speak("What you wan tto search Sir?")
            content = takeCommand()
            if "search" in content:
                if "search for" in content:
                    content=content[11:]
                elif "search" in content:
                    content=content[8:]

                pyautogui.write(content)
                pyautogui.hotkey("enter")
                
        elif "show all window" in query or "show all tabs" in query:
            show_tab()
            time.sleep(3)
            hide_tab()

        elif query in ['hello',"hi","hey"]:
            speak('hello, how can i help you ??')
        
        elif 'who made you' in query or 'created you'in query:
            speak('I have been created by Sanyam Shandilya, Kriti Aggarwal, Deepanshu Jaiswal and Nikita Rawat')
        
        elif 'who are you' in query:
            speak('i am Jarvis, your virtual assistant. how can i help you?')
        
        elif 'how are you' in query:
            speak('i am fine,Thankyou and how about you?')

        elif 'fine' in query or 'good' in query:
            speak('It is good to know that you are doing good')
        
        elif 'can you do' in query:
            speak('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time, find your location, locate areas on map,  open different websites like instagram, youtube, gmail, git hub, stack overflow and  can also searche on google.''')



        '''elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") '''   
