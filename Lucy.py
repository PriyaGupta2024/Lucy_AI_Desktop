import pyttsx3   ## pip install from terminal
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os
import random
import pygame
import requests
import json
from bs4 import BeautifulSoup
from time import sleep
from datetime import timedelta
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk, ImageSequence  ## pip install pillow
import pygame
from pygame import mixer
import smtplib
import subprocess
import time
import pyautogui
   

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) [ 1 = woman OR 0 = man ]
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp = {"commandprompt": "cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt","spotify":"spotify","youtube":"youtube","google":"google"}    


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None" 
    return query

def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!!")

    else:
        speak("Good Evening!!")

    speak("i am Lucy!  Mam Please tell me how may I help you")


############# GUI of Lucy #####################
mixer.init()
root = Tk()
root.geometry("1000x500")
def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img 
    img = Image.open(r"C:\Users\PRIYA GUPTA\OneDrive\Desktop\OneDrive\Desktop\pikachu.gif")
    lbl = Label(root)
    lbl.place(x=0,y=0)
    i=0

    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

#play_gif()
#root.mainloop()        

###################### ROCK PAPER SCISSOR GAME ##########################
def game_play():
    speak("LETS PLAYYYYY GAME ")
    print("!!LETS PLAYYYY GAME  YEEEEEEEEEE!!")
    i = 0
    My_score = 0
    Com_score = 0

    while(i<8):
        choose = ("rock","paper" ,"scissor")
        com_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if(com_choose == "rock"):
                speak("ROCK")
                print("Rock")
                print(f"Score :- My :- {My_score} : Com :- {Com_score}")
            elif(com_choose == "paper"):
                speak("paper")
                print("paper")
                Com_score += 1
                print(f"Score :- My :- {My_score} : Com :- {Com_score}")

            else:
                speak("Scissors")
                print("Scissors")
                My_score += 1
                print(f"Score :- My :- {My_score} : Com :- {Com_score}")


        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                My_score += 1
                print(f"Score:- My :- {My_score+1} : Com :- {Com_score}")

            elif(com_choose == "paper" or query == "taper"):
                speak("paper")
                print("paper")
                print(f"Score:- My :- {My_score} : Com :- {Com_score}")
            else:
                speak("Scissors")
                print("Scissors")
                Com_score += 1
                print(f"Score:- My :- {My_score} : Com :-{Com_score}")


        elif (query == "scissors" or query == "scissor" or query == "caesar"):
            if (com_choose == "rock"):
                speak("ROCK")
                print("Rock")
                Com_score += 1
                print(f"Score:- My :- {My_score} : Com :- {Com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                print("paper")
                My_score += 1
                print(f"Score:- My :- {My_score} : Com :- {Com_score}")
            else:
                speak("Scissors")
                print("Scissors")
                print(f"Score:- My :- {My_score} : Com :- {Com_score}")


        i += 1  

    print(f"FINAL SCORE :- My :- {My_score} : Com:- {Com_score}")
    if(My_score > Com_score):
        print("Winner :- !!ME!!")
    
    elif(Com_score > My_score):
        print("Winner :- !!Computer!!")
    elif(Com_score == My_score):
        print("Winner :- !!Game is tie!!")

    else:
        print("Not Valid")    



###################### WHATSAPP FUNCTION #####################
strTime = int(datetime.now().strftime("%H"))
update = int((datetime.now()+timedelta(minutes = 2)).strftime("%M"))
def sendMessage():
    speak("Who do you want to message")
    a = int(input('''kshama-1
                     nikki-2
                     suuu-3
                     AK-4
                     mahek-5
                     arya-6
                     saavni-7
                     dipali-8
                     bade mama-9
                  
                  
                  '''))
    if a == 1:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91 93219 07617",message,time_hour=strTime,time_min=update)
        
    elif a == 2:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91 96939 61334 ",message,time_hour=strTime,time_min=update)
        
    elif a == 3:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91 74002 21786",message,time_hour=strTime,time_min=update)
        
    elif a == 4:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91 84336 06604 ",message,time_hour=strTime,time_min=update)
        
    elif a == 5:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91 87797 17686",message,time_hour=strTime,time_min=update)
        
    elif a == 6:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91 72085 22670",message,time_hour=strTime,time_min=update)
        
    elif a == 7:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91  85910 67429",message,time_hour=strTime,time_min=update)
        
    elif a == 8:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91  7738510264",message,time_hour=strTime,time_min=update)

    elif a == 9:
        speak("whats the message")
        message = str(input("Enter the message:- "))
        pywhatkit.sendwhatmsg("+91  8433776637",message,time_hour=strTime,time_min=update)    
        
############## clossing the web ####################
def closeappweb(query):
     speak("closing, mam")
     if "one tab" in query or "1 tab" in query:
           pyautogui.hotkey("ctrl","w")
           speak("All tabs closed")
     elif "two tab" in query:
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          speak("All tabs closed")
     elif "three tab" in query:
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          speak("All tabs closed")  
     elif "four tab" in query:
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          speak("All tabs closed")
     elif "five tab" in query:
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          sleep(0.5)
          pyautogui.hotkey("ctrl","w")
          speak("All tabs closed")

     else:
          keys = list(dictapp.keys())
          for app in keys:
               if app in query:
                    os.system(f"taskKill /f /im  {dictapp[app]}.exe");

def Searchweb(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("Lucy","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found for your search!")


        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

########################## News Function #####################
def latestnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=11488afa1d094c37918fadb3404219e8",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=11488afa1d094c37918fadb3404219e8",
               "healthcare":"https://newsapi.org/v2/top-headlines?country=us&category=healthcare&apiKey=11488afa1d094c37918fadb3404219e8",
               "science":"https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=11488afa1d094c37918fadb3404219e8",
               "sports":"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=11488afa1d094c37918fadb3404219e8",
               "technology":"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=11488afa1d094c37918fadb3404219e8",
               "economic":"https://newsapi.org/v2/top-headlines?country=us&category=economic&apiKey=11488afa1d094c37918fadb3404219e8",
               "population":"https://newsapi.org/v2/top-headlines?country=us&category=population&apiKey=11488afa1d094c37918fadb3404219e8",
               "politics":"https://newsapi.org/v2/top-headlines?country=us&category=politics&apiKey=11488afa1d094c37918fadb3404219e8",
               "stockmarket":"https://newsapi.org/v2/top-headlines?country=us&category=stockmarket&apiKey=11488afa1d094c37918fadb3404219e8"}
    
    content = None
    url = None
    speak("Which field news do you want [business] [entertainment] [healthcare] [science] [sports] [technology] [economic] [population] [politics] [stockmarket]")
    field = input("Type field news that you want:  ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
                print("url not ")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit : {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

        speak("thats all") 

if __name__ == "__main__":

    wishMe()
    while True:
      query = takeCommand().lower()
    #Logic for executing task based on query
      if 'wikipedia' in query:
          speak('searching Wikipedia......')
          query = query.replace("wikipedia","")
          results = wikipedia.summary(query,sentences=2)
          speak("Acording to wikipedia")
          print(results)
          speak(results)
################### MY Introduction #############################
      elif 'introduce priya gupta' in query:
          print("Hello, my name is Priya Gupta. I am currently pursuing a Bachelor of Engineering in Electronics and Computer Science from Mumbai University."
                 "I have a keen interest in backend development and am looking to further my skills in data science."
                   "My focus right now is on enhancing my technical skills, particularly in Java, Python, SQL, C programming, and project management." 
                   "I also enjoy solving problems related to data structures and algorithms." 
                   "I am here to explore new opportunities in the field and to connect with like-minded professionals.")
          
          speak("Hello, my name is Priya Gupta. I am currently pursuing a Bachelor of Engineering in Electronics and Computer Science from Mumbai University."
                 "I have a keen interest in backend development and am looking to further my skills in data science."
                   "My focus right now is on enhancing my technical skills, particularly in Java, Python, SQL, C programming, and project management." 
                   "I also enjoy solving problems related to data structures and algorithms." 
                   "I am here to explore new opportunities in the field and to connect with like-minded professionals. THANK YOU")   
      elif 'open google' in query:
          Searchweb(query)
        
      elif 'open youtube' in query:
            speak("This is what I found for your search!")
            query = query.replace("youtube search", "")
            query = query.replace("youtube","")
            query = query.replace("Lucy","")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Done Mam")

      elif "pause" in query:
          pyautogui.press("k")
          speak("Video paused")
      #elif "play" in query:
       #   pyautogui.press("k")
        #  speak("Video played")    
               
      elif 'open spotify' in query:
          webbrowser.open("spotify.com")

      elif 'open powerpoint' in query:
          pptpath ="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
          #subprocess.Popen(pptpath)
          os.startfile(pptpath)

      elif 'open word' in query:
          word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
          os.startfile(word_path)
             

      elif 'play music' in query:
          pygame.mixer.init()

          music_dir = 'C:\\Users\PRIYA GUPTA\Music'
          PRIYAGUPTA = [f for f in os.listdir(music_dir) if f.endswith('.mp3')]
          random_song = random.choice(PRIYAGUPTA)
          song_path =os.startfile(os.path.join( music_dir,random_song))
          pygame.mixer.music.load(song_path)
          pygame.mixer.music.play()


      elif 'time'in query:
          strTime = datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"Sir,the time is {strTime}")  


      elif 'open vscode' in query:
          codepath =  "C:\\Users\\PRIYA GUPTA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
          os.startfile(codepath)


      elif 'open' in query:    # EASY METHOD
          query = query.replace("open","")
          query = query.replace("lucy","")
          pyautogui.press("super")
          pyautogui.typewrite(query)
          pyautogui.sleep(2)
          pyautogui.press("enter")



      elif 'close' in query:
          closeappweb(query)

      elif "news" in query:
          latestnews()

      elif "whatsapp" in query:
          sendMessage()

      elif "play gif" in query:
          play_gif()

      elif "play game" in query:
          game_play()
                        
      elif 'terminate' in query:
          speak(" I am going to terminated , BYE MAM")
          exit()   


     
          
              



      






    
