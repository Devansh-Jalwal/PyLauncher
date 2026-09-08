import datetime
import os
import difflib
import time
import subprocess
import sys


import os, sys, subprocess

def run_program(file_name):
    base_folder = os.path.dirname(os.path.abspath(__file__))
    
    search_folders = [
        base_folder,
        os.path.join(base_folder, ".."),
        os.path.join(base_folder, "..", "Programs"),
        os.path.dirname(base_folder),
    ]
    
    try:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        for item in os.listdir(desktop):
            item_path = os.path.join(desktop, item)
            if os.path.isdir(item_path):
                search_folders.append(item_path)
    except:
        pass

    for folder in search_folders:
        possible_path = os.path.join(folder, file_name)
        if os.path.exists(possible_path):
            print(f"Found {file_name} -> Running from {possible_path}")
            subprocess.run([sys.executable, possible_path])
            return
            
    print(f"[!] Could not find {file_name} in nearby folders")
    print(f"    I searched in: {base_folder}")



print("A download is being started on your computer it's just installing liabraries don't worry :D")
print("It will not start if you already have them it will just say [OK]")

time.sleep(1)

if sys.version_info >= (3,13):
   print("Hmm Actually You are on a quite new version of Python which unfortunately can't install this feature")
   print("Don't Worry everything is still very good Just install Python 3.12 from https://www.python.org/downloads/release/python-31214/")
   print("Done?? Now Just check your bottom right which states Python (vesrion) if it's not 3.12 then click on it and change it to 3.12")
   print("You must be using VS code right? I know because You are Definitely NOT a psychopath")
   print("Right??")
   print("**** If it still don't change then uninstall Python (new version)***")
   print("If you don't know how to unistall then press windows button , then search Apps & Features go there and search Python and Uninstall all the other versions except 3.12 ")
   print("Thank You :D")
   input("Press Enter to Exit :D")
   sys.exit()
   


def setup_module(name):
    try:
        __import__(name)
        print(f"[OK] {name} found")
    except ImportError:
        print(f"\n[+] {name} not found. Installing... (first time only, 20 sec)")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", name])
            print(f"[OK] {name} installed successfully!")
        except Exception as e:
            print(f"\n[!] Failed to auto-install {name}")
            print(f" Please run manually in terminal: pip install {name}")
            print(f" Error was: {e}")
            input("Press Enter to exit...")
            sys.exit()
    finally:
        globals()[name] = __import__(name)

setup_module("pygame")
setup_module("requests")

print("[OK] All setup done! Starting game...\n")



timenow = datetime.datetime.now()
# You can add songs' names here ok?
SongList = """
"""

print("")
print("")
print("Ignore all this above..")
print("")
print("Hi there it's Me, The launcher You can know about me from README.md ")
print("")
print("")
y = input("Enter Your name Please,Press Enter to leave it blank : ")

while True:
 
 print("")
 print("")

 x = input(f"Hi {y} What's in Your Mind? : ").casefold()
 time.sleep(0.9)
 print("")
 print("")

 if x == "hi":
    print("hello human!")
 elif x == "hI":
    print("Hello Human!")
 elif x == "give me a random number":
    time.sleep(1)
    run_program("Random_Number.py")
 elif x == "fact":
    print("Findin Facts.. It may take a while...")
    run_program("facts.py")
 elif x == "facts":
    print("Findin Facts.. It may take a while...")
    run_program("facts.py")
 elif x == "quit":
    print("See you Later!")
    quit()


 elif x == "cmd":
    print("""The Commands Below Will help you to use The Actual Program -------->

1. play --> use the command "play" to play a song you should use the command in the way like  play Billie Jean   (But first you have to insert some songs in the folder
            named as "This Should be the place where your music should be".

2. stop --> Use "stop" to stop the music.


3. date --> type "date" to get the current date and day.


4. baseball --> A baseball game rules will be told in the game, use command "baseball" to play (You only have 1 chance).


5. weather --> Use command "weather" to check the current weather.


6. generate password --> Use command "generate password" to use a password generator.""")


 elif x == "cmds":
    print("""The Commands Below Will help you to use The Actual Program -------->

1. play --> use the command "play" to play a song you should use the command in the way like  play Billie Jean   (But first you have to insert some songs in the folder
            named as "This Should be the place where your music should be".

2. stop --> Use "stop" to stop the music.


3. date --> type "date" to get the current date and day.


4. baseball --> A baseball game rules will be told in the game, use command "baseball" to play (You only have 1 chance).


5. weather --> Use command "weather" to check the current weather.


6. generate password --> Use command "generate password" to use a password generator.""")




 elif x == "command":
     print("""The Commands Below Will help you to use The Actual Program -------->
 
 1. play --> use the command "play" to play a song you should use the command in the way like  play Billie Jean   (But first you have to insert some songs in the folder
             named as "This Should be the place where your music should be".
 
 2. stop --> Use "stop" to stop the music.
 
 
 3. date --> type "date" to get the current date and day.
 
 
 4. baseball --> A baseball game rules will be told in the game, use command "baseball" to play (You only have 1 chance).
 
 
 5. weather --> Use command "weather" to check the current weather.
 
 
 6. generate password --> Use command "generate password" to use a password generator.""")
 


          
 elif x == "what is the time?":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what is the time":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "whats the time":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "whats the time?":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what's the time":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what's the time?":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what the time is?":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what the time is":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "time?":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "time":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what is the time now":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what is the time now?":
    print(timenow.strftime("The Time Currently is: %I:%M  %P"))
 elif x == "what is the date?":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "what is the date":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "whats the date":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "whats the date?":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "what's the date":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "what's the date?":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "what the date is?":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "what the date is":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "date?":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "date":
    print(timenow.strftime("%d,%B,%Y (%A)"))
 elif x == "stop":
    print("Your Music has been stopped Successfully!")
 elif x.startswith("play "):
    print("sure")
    time.sleep(0.5)
    print("Here You Go!")
 elif x == "list":
    print(SongList)

 elif x == "baseball":
    time.sleep(1)
    print("Launching Baseball...")
    time.sleep(1)
    run_program("Baseball.py")
 elif x == "generate password":
    time.sleep(1)
    print("Sure")
    time.sleep(1)
    print("Launching Password Generator...")
    time.sleep(2)
    run_program("Password_Generator.py")
 elif x == "weather":
    print("Launching The Weather App...")
    time.sleep(1)
    print("Here You Go!")
    time.sleep(0.5)
    run_program("Weather_app.py")
 else:
   print("Invalid Prompt,You can only use some certain commands   Go to commands.txt on your computer to know the commands")



 pygame.mixer.init()

 BASE_DIR = os.path.dirname(os.path.abspath(__file__))
 MUSIC_FOLDER = os.path.join(BASE_DIR, "This Should Be the place where your Music should Be")
 os.makedirs(MUSIC_FOLDER, exist_ok=True)

 def play_song(song_name):
    songs = os.listdir(MUSIC_FOLDER)

    match = difflib.get_close_matches(song_name, songs, n=1, cutoff=0.4)

    if match:
        song_path = os.path.join(MUSIC_FOLDER, match[0])
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()
        print(f"Bot: Playing {match[0]}")
    else:
        print("Song not found in your folder type 'list' to get the list of the songs,You have to add songs and names in the list manually")



 if "play" in x:
    song = x.replace("play", "").strip()
    play_song(song)
 elif x == "stop":
    pygame.mixer.music.stop()


    


 time.sleep(1)