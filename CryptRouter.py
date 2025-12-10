from collections import deque
import heapq
import itertools
import sys
# https://ddowiki.com/page/The_Shadow_Crypt/Instance_Paths - refer to this link for topology of instances

from room import Room
from instance import Instance
from utils import *


# next step: creating objects for each possible room (without pointers, just yet)

"""
GENERAL INSTANCE SETUP
"""

pointedRoomListInstance1  = [Room("Colorless", "Start")] # starting room = index 0
pointedRoomListInstance2  = [Room("Colorless", "Start")] # starting room = index 0
pointedRoomListInstance3  = [Room("Colorless", "Start")] # starting room = index 0


global instance1
global instance2
global instance3

"""
#TEST CASES



initializeInstance1()
initializeInstance2()
initializeInstance3()

start1 = pointedRoomListInstance1[2]
goal1 = pointedRoomListInstance1[13]
path1 = prioBFS(instance1, start1, goal1)
start2 = pointedRoomListInstance2[0]
goal2 = pointedRoomListInstance2[13]
path2 = prioBFS(instance2, start2, goal2)
start3 = pointedRoomListInstance3[7]
goal3 = pointedRoomListInstance3[13]
path3 = prioBFS(instance3, start3, goal3)



#printPath(path1, "instance 1 [RED]")
#printPath(path2, "instance 2 [GREEN]")
#printPath(path3, "instance 3 [BLUE]")


"""


