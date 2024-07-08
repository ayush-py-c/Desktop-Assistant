<h1 align="center" id="title">Desktop-Assistant</h1>

<p align="center"><img src="https://socialify.git.ci/ayush-py-c/Desktop-Assistant/image?language=1&amp;owner=1&amp;name=1&amp;stargazers=1&amp;theme=Light" alt="project-image"></p>

<p id="description">NEEMO is a virtual desktop assistant built using python modules and libraries. The main objective of developing a virtual assistant is to minimize the use of input devices like keyboard mouse touch pens etc. As a result the hardware cost as well as the space occupied would be reduced. User can use it when he/she feels lonely and bored. It can also become a means of entertainment due to its interactive nature</p>



## Table Of Contents



- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [System Architecture](#system-architecture)
  - [Speech Recognition](#speech-recognition)
  - [TTS & STT-](#TTS-&-STT-)
-[Imported Modules](#imported-modules)
  -[SYS MODULE](#SYS-MODULE)
  -[pywhatkit](#pywhatkit)
  -[OS MODULE](#OS-MODULE)
  -[WIKIPEDIA](#WIKIPEDIA)
  -[DATETIME](#datetime)
  -[PYTTSX3](#pyttsx3)
    
## About The Project

![WhatsApp Image 2024-07-08 at 21 25 18_98d08b76](https://github.com/ayush-py-c/Desktop-Assistant/assets/85986862/cbbb4bf4-ee83-4056-967d-70fe96f62178)


NEEMO is a virtual desktop assistant built using python modules and libraries. 
NEEMO is just a basic version of desktop assistants along with a GUI which could 
perform almost all the basic tasks mentioned below:

- Greet the user according to the time(being polite at the same time).
- Basic Arithmetic Calculations can also be performed just by giving a command.
- Inbuilt Calculator to be opened on a command.
- Search anything from the web or directly tell about something using Wikipedia.
- Open any application in the current system.
- Operate on any application using voice commands.
- Stream Music.
- Crack Jokes.
- Show Date & time.
- Set Alarm.
- Show a VIRTUAL KEYBOARD.
- Can operate sql commands (create,insert,delete etc) using voice commands.
- End any task or running application
- ![WhatsApp Image 2024-07-08 at 21 25 18_03fb39a3](https://github.com/ayush-py-c/Desktop-Assistant/assets/85986862/303fc33c-0bee-4eef-9830-23d9f8183cc4)
![WhatsApp Image 2024-07-08 at 21 25 17_32120c92](https://github.com/ayush-py-c/Desktop-Assistant/assets/85986862/4fa60981-2e2f-4b75-bced-7f52c9827153)


All these tasks can be carried out by voice recognition which makes NEEMO 
almost a perfect desktop assistant. The user will just have to run the program and it 
would do everything afterwards.

# System Architecture 

  - # Speech Recognition
      The speech recognition module used in the program is Google’s Speech 
    Recognition API which is imported in python   using he command “import 
    speech_recognition as sr”. This module helps the program to recognize the voice 
    which is given as an input by the user.

     ```sh
     pip install SpeechRecognition
      ```
  - # TTS & STT-
      The voice which is given as the input is    first converted to text using the 
      speech_recognition module. The process for  the above conversion used is TTS 
      (Text To Speech). The text is then processed by the interpreter in the form of a 
      syntax as we usually give in a python file.
      After the processing the interpreter gives the output in the form of text. 
      The output text is then converted into speech(NEEMO’s voice) by the process of 
    STT(Speech To Text).
    The most time consuming among the two is STT because it is difficult for 
    the program to recognize voices of different persons due to their differences. Some 
    are easily audible so easily processed but some are difficult to recognize and hence 
    it takes time in recognition.
    Once the speech is converted to text, executing commands and giving 
    the results back to the user is not a time consuming step for NEEMO.

# Imported modules
We have already discussed aboutspeech_recognition module and its working. 
Other modules used to create NEEMO(Desktop Assistant) are given below:

- # PYTTSX3
  The pyttsx3 is an offline module that is used for text to speech 
   conversions in Python and is supported by Python 2 & 3. The run and wait 
   functionality is also present in this module. It determines the time interval between 
  inputs given to the program.

  ```sh
     pip install pyttsx3
  ```
- # DATETIME 
    The datetime module is imported to support the functionality of the date 
  and time. This helps the user to know the current date and time if he/she wants to 
  schedule a task like an alarm or a reminder and perform operations accordingly. 
  This module also helps NEEMO(Desktop Assistant) in greeting the user at any time 
  the program is run.
  ```sh
     pip install DateTime
  ```
- # WIKIPEDIA
    Wikipedia is an online library for Python which makes it possible for
    NEEMO (Desktop Assistant) to process the queries regarding Wikipedia and 
    display the results to the user accordingly. The number of lines that the user wants 
    to get as the result can also be set
      
    ```sh
     pip install wikipedia
  ```
- # OS MODULE
    The os module provides an operating system dependent functionalities. 
  This enables in the task of opening applications like notepad, wordpad, ms-paint, 
  etc. when the user wants to write, read or    manipulate paths. All the operations available raise an “OSERROR” in case of any error like invalid names, paths or 
  arguments which may be correct but were not accepted by the operating system

    ```sh
     pip install os-sys 
  ```
- # pywhatkit
    pywhatkit is a Python library which enables the user to send whatsapp 
  messages at a certain time including several others features too. There are some 
  parameters which make it easy to send the message like it provides the features of 
  scheduling the time at which the message would be sent, waiting time after which 
  the message will be sent after opening the web, etc.
   ```sh
     pip install pywhatkit
  ```
- # SYS MODULE
    The sys module in Python provides various functions and variables that 
  are used to manipulate different parts of the Python runtime environment. It allows 
  operation on the interpreter as it provides access to the variables and functions that 
  interact strongly with the interpreter.


