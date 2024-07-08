import datetime
import os
import random
import sys
import webbrowser
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit as kit
import speech_recognition as sr
import wikipedia
import MyAlarm
from MyAlarm import alarm
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QTime, QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from frontend import Ui_NEEMO


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):  # Defining speak function
    engine.say(audio)
    engine.runAndWait()

#passcode

def greet():  # defining greet function
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("Good Morning")
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        print("Good Afternoon")
        speak("Good Afternoon!")

    else:
        print("Good Evening")
        speak("Good Evening!")

    print("I am Neemo, a desktop assistant, created by Ayush and Vishnu. I can look up answers for you or help you in finding the quickest way home. If you need anything, please wake me up.")


    speak("I am Neemo, a desktop assistant, created by Aayoosh and Vishnu. I can look up answers for you, or help you in finding the quickest way home.! If you need anything, please wake me up.")

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()




    def run(self):
        #passcode(self)
        greet()
        while True:
            self.query = self.takeCommand()

            if "break" in self.query or "wake" in self.query or "makeup" in self.query:
                self.task_execution()

            elif "goodbye" in self.query or "thank you" in self.query or "thanks" in self.query or "terminate" in self.query or "exit" in self.query:
                print("I hope I was helpful to you. Good bye...")
                speak("I hope I was helpful to you. Good bye.")
                sys.exit()


    def takeCommand(self):
        # It takes microphone input from the user and returns string output

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1   # time in seconds of non-speaking audio before a phrase is considered to be complete
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")

        except Exception:
            return "None"
        query = query.lower()
        return query



    def task_execution(self):
        print("Hello! I am on. You will see the written output on the console. In case you type something,type in the console.")
        speak("Hello! I am on. You will see the written output on the console. In case you type something,type in the console.")
        print("How may I help you?")
        speak("How may I help you?")

        while True:
            self.query = self.takeCommand()
#1)to search on wikipedia
            if 'wikipedia' in self.query:
                try:
                    print("Searching Wikipedia...")
                    speak('Searching Wikipedia...')
                    self.query = self.query.replace("Wikipedia", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    print("According to Wikipedia")
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except Exception:
                    print('Sorry, some error occured!')
                    speak("Sorry, some error occured!")
#2)to open yt
            elif 'open youtube' in self.query:
                print("Ok! Opening Youtube")
                speak('Ok! Opening Youtube')
                webbrowser.open("youtube.com")
#3)to open google
            elif 'google' in self.query:
                print("What should I search on google?")
                speak(" what should i search on google? ")
                cm = self.takeCommand().lower()
                print("searching...")
                speak("Searching.")
                webbrowser.open(f"{cm}")
#4)to open twitter
            elif "twitter" in self.query or "Twitter" in self.query:
                print("Opening twitter for you")
                speak("Opening twitter for you.")
                webbrowser.open("twitter.com")
#5)to open instagram
            elif "instagram" in self.query or "insta" in self.query:
                print("Opening instagram for you")
                speak("Opening instagram for you.")
                webbrowser.open("instagram.com")
#6)to play anime
            elif "cartoon" in self.query or "cartoons" in self.query or "animated movie" in self.query:
                print("Opening the website for you to play anime.")
                speak("Opening the website for you to play anime.")
                webbrowser.open("kayoanime.com")
#7)to tell the current time
            elif 'time' in self.query or "current time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time is{strTime}")
                speak(f"  The time is {strTime}")
                print(strTime)
#8)to open notepad
            elif "notepad" in self.query or "open notepad" in self.query:
                print("Ok! Opening notepad.")
                path="notepad.exe"
                os.startfile(path)
                speak("Ok! Opening notepad.")
#9)to open command prompt
            elif "open command prompt" in self.query:
                print("Ok! Opening command prompt")
                speak("Ok! Opening Command Prompt.")
                os.system("start cmd")
#10)to play song on yt
            elif "song on youtube" in self.query or "songs on youtube" in self.query or "song" in self.query:
                print("Please tell me the song name:")
                speak("Please tell me the song name.")
                song_choice = str(self.takeCommand())
                speak("Ok! Searching song on youtube")
                kit.playonyt(song_choice)
