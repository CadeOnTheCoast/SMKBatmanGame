from sys import exit
#import os for 'say' capability to make the program auditory
import os
#import PIL Image function to allow us to open images and show them to the user
from PIL import Image
#Used to help randomize lists so we give the user some variety in pictures and videos
import random
#used to open a hyperlink to youtube in the intro_video function
import webbrowser

#makes the game print out and speak the given value
def speak(words):
    print(f"{words}")
    os.system(f"say {words}")

#Starts the game by giving an introduction then giving the user an option to see an intro video via batman_intro()
#The user can pick from one of three forks - head to the batcave, drive batmobile, or fly
def start():
    speak("It\'s the year 2020, you\'ve just found out that YOU are batman.")
    speak("Do you need to see your intro video?")
    choice = input("> ")

    if choice == "yes" or choice == "Yes":
        batman_intro()

    elif "Bruce" in choice or "off" in choice:
        Bruce_Wayne_Mode()

    elif "No" in choice or "no" in choice:
        speak("Do you want to head to the batcave, drive the batmobile or fly?")
        choice2 = input("> ")

        if "cave" in choice2 or "Cave" in choice2:
            bat_cave()

        elif "batmobile" in choice2:
            batmobile()

        elif "fly" in choice2:
            fly()

        else:
            speak("That doesn\'t make sense. Let\'s head to the batcave to regroup!")
            bat_cave()
    else:
        speak("That doesn\'t make sense. Let\'s head to the batcave to regroup!")
        bat_cave()

#Explore the batcave
def bat_cave():
    speak("You walk into the bat cave, it\'s amazing!")
    bat_cave_pic()
    speak("You look around, you see your equipment, a comfy batman bed, and a mysterious bear")
    speak("What do you do first? Go look through your equipment, take a nap, or check out the mysterious bear")
    choice = input("> ")

    if "equipment" in choice:
        speak("You see your equipment. Your utility belt full of tools to stop bad guys.")
        speak("You\'ve got a cabinet full of grappling hooks, gadgets, and batman suits.")
        speak("What do you do next?")
        speak("You can put on your equipment and head out or keep exploring the batcave.")
        choice1 = input("> ")

        if "equipment" in choice or "out" in choice:
            Gotham()

        elif "explore" in choice or "batcave" in choice:
            bat_cave()

        else:
            speak ("You\'re confused. It\'s been a long time since you were new. Maybe getting out will help. Let\'s go see Gotham!")
            Gotham()

    elif "bear" in choice:
        mystery_bear(4)

    elif "nap" in choice:
        nap()

    else:
        speak("Probably time to get some fresh air. Villains of Gotham better watch out, Batman\'s on the prowl.")

def nap():
    speak("You feel refreshed.")
    speak("Wipe the drool of your mouth bat man. What\'s next? The mystery bear, drive the batmobile, or fly?")
    choice = input
    if "bear" in choice1:
        mystery_bear(4)

    elif "batmobile" in choice2:
        batmobile()

    elif "fly" in choice2:
        fly()


def Gotham():
    speak("You head out into Gotham. The big city sounds are all around. As you walk through the crowd you hear a maniacal laugh. It\'s Joker!")
    speak("He grabs someones ice cream as he runs away laughing. They should\'nt call this ice cream he cackles, They should call it me cream! he says")
    speak("Next up is ice cream world domination he giggles as he jumps into an ince cream truck!")
    speak("What are you going to do Batman? Follow him from the roof tops or fight him?")
    choice = input("1 = follow him! 2 = fight him!")

    while TRUE:
        if choice == 1:
            batman_follow()

        elif choice == 2:
            batman_fight()

        else:
            speak("that\'s not right, try again.")