firstIteration = True
foundInstance = False
yesSet = {"y", "yes"}
print("\nWelcome to Crypt-Router! Ver 1.041\n\nThis is a software to help you navigate your way throughout the Shadow Crypt Dungeon in DDO.\n")
while True:
    needInstructions = False
    while firstIteration:
        firstTimer = input("Is this your first time using Crypt-Router? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit.\n"+ orange("Enter Here: ")).lower()
        if yesNoAssociation(firstTimer):
            if firstTimer in yesSet:
                needInstructions = True
                break
            else:
                break
        elif isExitChar(firstTimer):
            sys.exit()
        else:
            print("Invalid input, try again.")
    if needInstructions:    
        welcStr = "\nAs you may or may not know, Shadow Crypt is one of the most experience-dense quests along the entire heroic leveling arc."
        welcStr += "\nDespite that, many players still do not run Shadow Crypt with regularity throughout their heroic leveling experience."
        welcStr += "\nThis can primarily be attributed to the fact that there is virtually no way to know where you are going in the dungeon, even with a map."
        welcStr += "\nWhile there are resources online with solo/duo paths for 8 or 12 gears to help you complete the quest,\nthere's not much of a contingency plan for a wrong turn."
        welcStr += "\nThat's where Crypt-Router comes in! in the event that you either do not have access to the known paths or have found yourself in a room found separate from the path"
        welcStr += "\nyou can use Crypt-Router to find your way back to a specific room from any of the rooms you may find yourself in in any given instance"
        welcStr += "\n\n How do I use Crypt-Router?"
        welcStr += "\n\n\t - First, you will begin by letting the program know if you know what instance you are in or not."
        welcStr += "\n\n\t - Second, you will be asked which instance you are in if you know your current instance; if not, the program will help figure out your instance\n\t along side you."
        welcStr += "\n\n\t - Third, you will give the program which room you are currently in\n\t ( of which can be written out as given to you or abbreviated by <first-letter-of-color><first-letter-of-structure> )"
        welcStr += "\n\n\t - Fourth, similarly to the last step you will let the program know which room you want to go to. Note: If you need a specific gear color,\n\t go to a room of that color."
        welcStr += "\n\nIMPORTANT NOTE:\t if you encounter a maze that you cannot traverse through, enter another room (sometimes more than one room away)\n\t and restart the program from there"
        welcStr += ". However, the program operates in such a way that most of the times you can avoid mazes altogether."
        welcStr += "\n\nAfter these steps, you will have been given a path formatted by which room you need to go to and which direction to go as well as\nuppercase directional format as traditionally used on DDO wiki. i.e EWSNE"
        print(welcStr)
    while firstIteration:
        startInput = input("\n\nReady to Find your way? type 'yes' or 'y' if so & 'no' or 'n' if not, or press 'enter' to exit.\n"+ orange("Enter Here: ")).lower()
        if(yesNoAssociation(startInput)):         
            if startInput in yesSet:
                break
            else:
                print("Closing Program ... Thank you for using Crypt Router!")
                sys.exit()
        elif isExitChar(startInput):
            sys.exit()
        else:
            print("Invalid Input, please try again.") 
    while True:
        if not foundInstance:
            userKnowInstance = input("\nDo you know which instance you are in? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower() # primary question for this while loop
            flagDD = None # initialize as None
            exitedInnerLoop = False
            inInstance1 = False
            inInstance2 = False
            inInstance3 = False
            isUnsure = False
            wasUnsure = False
            if yesNoAssociation(userKnowInstance): # checks to see if the response is a valid affirmative/negative response
                userKnowInstance = userKnowInstance.strip().lower() # use to make case insensitive
                while True: # use a while loop to loop back for mistaken instance responses
                    if userKnowInstance in yesSet: # basically, cannot proceed if they do not know their instance.
                        flagDD = False # because we know our instance DD becomes irrelevant
                        userInstance = input("\nWhich instance are you in? (r/g/b/red/green/blue) or press enter to exit\n"+ orange("Enter Response: ")).lower() # primary questions for this while loop
                        if instanceAssociation(userInstance): # verifies if any of the user's responses correlate to valid instances
                            userInstance = userInstance.strip().lower() # use to make case insensitive
                            # print(userInstance)
                            # print(isinstance(userInstance, str))
                            if userInstance == "r" or  userInstance == "red":
                                if firstIteration:
                                    initializeInstance1()
                                inInstance1 = True
                                # print("DEBUG: instance 1 initialized.")
                                break # if valid instance, no need to continue while loop
                            elif userInstance == "g" or userInstance ==  "green":
                                if firstIteration:
                                    initializeInstance2()
                                inInstance2 = True
                                # print("DEBUG: instance 2 initialized.")
                                break # if valid instance, no need to continue while loop
                            elif userInstance == "b" or userInstance == "blue":
                                if firstIteration:
                                    initializeInstance3()
                                inInstance3 = True
                                # print("DEBUG: instance 3 initialized.")
                                break # if valid instance, no need to continue while loop
                        elif isExitChar(userInstance):
                            # let outter loop know that there was an exit within the inner loop so that the outter loop can automatically break
                            sys.exit()
                        else:
                            print("please enter a valid instance")
                            continue # if invalid instance, ask again for a valid instance
                    else:
                        userDD = input("\nDo you Have Death's Door charges or Dimension Door Spell? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower() # allows for alternative to check instance ( returns player to starting room )
                        if(yesNoAssociation(userDD) and userDD in yesSet):
                            flagDD = True
                            print("Please use Deaths Door/Dimension door to return to the starting room, and go east to learn which instance you are in.\n")
                            break
                        elif isExitChar(userDD):
                            exitedInnerLoop = True
                            break
                        else:
                            # initialize all 3 instances and offer them a path to try, if path does not properly get from A to B, then try next instance, and so on.
                            if firstIteration:
                                initializeInstance1()
                                initializeInstance2()
                                initializeInstance3()
                            isUnsure = True
                            break
            elif isExitChar(userKnowInstance):
                #check if there was a break within the outter loop or inner loop
                sys.exit()
            else:
                print("\ninvalid input, please try again.")
                continue
            if flagDD: # if the user had dimension door, restart the loop because now they should know their instance.
                continue
        while True:
            if(inInstance1):
                firstIteration = False
                # populate a list with the valid map-form string identifiers of the room in given instance
                roomsInInstance1 = ["s","gc", "rc", "bc", "ym", "gm", "bm", "yp", "yd", "gd", "rd", "ru", "bu", "r"]
                abrvSet = set(roomsInInstance1) # transform map-form string list into set for element checks
                stringToObjMap = dict(zip(roomsInInstance1, pointedRoomListInstance1)) # create map
                
                while True:
                    print("\n\n[Shadow Crypt " + bold(red("Red")) + " Instance]\n")
                    for room in pointedRoomListInstance1: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)    
                    while True: # dialogue loop for starting room
                        raw = input("\nWhich of these rooms are you currently in? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\n"+ orange("Enter Room: ")).lower() # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        startingRoomString = roomTerms(normalized) # check to see if valid room term
                        if startingRoomString in abrvSet: # easy element check from set copy of map-form list
                            startingRoom = stringToObjMap.get(startingRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    print("\n\n[Shadow Crypt " + bold(red("Red")) + " Instance]\n")
                    for room in pointedRoomListInstance1: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for destination room
                        raw = input("\nWhich of these rooms are you trying to reach? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\n"+ orange("Enter Room: ")).lower() # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        destinationRoomString = roomTerms(normalized) # check to see if valid room term
                        if destinationRoomString in abrvSet: # easy element check from set copy of map-form list
                            destinationRoom = stringToObjMap.get(destinationRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    path = prioBFS(instance1, startingRoom, destinationRoom) # perform priority BFS, store path as a list
                    print("\nHere is your path from " + str(startingRoom) + " to " + str(destinationRoom) + "\n") # reiterate to the user their chosen rooms
                    printPath(path) # display path to user
                    while True:
                        again = input("\nNeed to get to another room? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                        if(yesNoAssociation(again)):
                            if again in yesSet:
                                break
                            else:
                                print("Closing Program ... Thank you for using Crypt Router!")
                                sys.exit()
                        elif isExitChar(again):
                            sys.exit()
                        else:
                            print("invalid response, try again")
                            continue
            elif(inInstance2):
                firstIteration = False
                # populate a list with the valid map-form string identifiers of the room in given instance
                roomsInInstance2 = ["s","gc", "bc", "gm", "rm", "bm", "yp", "gp", "rp", "yd", "bd", "yu", "ru", "r"]
                abrvSet = set(roomsInInstance2) # transform map-form string list into set for element checks
                stringToObjMap = dict(zip(roomsInInstance2, pointedRoomListInstance2)) # create map
                while True:
                    print("\n\n[Shadow Crypt " + bold(green("Green")) + " Instance]\n")
                    for room in pointedRoomListInstance2: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for starting room
                        raw = input("\nWhich of these rooms are you currently in? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\n"+ orange("Enter Room: ")).lower() # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        startingRoomString = roomTerms(normalized) # check to see if valid room term
                        if startingRoomString in abrvSet: # easy element check from set copy of map-form list
                            startingRoom = stringToObjMap.get(startingRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    print("\n\n[Shadow Crypt " + bold(green("Green")) + " Instance]\n")
                    for room in pointedRoomListInstance2: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for destination room
                        raw = input("\nWhich of these rooms are you trying to reach? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\n"+ orange("Enter Room: ")) # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        destinationRoomString = roomTerms(normalized) # check to see if valid room term
                        if destinationRoomString in abrvSet: # easy element check from set copy of map-form list
                            destinationRoom = stringToObjMap.get(destinationRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    path = prioBFS(instance2, startingRoom, destinationRoom) # perform priority BFS, store path as a list
                    print("\nHere is your path from " + str(startingRoom) + " to " + str(destinationRoom) + "\n") # reiterate to the user their chosen rooms
                    printPath(path) # display path to user
                    while True:
                        again = input("\nNeed to get to another room? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                        if(yesNoAssociation(again)):
                            if again in yesSet:
                                break
                            else:
                                print("Closing Program ... Thank you for using Crypt Router!")
                                sys.exit()
                        elif isExitChar(again):
                            sys.exit()
                        else:
                            print("invalid response, try again")
                            continue
            elif(inInstance3):
                firstIteration = False
                # populate a list with the valid map-form string identifiers of the room in given instance
                roomsInInstance3 = ["s","yc", "rc", "ym", "bm", "gp", "rp", "bp", "gd", "rd", "yu", "gu", "bu", "r", "gc"]
                abrvSet = set(roomsInInstance3) # transform map-form string list into set for element checks
                stringToObjMap = dict(zip(roomsInInstance3, pointedRoomListInstance3)) # create map
                while True:
                    print("\n\n[Shadow Crypt " + bold(blue("Blue")) + " Instance]\n")
                    for room in pointedRoomListInstance3: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for starting room
                        raw = input("\nWhich of these rooms are you currently in? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\n"+ orange("Enter Room: ")) # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        startingRoomString = roomTerms(normalized) # check to see if valid room term
                        if startingRoomString in abrvSet: # easy element check from set copy of map-form list
                            startingRoom = stringToObjMap.get(startingRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    print("\n\n[Shadow Crypt " + bold(blue("Blue")) + " Instance]\n")
                    for room in pointedRoomListInstance3: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for destination room
                        raw = input("\nWhich of these rooms are you trying to reach? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\n"+ orange("Enter Room: ")) # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        destinationRoomString = roomTerms(normalized) # check to see if valid room term
                        if destinationRoomString in abrvSet: # easy element check from set copy of map-form list
                            destinationRoom = stringToObjMap.get(destinationRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    path = prioBFS(instance3, startingRoom, destinationRoom) # perform priority BFS, store path as a list
                    print("\nHere is your path from " + str(startingRoom) + " to " + str(destinationRoom) + "\n") # reiterate to the user their chosen rooms
                    printPath(path) # display path to user
                    while True:
                        again = input("\nNeed to get to another room? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                        if(yesNoAssociation(again)):
                            if again in yesSet:
                                break
                            else:
                                print("Closing Program ... Thank you for using Crypt Router!")
                                sys.exit()
                        elif isExitChar(again):
                            sys.exit()
                        else:
                            print("invalid response, try again")
                            continue  
            elif(isUnsure):
                firstIteration = False
                while isUnsure:
                    print("So let's try instance 1 first!\n")
                    # populate a list with the valid map-form string identifiers of the room in given instance
                    roomsInInstance1 = ["s","gc", "rc", "bc", "ym", "gm", "bm", "yp", "yd", "gd", "rd", "ru", "bu", "r"]
                    abrvSet = set(roomsInInstance1) # transform map-form string list into set for element checks
                    stringToObjMap = dict(zip(roomsInInstance1, pointedRoomListInstance1)) # create map
                    print("\n\n[Shadow Crypt " + bold(red("Red")) + " Instance]\n")
                    for room in pointedRoomListInstance1: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for starting room
                        roomNotFound = False
                        raw = input("\nWhich of these rooms are you currently in? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\nIf you cannot find your room, type 'x'\n"+ orange("Enter Room: ")) # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        startingRoomString = roomTerms(normalized) # check to see if valid room term
                        if startingRoomString in abrvSet: # easy element check from set copy of map-form list
                            startingRoom = stringToObjMap.get(startingRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        if roomNotInTopologyChar(raw):
                            roomNotFound = True
                            break
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    if not roomNotFound:
                        print("\n\n[Shadow Crypt " + bold(red("Red")) + " Instance]\n")
                        for room in pointedRoomListInstance1: # display rooms for user
                            strng = ""
                            roomColor = room.getColor().lower()
                            if roomColor == "yellow":
                                strng = yellow(str(room))
                            elif roomColor == "green":
                                strng = green(str(room))
                            elif roomColor == "red":
                                strng = red(str(room))
                            elif roomColor == "blue":
                                strng = blue(str(room))
                            else:
                                strng = bold(str(room))
                            print(strng)
                        while True: # dialogue loop for destination room
                            raw = input("\nWhich of these rooms are you trying to reach? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\nIf you cannot find your room, type 'x'\n"+ orange("Enter Room: ")) # collect input
                            normalized = raw.strip().lower().replace(" ", "") # normalize input
                            destinationRoomString = roomTerms(normalized) # check to see if valid room term
                            if destinationRoomString in abrvSet: # easy element check from set copy of map-form list
                                destinationRoom = stringToObjMap.get(destinationRoomString) # because room is mapped to string, easy room retrieval
                                break # break dialogue loop, no more need to continue this query
                            elif isExitChar(raw): # check raw input to see if it is the exit character
                                sys.exit()
                            elif roomNotInTopologyChar(raw):
                                roomNotFound = True
                                break
                            else:
                                print("invalid room, please try again\n") # inform the user of the error of their ways
                                continue # restart the while loop
                        if not roomNotFound:
                            path = prioBFS(instance1, startingRoom, destinationRoom) # perform priority BFS, store path as a list
                            print("\nHere is your path from " + str(startingRoom) + " to " + str(destinationRoom) + "\n") # reiterate to the user their chosen rooms
                            printPath(path) # display path to user
                            while True:
                                workInput = input("\nDid that work? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                                if yesNoAssociation(workInput):
                                    if workInput in yesSet:
                                        foundInstance = True
                                        while True:
                                            again = input("\nNeed to get to another room? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                                            if(yesNoAssociation(again)):
                                                if again in yesSet:
                                                    break
                                                else:
                                                    print("Closing Program ... Thank you for using Crypt Router!")
                                                    sys.exit()
                                            elif isExitChar(again):
                                                sys.exit()
                                            else:
                                                print("invalid response, try again")
                                                continue
                                        isUnsure = False
                                        inInstance1 = True
                                        break
                                    else:
                                        break
                                elif isExitChar(workInput):
                                    sys.exit()
                                else:
                                    print("\ninvalid response, please try again\n")
                                    continue
                    if foundInstance:
                        break
                    # out of precaution, set variables in scope to none
                    stringToObjMap = None
                    abrvSet = None
                    print("\nnext, let's try instance 2!")
                    # populate a list with the valid map-form string identifiers of the room in given instance
                    roomsInInstance2 = ["s","gc", "bc", "gm", "rm", "bm", "yp", "gp", "rp", "yd", "bd", "yu", "ru", "r"]
                    abrvSet = set(roomsInInstance2) # transform map-form string list into set for element checks
                    stringToObjMap = dict(zip(roomsInInstance2, pointedRoomListInstance2)) # create map
                    print("\n\n[Shadow Crypt " + bold(green("Green")) + " Instance]\n")
                    for room in pointedRoomListInstance2: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for starting room
                        roomNotFound = False
                        raw = input("\nWhich of these rooms are you currently in? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\nIf you cannot find your room, type 'x'\n"+ orange("Enter Room: ")) # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        startingRoomString = roomTerms(normalized) # check to see if valid room term
                        if startingRoomString in abrvSet: # easy element check from set copy of map-form list
                            startingRoom = stringToObjMap.get(startingRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        elif roomNotInTopologyChar(raw):
                            roomNotFound = True
                            break
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    if not roomNotFound:
                        print("\n\n[Shadow Crypt " + bold(green("Green")) + " Instance]\n")
                        for room in pointedRoomListInstance2: # display rooms for user
                            strng = ""
                            roomColor = room.getColor().lower()
                            if roomColor == "yellow":
                                strng = yellow(str(room))
                            elif roomColor == "green":
                                strng = green(str(room))
                            elif roomColor == "red":
                                strng = red(str(room))
                            elif roomColor == "blue":
                                strng = blue(str(room))
                            else:
                                strng = bold(str(room))
                            print(strng)
                        while True: # dialogue loop for destination room
                            raw = input("\nWhich of these rooms are you trying to reach? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\nIf you cannot find your room, type 'x'\n"+ orange("Enter Room: ")) # collect input
                            normalized = raw.strip().lower().replace(" ", "") # normalize input
                            destinationRoomString = roomTerms(normalized) # check to see if valid room term
                            if destinationRoomString in abrvSet: # easy element check from set copy of map-form list
                                destinationRoom = stringToObjMap.get(destinationRoomString) # because room is mapped to string, easy room retrieval
                                break # break dialogue loop, no more need to continue this query
                            elif isExitChar(raw): # check raw input to see if it is the exit character
                                sys.exit()
                            elif roomNotInTopologyChar(raw):
                                roomNotFound = True
                                break
                            else:
                                print("invalid room, please try again\n") # inform the user of the error of their ways
                                continue # restart the while loop
                        if not roomNotFound:
                            path = prioBFS(instance2, startingRoom, destinationRoom) # perform priority BFS, store path as a list
                            print("\nHere is your path from " + str(startingRoom) + " to " + str(destinationRoom) + "\n") # reiterate to the user their chosen rooms
                            printPath(path) # display path to user
                            while True:
                                workInput = input("\nDid that work? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                                if yesNoAssociation(workInput):
                                    if workInput in yesSet:
                                        foundInstance = True
                                        while True:
                                            again = input("\nNeed to get to another room? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                                            if(yesNoAssociation(again)):
                                                if again in yesSet:
                                                    break
                                                else:
                                                    print("Closing Program ... Thank you for using Crypt Router!")
                                                    sys.exit()
                                            elif isExitChar(again):
                                                sys.exit()
                                            else:
                                                print("invalid response, try again")
                                                continue
                                        isUnsure = False
                                        inInstance2 = True
                                        break
                                    else:
                                        break
                                elif isExitChar(workInput):
                                    sys.exit()
                                else:
                                    print("\ninvalid response, please try again\n")
                                    continue
                    if foundInstance:
                        break
                    # out of precaution, set variables in scope to none
                    stringToObjMap = None
                    abrvSet = None
                    print("\nThat's Okay! last but not least, let's try instance 3!")
                    # populate a list with the valid map-form string identifiers of the room in given instance
                    roomsInInstance3 = ["s","yc", "rc", "ym", "bm", "gp", "rp", "bp", "gd", "rd", "yu", "gu", "bu", "r", "gc"]
                    abrvSet = set(roomsInInstance3) # transform map-form string list into set for element checks
                    stringToObjMap = dict(zip(roomsInInstance3, pointedRoomListInstance3)) # create map
                    print("\n\n[Shadow Crypt " + bold(blue("Blue")) + " Instance]\n")
                    for room in pointedRoomListInstance3: # display rooms for user
                        strng = ""
                        roomColor = room.getColor().lower()
                        if roomColor == "yellow":
                            strng = yellow(str(room))
                        elif roomColor == "green":
                            strng = green(str(room))
                        elif roomColor == "red":
                            strng = red(str(room))
                        elif roomColor == "blue":
                            strng = blue(str(room))
                        else:
                            strng = bold(str(room))
                        print(strng)
                    while True: # dialogue loop for starting room
                        roomNotFound = False
                        raw = input("\nWhich of these rooms are you currently in? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\nIf you cannot find your room, type 'x'\n"+ orange("Enter Room: ")) # collect input
                        normalized = raw.strip().lower().replace(" ", "") # normalize input
                        startingRoomString = roomTerms(normalized) # check to see if valid room term
                        if startingRoomString in abrvSet: # easy element check from set copy of map-form list
                            startingRoom = stringToObjMap.get(startingRoomString) # because room is mapped to string, easy room retrieval
                            break # break dialogue loop, no more need to continue this query
                        elif isExitChar(raw): # check raw input to see if it is the exit character
                            sys.exit()
                        elif roomNotInTopologyChar(raw):
                            roomNotFound = True
                            isUnsure = False
                            wasUnsure = True
                            break
                        else:
                            print("invalid room, please try again\n") # inform the user of the error of their ways
                            continue # restart the while loop
                    if not roomNotFound:
                        print("\n\n[Shadow Crypt " + bold(blue("Blue")) + " Instance]\n")
                        for room in pointedRoomListInstance3: # display rooms for user
                            strng = ""
                            roomColor = room.getColor().lower()
                            if roomColor == "yellow":
                                strng = yellow(str(room))
                            elif roomColor == "green":
                                strng = green(str(room))
                            elif roomColor == "red":
                                strng = red(str(room))
                            elif roomColor == "blue":
                                strng = blue(str(room))
                            else:
                                strng = bold(str(room))
                            print(strng)
                        while True: # dialogue loop for destination room
                            raw = input("\nWhich of these rooms are you trying to reach? (or press enter to exit)\nValid inputs: i.e. gc, rc, yellow maze, etc. s/start for starting room, r/ramp for final room <case insensitive>\nIf you cannot find your room, type 'x'\n"+ orange("Enter Room: ")) # collect input
                            normalized = raw.strip().lower().replace(" ", "") # normalize input
                            destinationRoomString = roomTerms(normalized) # check to see if valid room term
                            if destinationRoomString in abrvSet: # easy element check from set copy of map-form list
                                destinationRoom = stringToObjMap.get(destinationRoomString) # because room is mapped to string, easy room retrieval
                                break # break dialogue loop, no more need to continue this query
                            elif isExitChar(raw): # check raw input to see if it is the exit character
                                sys.exit()
                            elif roomNotInTopologyChar(raw):
                                roomNotFound = True
                                isUnsure = False
                                wasUnsure = True
                                break
                            else:
                                print("invalid room, please try again\n") # inform the user of the error of their ways
                                continue # restart the while loop
                        if not roomNotFound:
                            path = prioBFS(instance3, startingRoom, destinationRoom) # perform priority BFS, store path as a list
                            print("\nHere is your path from " + str(startingRoom) + " to " + str(destinationRoom) + "\n") # reiterate to the user their chosen rooms
                            printPath(path) # display path to user
                            while True:
                                workInput = input("\nDid that work? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                                if yesNoAssociation(workInput):
                                    if workInput in yesSet:
                                        foundInstance = True
                                        while True:
                                            again = input("\nNeed to get to another room? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                                            if(yesNoAssociation(again)):
                                                if again in yesSet:
                                                    break
                                                else:
                                                    print("Closing Program ... Thank you for using Crypt Router!")
                                                    sys.exit()
                                            elif isExitChar(again):
                                                sys.exit()
                                            else:
                                                print("invalid response, try again")
                                                continue
                                        isUnsure = False
                                        inInstance3 = True
                                        break
                                    else:
                                        isUnsure = False
                                        wasUnsure = True
                                        break
                                elif isExitChar(workInput):
                                    sys.exit()
                                else:
                                    print("\ninvalid response, please try again\n")
                                    continue
            break
        if wasUnsure:
            print("\nI'm sorry that didn't work.")
            while True:
                restartQuery = input("\nWould you like to restart the program and try again? type 'yes' or 'y' if so & 'no' or 'n' if not, or press enter to exit\n"+ orange("Enter Response: ")).lower()
                if yesNoAssociation(restartQuery):
                    if(restartQuery in yesSet):
                        break
                    else:
                        sys.exit()
                elif isExitChar(restartQuery):
                    sys.exit()
                else:
                    print("\ninvalid input, please try again.")
                    continue
        print("\n\n")
        break
"""

ADDITIONAL DOCUMENTATION
 instances in shadow crypt can vary by having set/immutable pointers to different rooms given certain directions. 
 instances have will have a total of 14 distinct rooms

 Instance #1 has the rooms as follows:

 - Starting Room

 - Green Columns
 - Red Columns
 - Blue Columns
 - Yellow Maze
 - Green Maze
 - Blue Maze
 - Yellow Puzzle
 - Yellow Dais
 - Green Dais
 - Red Dais
 - Red Underwater
 - Blue Underwater

 - Ramp Room

 Instance #2 has the rooms as follows:

 - Starting Room

 - Green Columns 
 - Blue Columns
 - Green Maze
 - Red Maze
 - Blue Maze
 - Yellow Puzzle
 - Green Puzzle
 - Red Puzzle
 - Yellow Dais
 - Blue Dais
 - Yellow Underwater
 - Red Underwater

 - Ramp Room

 Instance #3 has the rooms as follows: (Wiki Diagram indicates 13)

 - Starting Room

 - Yellow Columns 
 - Red Columns 
 - Yellow Maze 
 - Blue Maze 
 - Green Puzzle 
 - Red Puzzle 
 - Blue Puzzle 
 - Green Dais 
 - Red Dais 
 - Yellow Underwater 
 - Green Underwater 
 - Blue Underwater 

 - Green Columns (not intended?)

 - Ramp Room

PROTO instance population -- didnt work because each instance is unique and lacks any computer reproduceable pattern.

# Columns on 1, 6, 11, and 16 ( n % 5 = 1)
# Mazes on 2, 7, 12, and 17 ( n % 5 = 2)
# Puzzles on 3, 8, 13, and 18 ( n % 5 = 3)
# Dais on 4, 9, 14, and 19 ( n % 5 = 4)
# Underwater on 5, 10, 15, and 20 ( n % 5 = 0)
# Yellow Ranges from 1 - 5
# Green Ranges from 6 - 10
# Red Ranges from 11 - 15
# Blue Ranges from 16 - 20

colorList = ["Yellow", "Green", "Red", "Blue"]
structureList = ["Columns", "Maze", "Puzzle", "Dais", "Underwater"]

unpointedGeneralRoomList  = [Room("Colorless", "Start")] # starting room = index 0

for color in colorList:
    for structure in structureList:
        unpointedGeneralRoomList.append(Room(color, structure))
"""