#11)to set alarm
            elif "set alarm" in self.query or "alarm" in self.query or "set an alarm" in self.query:
                print("Tell me the time at which you want to set your alarm, for example: 6:00 a.m.")
                speak('Tell me the time at which you want to set your alarm! for example, 6 0 0 a, m')
                nn = self.takeCommand()
                nn = nn.replace('set alarm to',"")      #6:00 a.m.
                nn = nn.replace(".","")           #6:00 am
                nn = nn.upper()             #6:00 AM
                MyAlarm.alarm(nn)
                speak("Ok! Setting alarm!")
                print("Ok! Setting alarm for",nn)
#12)to hear a joke
            elif "joke" in self.query:
                joke = pyjokes.get_jokes()
                print(joke)
                speak(joke)
#13)to close notpad
            elif "close notepad" in self.query:
                print("Ok! Closing notepad")
                speak("Ok! closing notepad.")
                os.system("taskkill /f /im notepad.exe")
#14)to toss a coin
            elif "heads or tails" in self.query or "toss" in self.query:
                coin=random.randint(1,2)
                if coin == 1:
                    speak('heads')
                    print('heads')
                else:
                    speak('tails')
                    print('tails')
#15)to perform arithmetic calculations
            elif 'open calculator' in self.query:
                print("Ok! Opening Neemo's Calculator")
                speak("Ok! Opening Neemo's Calculatar")
                import NeemoCalculator
#16)to roll a dice
            elif "dice" in self.query:
                dice=random.randint(1,6)
                speak("ok! rolling the dice. Let's see what you get!")
                print("Ok! rolling the dice. Let's see what you get")
                if dice==1:
                    speak("oh! you got 1!")
                    print("oh! you got 1")
                elif dice == 2:
                    speak('oh! you got 2!')
                    print('oh! you got 2')
                elif dice == 3:
                    speak('oh! you got 3!')
                    print('oh! you go 3')
                elif dice == 4:
                    speak('oh! you got 4!')
                    print('oh! you got 4')
                elif dice == 5:
                    speak('oh! you got 5!')
                    print('oh! you got 5')
                else:
                    speak('oh! you got 6!')
                    print('oh! you got 6')
#17)to draw different cartoon characters along with the Tiranga
            elif "draw" in self.query or "paint" in self.query:
                try:
                    print("I can draw Doraemon, Shinchan, BTS Logo, Among us,Iron Man's head, Tiranga and the surprise.")
                    speak("I can draw Doraemon, Shinchan, BTS Logo, Among us,Iron Man's head, Tiranga and the surprise.")
                    print("What do you want me to draw?")
                    speak("What do you want me to draw?")
                    draw_pic = self.takeCommand()
                    if "doraemon" in draw_pic:
                        try:
                            print("Ok! Drawing Doraemon")
                            speak("Ok. Drawing Doraemon")
                            import doraemondrawing
                        except exception:
                            pass
                    elif "shinchan" in draw_pic or "shin chan" in draw_pic or "shin-chan" in draw_pic:
                        try:
                            print("Ok! Drawing Shinchan")
                            speak("Ok. Drawing Shinchan.")
                            import shinchandrawing
                        except Exception:
                            pass
                    elif "bts" in draw_pic or "b t s" in draw_pic or "b-t-s" in draw_pic:
                        try:
                            print("Ok! Drawing BTS logo")
                            speak("Ok! Drawing B T S logo.")
                            import btsdrawing
                        except Exception:
                            pass
                    elif "among us" in draw_pic or "amongus" in draw_pic:
                        try:
                            print("Ok! Drawing Among Us")
                            speak("Ok. Drawing Among Us.")
                            import amongus
                        except Exception:
                            pass
                    elif "iron man" in draw_pic or "Iron Man" in draw_pic or "iron-man" in draw_pic:
                        try:
                            print("Ok! Drawing Iron Man's head")
                            speak("Ok. Drawing Iron Man's head.")
                            import ironmandrawing
                        except Exception:
                            pass
                    elif "flag" in draw_pic or "tiranga" in draw_pic:
                        try:
                            print("Ok! Drawing the National Flag of India")
                            speak("Ok. Drawing the National Flag of India.")
                            import nationalflagdawing
                        except Exception:
                            pass
                    elif "surprise" in draw_pic or "price" in draw_pic or "prize" in draw_pic:
                        print("Ok! Drawing our honourable C.S teacher Binit Sir :)")
                        speak("Ok! Drawing our honourable C.S teacher Binit Sir :)")
                        import binitsir
                        print("A good teacher is not that hard to find, but you must know where to look.\nI can sense Binit Sir around me who always expands his knowledge and continues to provide good answers to you both.\n He is like a friend that helps you in all your troubles.\nMost importantly, he is one of the teachers who do not merely focus on your academic performance but your overall development.\nHe understands your problems and tries to deal with them correctly.\nHe makes you feel like you always have someone to talk to if you cannot do so at home or with your friends.")
                        speak("A good teacher is not that hard to find, but you must know where to look.  ")
                        speak("I can sense, Binit Sir around me, who always expands his knowledge and continues to provide good answers to you both.   ")
                        speak(" He is like a friend that helps you in all your troubles.")
                        speak("Most importantly, he is one of the teachers, who do not merely focus on your academic performance, but your overall development.   ")
                        speak("He understands your problems, and tries to deal with them, correctly.")
                        speak("He makes you feel like you always have someone to talk to if you cannot do so at home or with your friends.")
                except Exception:
                    pass