def mystery_bear(number):

    attempts = 0
    for attempts in range (0, number):
        speak("You walk up to the bear")
        speak("It\'s mysterious")
        speak("It asks you a question")
        question = {
            "What is 1 + 1 batman?": '2',
            "What letter does bear start with": 'b',
            "are bats nocturnal?": 'yes'
            }

        rand_question = random.choice(list(question))
        speak(rand_question)
        answer = input(">")


        if answer == question[rand_question]:
            speak("Correct!")
            speak("The bear quietly walks away and flips a switch on a very large machine you hadn\'t noticed earlier. You feel a hard pull and hear a loud whirring then everything goes dark")
            teleport()

        #elif rand_question == questionlist[1] and choice == "b" or choice == "B":
        #    speak("Correct!")
        #    speak("The bear gives you a gift")
        #    speak("You\'ve unlocked batmans secret tools")
            #insert a pic here
            #need to think about if we can 'flip a switch here' i.e. set something to true so that the character has a special bonus in some later stage of the game
        #    bat_cave()

        #elif rand_question == questionlist[2] and choice == "yes" or choice == "Yes":
            #speak("Correct!")
            #speak("You\'ve unlocked batarangs!")
            #bat_cave()

        elif attempts == number:
            speak("Better luck next time")
            bat_cave()

        else:
            speak("That\'s incorrect, why don\'t you try another question")

#functions that I still need to create need to think if there's a way to be more concise
#def fly():

#def batmobile():

#def See_Joker():

#def Lair_Entrance_Normal():

#def Lair_entrance_Underground():

#def Lair_Entrance_Climb():

#BackpackPhoneTracker():

#def teleport():

def joker_pic():
    #joker_pic_list = ["Batcave.jpg", "Batcave1.jpeg", "batcave3.jpg", "batcave4.jpg", "batcave5.jpeg", "batcave6.jpeg", "batcave7.jpeg", "batcave8.jpeg", "batcave9.jpg"]
    #randpic = random.choice(bat_cave_pic_list)
    with Image.open("joker.jpg") as image:
        width, height = image.size

    try:
        img  = Image.open("joker.jpg")
        img.show()
    except IOError:
        pass

def bat_cave_pic():
    bat_cave_pic_list = ["Batcave.jpg", "Batcave1.jpeg", "batcave3.jpg", "batcave4.jpg", "batcave5.jpeg", "batcave6.jpeg", "batcave7.jpeg", "batcave8.jpeg", "batcave9.jpg"]
    randpic = random.choice(bat_cave_pic_list)
    with Image.open(randpic) as image:
        width, height = image.size

    try:
        img  = Image.open(randpic)
        img.show()
    except IOError:
        pass

def batman_intro():
    intro_video = ["https://www.youtube.com/embed/TZqUSQzukOI?controls=0&autoplay=1" , "https://www.youtube.com/watch/ws68JFY8qfI"]
    rand_intro = random.choice(intro_video)
    webbrowser.open(rand_intro)
    speak("Ok let\'s get to work!")
    speak("Do you want to head to the batcave, drive the batmobile or fly?")
    choice1 = input("> ")
    if "cave" in choice1:
        bat_cave()

    elif "batmobile" in choice1:
        batmobile()

    elif "fly" in choice1:
        fly()

def Bruce_Wayne_Mode():
    print("\nYou see your beautiful wife standing alone beside the fire in the batcave.")
    print("  You take off your cape and mask and walk up behind her. The firelight twinkles in her eyes and off of her highball glass.")
    print("  I\'m tired, you whisper into her ear. Tired of all this. If it wasn\'t for you, I dont know if I would still think good exists in Gotham.")
    print("  She turns around and leaning in closer whispers back. I can be bad too.")
    print("  She takes your hand and you both walk away...\n")
    love_pic()

def love_pic():
    love_pic_list = ["BatmanLove.jpg", "BatmanLove1.jpg", "BatmanLove2.jpg", "BatmanLove3.jpg"]
    randpic = random.choice(love_pic_list)
    with Image.open(randpic) as image:
        width, height = image.size
    try:
        img  = Image.open(randpic)
        img.show()
    except IOError:
        pass

start()
