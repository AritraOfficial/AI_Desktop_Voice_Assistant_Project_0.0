# ---------- Jarvis AI Desktop Voice Assistant ------------
import pyttsx3   #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime 
import wikipedia  #pip install wikipedia
import webbrowser 
import os
import smtplib
import cv2 #pip install opencv-python
import threading
#---------------------------------#


#---------------------------------
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices") #getting details of current voice
# print(voices[0].id)  # voice[0].id = Male voice 
# print(voices[1].id)  # voice[1].id = Female voice 
engine.setProperty("voice", voices[0].id)
#---------------------------------#


#---------------------------------
def speck(audio):
    engine.say(audio)
    engine.runAndWait() #Without this command, speech will not be audible to us.
#---------------------------------#



#---------------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speck(" Hello Aritra, A Very Good Morning!")
    elif hour>= 12 and hour<18:
        speck(" Hello Aritra, Good AfterNoon..")
    else:
        speck(" Hello Aritra Good Evening!")

    speck("Sir Here I am Your Voice Assistent .... Please Tell me how can i help you? ")
    
#---------------------------------#


#---------------------------------
def takeCommand():
     #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.energy_threshold = 600  # minimum audio energy to consider for recording
        #  r.dynamic_energy_threshold = True
         r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
         audio = r.listen(source)  

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        #Using google for voice recognition.
        print(f"User said > {query}\n")  #User query will be printed.
    except Exception as e:
        print(e)
        print("Say that again please... ") #Say that again will be printed in case of improper voice
        return "None"  #None string will be returned
    return query
#---------------------------------#


#---------------------------------
def sendEmail(to, content):
    #smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dellceoaritra.mukherjee@gmail.com', 'kmnanmmcykdyxthy')
    server.sendmail('youreamil@gmail.com', to, content)
    server.close()
#---------------------------------#


#---------------------------------
def open_camera():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Camera', frame)

        # Press 'q' to exit the camera
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
#     cv2.destroyAllWindows()

    #-----------------#

def click_picture():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Capture a single frame
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Get the current working directory
    current_directory = os.getcwd()

    # Save the captured frame as an image in the current directory
    img_filename = os.path.join(current_directory, "captured_picture.jpg")
    cv2.imwrite(img_filename, frame)

    speck("Picture clicked and saved as captured_picture.jpg.")
    # Display the path where the picture is saved
    print("Picture saved at:", img_filename)
#---------------------------------#



#################################################
if __name__ == "__main__":
    # speck("Hey Aritra, Here I am Your Voice Assistent... ")
    wishMe()
    while True:  #it is for unlimited time
    # if 2:
        query = takeCommand().lower() #Converting user query into lower case
        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            print('Searching Wikipedia... ')
            speck('Searching Wikipedia... ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speck("According to wikipedia")
            print(results)
            speck(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speck("ok opening youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            speck("ok opening google")

        elif 'open stack overflow' in query:
            webbrowser.open("https://stackoverflow.com/")
            speck("ok opening stackoverflow")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
            speck("ok opening gmail")


        elif 'play music' in query:
            music_dir = "D:\\A_M_Official\\SONG IN ALL\\Free Time" 
            songs = os.listdir(music_dir)
            # print(songs)
            speck("Ok playing Favorite song")
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'what is time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, The Time is {strTime}" )
            speck(f"Sir, The Time is {strTime}")

        elif 'open vs code' in query:
            code_path = "C:\\Users\\Aritra_Offficial\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
            speck("Ok Opening Visual Studio Code.")
        
        elif 'send email to sir' in query:
            try:
                speck("What shoud I say .. ")
                content = takeCommand()
                to = "aritra.mukherjee.5g@gmail.com"
                sendEmail(to, content)
                print("Email has been send! Thanks")
                speck("Email has been send! Thanks")
            except Exception as e:
                print(e)
                speck("Sorry! I am not able to send the email.")

        elif 'open camera' in query:
            speck("Sure! Opening the camera. But if You want to click this pic .. you have to run the 'click picture' command")
            # open_camera()
            camera_thread = threading.Thread(target=open_camera)
            camera_thread.start()
        elif 'click picture' in query:  # Add this condition to click a picture
            speck("Sure! Clicking a picture.")
            click_picture()


        elif 'exit' in query:  # Add this condition to check if the user said "exit"
            speck("Goodbye! Have a nice day.")
            break  # Exit the while loop and end the program
#################################################




#version: "2"
# authtoken: 2TUJBcPK49zpfHg2F4i7dnV3hGc_4SrHBLYtbNUkcYG4NCSjP