#18)to work on mysql connector
            elif "my SQL connector" in self.query or "connector" in self.query:
                try:
                    print("Please type the host name e.g localhost:")
                    speak("Please type the host name, for example, local host")
                    h = input()
                    print("Please type the username e.g root:")
                    speak("Please type the username, for example, root")
                    u = input()
                    print("Please name the database:")
                    speak("Please name the database")
                    dbs = input()
                    print("Please give the password of your my sql:")
                    speak("Please give the password of your my sql")
                    pas = input()
                    print("Processing. Please wait!")
                    speak("Processing. Please wait!")
                    import mysql.connector as ms
                    mycon = ms.connect(host=h, user=u, passwd=pas, database=dbs)

                    if mycon.isconnected():
                        print("\nSuccessfully connected to device.\n")
                        speak("Successfully connected to device.")                    
                        cur = mycon.cursor()
                        while True:
                            print("Say 'create table' to create a table in your database.")
                            speak("Say create table to create a table in your database.")
                            print("Say 'alter table' to make changes in your table.")
                            speak("Say alter table to make changes in your table.")
                            print("Say 'drop table' to delete a table.")
                            speak("Say drop table to delete a table.")
                            print("Say 'describe table' to view structure of the table.")
                            speak("Say describe table to view structure of a table.")
                            print("Say 'select' to select all elements.")
                            speak("Say select to select all elements.")
                            print("Say 'insert' to insert an elements.")
                            speak("Say insert to insert an element.")
                            print("Say 'update' to update an element of a table.")
                            speak("Say update to update an element of a table.")
                            print("Say 'delete' to delete an element.")
                            speak("Say delete to delete an element.")
                            self.query = self.takeCommand()

#to create a table
                            if "create table" in self.query or "create" in self.query:
                                try:
                                    print("Provide table name:")
                                    speak("Provide table name.")
                                    name = self.takeCommand()
                                    print("How many fields do you want in your table? The maximum number of fields to be added is 5")
                                    speak("How many fields do you want in your table? The maximum number of fields to be added is 5")
                                    op = str(self.takeCommand())
#for 1 field
                                    if "one" in op or '1' in op:
                                        print("Provide the name of the field:")
                                        speak("Provide the name of the field.")
                                        field_name1 = self.takeCommand()
                                        print("Type the datatype of field e.g int(5):")
                                        speak("Type the data type of field, for example int 5.")
                                        field_type1 =str(input())
                                        query_create1 = "create table " + name + '(' + field_name1 + ' ' + field_type1 + ');'
                                        cur.execute(query_create1)
                                        print('\nTask completed. Table created with 1 field.\n')
                                        speak("Task completed. Table created with one field.")
#for 2 fields
                                    elif "two" in op or '2' in op or "tu" in op:
                                        print("Provide the name of the 1st field:")
                                        speak("Provide the name of the first field.")
                                        field_name1 = self.takeCommand()
                                        print("Type the datatype of 1st field e.g int(5):")
                                        speak("Type the data type of first field, for example int 5")
                                        field_type1 =str(input())
                                        print("Provide the name of 2nd field:")
                                        speak("Provide the name of second field.")
                                        field_name2 = self.takeCommand()
                                        print("Type the datatype of 2nd field:")
                                        speak("Type the data type of seconf field.")
                                        field_type2 =str(input())
                                        query_create2 = "create table " + name + '(' + field_name1 + ' ' + field_type1 + ',' + field_name2 + ' ' + field_type2 + ');'
                                        cur.execute(query_create2)
                                        print('\nTask completed. Table created with 2 fields.\n')
                                        speak("Task completed. Table created with two fields.")
#for 3 fields
                                    elif "three" in op or '3' in op:
                                        print("Provide the name of the 1st field:")
                                        speak("Provide the name of the first field.")
                                        field_name1 = self.takeCommand()
                                        print("Type the datatype of 1st field e.g int(5):")
                                        speak("Type the data type of first field, for example int 5.")
                                        field_type1 = str(input())
                                        print("Provide the name of the 2nd field:")
                                        speak("Provide the name of the second field.")
                                        field_name2 = self.takeCommand()
                                        print("Type the datatype of 2nd field:")
                                        speak("Type the data type of second field.")
                                        field_type2 =str(input())
                                        print("Provide the name of the 3rd field:")
                                        speak("Provide the name of the third field.")
                                        field_name3 = self.takeCommand()
                                        print("Type the datatype of 3rd field:")
                                        speak("Type the data type of third field.")
                                        field_type3 = str(input())
                                        query_create3 = "create table " + name + '(' + field_name1 + ' ' + field_type1 + ',' + field_name2 + ' ' + field_type2 + ',' + field_name3 + ' ' + field_type3 + ');'
                                        cur.execute(query_create3)
                                        print('\nTask completed. Table created with 3 fields.\n')
                                        speak("Task completed. Table created with three fields.")
#for 4 fields
                                    elif "four" in op or '4' in op:
                                        print("Provide the name of the 1st field:")
                                        speak("Provide the name of the first field.")
                                        field_name1 = self.takeCommand()
                                        print("Type the datatype of the 1st field e.g int(5):")
                                        speak("Type the data type of the first field, for example int 5.")
                                        field_type1 = str(input())
                                        print("Provide the name of the 2nd field:")
                                        speak("Provide the name of the second field.")
                                        field_name2 = self.takeCommand()
                                        print("Type the datatype of the 2nd field:")
                                        speak("Type the data type of the second field.")
                                        field_type2 = str(input())
                                        print("Provide the name of the 3rd field:")
                                        speak("Provide the name of the  third field.")
                                        field_name3 = self.takeCommand()
                                        print("Type the datatype of the 3rd field:")
                                        speak("Type the data type of the third field.")
                                        field_type3 = str(input())
                                        print("Provide the name of the 4th field:")
                                        speak("Provide the name of the fourth field.")
                                        field_name4 = self.takeCommand()
                                        print("Type the datatype of the 4th field:")
                                        speak("Type the data type of the fourth field.")
                                        field_type4 =str(input())
                                        query_create4 = "create table " + name + '(' + field_name1 + ' ' + field_type1 + ',' + field_name2 + ' ' + field_type2 + ',' + field_name3 + ' ' + field_type3 + ',' + field_name4 + ' ' + field_type4 + ');'
                                        cur.execute(query_create4)
                                        print('\nTask completed. Table created with 4 fields.\n')
                                        speak("Task completed. Table created with four fields.")
#for 5 fields
                                    elif "five" in op or '5' in op:
                                        print("Provide the name of the 1st field:")
                                        speak("Provide the name of the first field.")
                                        field_name1 = self.takeCommand()
                                        print("Type the datatype of the 1st field:")
                                        speak("Type the data type of the first field.")
                                        field_type1 = str(input())
                                        print("Provide the name of the 2nd field:")
                                        speak("Provide the name of the second field.")
                                        field_name2 = self.takeCommand()
                                        print("Type the datatype of the 2nd field:")
                                        speak("Type the data type of the second field.")
                                        field_type2 =str(input())
                                        print("Provide the name of the 3rd field:")
                                        speak("Provide the name of the third field.")
                                        field_name3 = self.takeCommand()
                                        print("Type the datatype of the 3rd field:")
                                        speak("Type the data type of the third field.")
                                        field_type3 = str(input())
                                        print("Provide the name of the 4th field:")
                                        speak("Provide the name of the fourth field.")
                                        field_name4 = self.takeCommand()
                                        print("Type the datatype of the 4th field:")
                                        speak("Type the data type of the fourth field.")
                                        field_type4 = str(input())
                                        print("Provide the name of the 5th field:")
                                        speak("Provide the name of the fifth field.")
                                        field_name5 = self.takeCommand()
                                        print("Type the datatype of the 5th field:")
                                        speak("Type the data type of the fifth field.")
                                        field_type5 = str(input())
                                        query_create5 = "create table " + name + '(' + field_name1 + ' ' + field_type1 + ',' + field_name2 + ' ' + field_type2 + ',' + field_name3 + ' ' + field_type3 + ',' + field_name4 + ' ' + field_type4 + ',' + field_name5 + ' ' + field_type5 + ');'
                                        cur.execute(query_create5)
                                        print('\nTask completed. Table created with 5 fields.\n')
                                        speak("Task completed. Table created with five fields.")

                                    else:
                                        print('Invalid number of fields chosen! Table not created.')
                                        speak("Invalid number of fields chosen. Table not created.")
                                except Exception:
                                    print("Something went wrong! Try again using correct values.")
                                    speak("Something went wrong. Try again using correct values.")

#to alter a table
                            elif "alter table" in self.query or "alter" in self.query:
                                try:
                                    cur.execute("show tables;")
                                    print("Which table do you want to alter?")
                                    speak("Which table do you want to alter?")
                                    name = self.takeCommand()
                                    print("What do you want to do? \n Add a field or modify a field in the table?")
                                    speak("What do you want to do?")
                                    speak("Add a field or modify a field in the table?")
                                    alter_function = self.takeCommand()
#to add a field in a table
                                    if "add" in alter_function:
                                        print("Please provide the name of new field to be added:")
                                        speak("Please provide the name of new field to be added.")
                                        new_field = self.takeCommand()
                                        print("Please Type the datatype of the field e.g int(5):")
                                        speak("Please provide the data type of the field, for example int 5.")
                                        new_field_type = str(input())
                                        query_alter_add = "alter table" + " " + name + " " + "add" + " " + new_field + " " + new_field_type +";"
                                        cur.execute(query_alter_add)
                                        print(new_field," added successfully.")
                                        speak("Field added successfully.")

#to modify a field in a table
                                    elif "modify" in alter_function:
                                        print("Which field you want to modify?")
                                        speak("Which field you want to modify?")
                                        alterfield = self.takeCommand()
                                        print("Type the new datatype to be assigned to",alterfield)
                                        speak("Type the new data type to be assigned tothe field")
                                        altertype = str(input())
                                        query_alter_modify="alter table" + " " + name + " " + "modify" + " " + alterfield + " " + altertype + ";"
                                        cur.execute(query_alter_modify)
                                        print(alterfield," modified successfully")
                                        speak("Field modified successfully")

                                    else:
                                        print("Incorect choice. Table not altered!")
                                        speak("Incorrect choice. Table not altered.")
                                except Exception:
                                    print("Something went wrong! Try again using correct values.")
                                    speak("Something went wrong! Try again using correct values.")

#to drop a table
                            elif "drop table" in self.query or "drop" in self.query:
                                try:
                                    print("Which table you want to delete?")
                                    speak("Which table you want to delete?")
                                    drop_table_name = self.takeCommand()
                                    query_drop = "drop table" + " " + drop_table_name + ";"
                                    cur.execute(query_drop)
                                    print(drop_table_name," deleted successfully.")
                                    speak("Table deleted successfully.")
                                except Exception:
                                    print("Some error eccored. Table not deleted!")
                                    speak("Some error occured. Table not deleted.")

#to describe a table
                            elif "describe table" in self.query or "describe a table" in self.query:
                                try:
                                    cur.execute("show tables;")
                                    print("Which table do want to describe?")
                                    speak("Which table you want to describe?")
                                    desc_table = self.takeCommand()
                                    query_desc_table = "desc" + " " + desc_table + ";"
                                    cur.execute(query_desc_table)
                                except Exception:
                                    print("An error occured. Table could not be described!")
                                    speak("An error occured. Table could not be described!")

#to select element
                            elif "select" in self.query:
                                try:
                                    print("which table you want to display the elements of?")
                                    speak("Which table you want to display the elements of?")
                                    select_table = self.takeCommand()

                                    print("Do you want to select all elements or elements using conditions?")
                                    speak("Do you want to select all elements or elements using conditions?")
                                    select_con = self.takeCommand()

                                    if "all" in select_con:
#to select all elements
                                        select_all = "select * from" + select_table + ";"
                                        cur.execute(select_all)
                                    elif "condition" in select_con:
                                        print("Please type the condition e.g select name from <tablename> where roll no=1:")
                                        speak("Please type the condition, for example, select name from table name where roll number is equal to 15")
                                        condition_select = str(input())
                                        cur.execute(condition_select)
                                except Exception:
                                    print("An error occured! Elements could not be displayed.")
                                    speak("An error occured. Elements could not be displayed.")
#to insert element
                            elif "insert" in self.query:
                                try:
                                    cur.execute("shoe tables;")
                                    print("Which table you want to insert elements into?")
                                    speak("Which table you want to insert elements into?")
                                    insert_table = self.takeCommand()
                                    print("Please type the query to insert e.g insert into <table_name> values(<value1>,<value2>);")
                                    speak("Please type the query in the console correctly.")
                                    insert_con = str(input())
                                    mycon.execute(insert_con)
                                    print("Element inserted successfully.")
                                    speak("Element inserted successfully.")
                                except Exception:
                                    print("Some error occured. Element not inserted.")
                                    speak("Some error occured. Element not inserted")
#to update element
                            elif "update" in self.query:
                                try:
                                    cur.execute("show tables;")
                                    print("Which table you want to update?")
                                    speak("Which table you eant to update?")
                                    update_table = self.takeCommand()
                                    print("Please type the query e.g update <table_name> set <field_name>=<value>;")
                                    speak("Please type the query in the console correctly.")
                                    update_query = str(input())
                                    cur.execute(update_query)
                                    mycon.commit()
                                    print("Table updated suucessfully.")
                                    speak("Table updated successfully.")
                                except Exception:
                                    print("Some error occured. Table not updated.")
                                    speak("Some error occured. Table not updated.")
#to delete element
                            elif "delete" in self.query:
                                try:
                                    cur.execute("show tables;")
                                    print("Which table you want to delete?")
                                    speak("Which table you want to delete?")
                                    delete_table = self.takeCommand()
                                    print("Please type the condition to be deleted:")
                                    speak("Please type the condition to be deleted:")
                                    delete_con = str(input())
                                    delete_query = "delete from" + delete_table + "where" + delete_con + ";"
                                    cur.execute(delete_query)
                                    mycon.commit()
                                    print("Table deleted successfully.")
                                    speak("Table deleted successfully.")
                                except Exception:
                                    print("Some error occured. Table not deleted.")
                                    speak("Some error occured. Table not deleted.")
                            else:
                                pass




                    else:
                        pass
                except Exception:
                    pass
#19)neemo at standby
            elif "stand by" in self.query or "no" in self.query:
                print("Ok! Going on stand by. Whenever you need my help, just say wake up or say good bye to exit")
                speak("Ok! Going on stand by. Whenever you need my help, just say wake up or say good bye to exit.")
                break
#20)what can you do
            elif "what can you do" in self.query:
                print("I can help you with wikipedia searches, open google and search whatever you want, open youtube, play songs on youtube, open twitter and instagram, open anime website, open and close notepad, open command prompt, tell you the current time, set alarm, tell jokes, roll a dice, toss a coin, open calculator, draw something for you and help you with python-mysql connectivity.")
                speak("I can help you with wikipedia searches, open google and search whatever you want, open youtube, play songs on youtube, open twitter and instagram, open animated movie website, open and close notepad, open command prompt, tell you the current time, set alarm, tell jokes, roll a dice, toss a coin, open calculator, draw something for you and help you with python mysql connectivity.")

            else:
                print("No function performed.")
                speak("No function performed.")
            print("Do you want me to do anything else for you?")
            speak("Do you want me to do anything else for you?")


startExecution = MainThread()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_NEEMO()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)





    def startTask(self):
        #passcode(self)
        timer = QTimer(self)
        self.ui.movie = QtGui.QMovie("C:\\Users\\user\\Desktop\\NEEMO\\newfrontend.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer.timeout.connect(self.showDateTime)
        timer.start(1000)
        startExecution.start()

    def showDateTime(self):
          current_time = QTime.currentTime()
          current_date = QDate.currentDate()
          label_time = current_time.toString('hh:mm:ss')
          label_date = current_date.toString(Qt.ISODate)

          self.ui.textBrowser.setText(label_date)
          self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
neemo = Main()
neemo.show()
sys.exit(app.exec_())
