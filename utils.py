"""
INSTANCE ONE SETUP
"""
import heapq
import itertools

from room import *
from instance import Instance

global pointedRoomListInstance1
global pointedRoomListInstance2
global pointedRoomListInstance3

def initializeInstance1():
    global instance1
    global pointedRoomListInstance1
    pointedRoomListInstance1 = [Room("Colorless", "Start")]
    # add the rooms in instance one initially to a list so that they can be indexed [exhaustively, theres no pattern just how it is]
    pointedRoomListInstance1.append(Room("Green", "Columns"))  # INDEX 1
    pointedRoomListInstance1.append(Room("Red", "Columns"))  # INDEX 2
    pointedRoomListInstance1.append(Room("Blue", "Columns"))  # INDEX 3
    pointedRoomListInstance1.append(Room("Yellow", "Maze"))  # INDEX 4
    pointedRoomListInstance1.append(Room("Green", "Maze"))  # INDEX 5
    pointedRoomListInstance1.append(Room("Blue", "Maze"))  # INDEX 6
    pointedRoomListInstance1.append(Room("Yellow", "Puzzle"))  # INDEX 7
    pointedRoomListInstance1.append(Room("Yellow", "Dais"))  # INDEX 8
    pointedRoomListInstance1.append(Room("Green", "Dais"))  # INDEX 9
    pointedRoomListInstance1.append(Room("Red", "Dais"))  # INDEX 10
    pointedRoomListInstance1.append(Room("Red", "Underwater"))  # INDEX 11
    pointedRoomListInstance1.append(Room("Blue", "Underwater"))  # INDEX 12
    pointedRoomListInstance1.append(Room("Colorless", "Ramp"))  # INDEX 13

    # pointers for starting room ( edges ) INDEX 0
    pointedRoomListInstance1[0].setNorthPointer(pointedRoomListInstance1[0])  # north points to Starting room
    pointedRoomListInstance1[0].setEastPointer(pointedRoomListInstance1[2])  # east points to Red Columns room
    pointedRoomListInstance1[0].setSouthPointer(pointedRoomListInstance1[4])  # south points to Yellow Maze room
    pointedRoomListInstance1[0].setWestPointer(pointedRoomListInstance1[1])  # west points to Green Columns room

    # pointers for Green Columns room ( edges ) INDEX 1
    pointedRoomListInstance1[1].setNorthPointer(pointedRoomListInstance1[5])  # north points to Green Maze room
    pointedRoomListInstance1[1].setEastPointer(pointedRoomListInstance1[1])  # east points to Green Columns room
    pointedRoomListInstance1[1].setSouthPointer(pointedRoomListInstance1[1])  # south points to Green Columns room
    pointedRoomListInstance1[1].setWestPointer(pointedRoomListInstance1[4])  # west points to Yellow Maze room

    # pointers for Red Columns room ( edges ) INDEX 2
    pointedRoomListInstance1[2].setNorthPointer(pointedRoomListInstance1[3])  # north points to Blue Columns
    pointedRoomListInstance1[2].setEastPointer(pointedRoomListInstance1[6])  # east points to Blue Maze room
    pointedRoomListInstance1[2].setSouthPointer(pointedRoomListInstance1[11])  # south points to Red Underwater room
    pointedRoomListInstance1[2].setWestPointer(pointedRoomListInstance1[12])  # west points to Blue Underwater room

    # pointers for Blue Columns room ( edges ) INDEX 3
    pointedRoomListInstance1[3].setNorthPointer(pointedRoomListInstance1[9])  # north points to Green Dais room
    pointedRoomListInstance1[3].setEastPointer(pointedRoomListInstance1[7])  # east points to Yellow Puzzle room
    pointedRoomListInstance1[3].setSouthPointer(pointedRoomListInstance1[10])  # south points to Red Dais room
    pointedRoomListInstance1[3].setWestPointer(pointedRoomListInstance1[11])  # west points to Red Underwater room

    # pointers for Yellow Maze room ( edges ) INDEX 4
    pointedRoomListInstance1[4].setNorthPointer(pointedRoomListInstance1[5])  # north points to Green Maze room
    pointedRoomListInstance1[4].setEastPointer(pointedRoomListInstance1[8])  # east points to Yellow Dais room
    pointedRoomListInstance1[4].setSouthPointer(pointedRoomListInstance1[6])  # south points to Blue Maze room
    pointedRoomListInstance1[4].setWestPointer(pointedRoomListInstance1[0])  # west points to Starting room

    # pointers for Green Maze room ( edges ) INDEX 5
    pointedRoomListInstance1[5].setNorthPointer(pointedRoomListInstance1[2])  # north points to Red Columns room
    pointedRoomListInstance1[5].setEastPointer(pointedRoomListInstance1[0])  # east points to Starting room
    pointedRoomListInstance1[5].setSouthPointer(pointedRoomListInstance1[12])  # south points to Blue Underwater room
    pointedRoomListInstance1[5].setWestPointer(pointedRoomListInstance1[9])  # west points to Green Dais room

    # pointers for Blue Maze room ( edges ) INDEX 6
    pointedRoomListInstance1[6].setNorthPointer(pointedRoomListInstance1[2])  # north points to Red Columns Room
    pointedRoomListInstance1[6].setEastPointer(pointedRoomListInstance1[10])  # east points to Red Dais room
    pointedRoomListInstance1[6].setSouthPointer(pointedRoomListInstance1[7])  # south points to Yellow Puzzle room
    pointedRoomListInstance1[6].setWestPointer(pointedRoomListInstance1[9])  # west points to Green Dais room

    # pointers for Yellow Puzzle room ( edges ) INDEX 7
    pointedRoomListInstance1[7].setNorthPointer(pointedRoomListInstance1[4])  # north points to Yellow Maze room
    pointedRoomListInstance1[7].setEastPointer(pointedRoomListInstance1[10])  # east points to Red Dais room
    pointedRoomListInstance1[7].setSouthPointer(pointedRoomListInstance1[12])  # south points to Blue Underwater room
    pointedRoomListInstance1[7].setWestPointer(pointedRoomListInstance1[6])  # west points to Blue Maze room

    # pointers for Yellow Dais room ( edges ) INDEX 8
    pointedRoomListInstance1[8].setNorthPointer(pointedRoomListInstance1[11])  # north points to Red Underwater room
    pointedRoomListInstance1[8].setEastPointer(pointedRoomListInstance1[1])  # east points to Green Columns room
    pointedRoomListInstance1[8].setSouthPointer(pointedRoomListInstance1[3])  # south points to Blue Columns room
    pointedRoomListInstance1[8].setWestPointer(pointedRoomListInstance1[10])  # west points to Red Dais room

    # pointers for Green Dais room ( edges ) INDEX 9
    pointedRoomListInstance1[9].setNorthPointer(pointedRoomListInstance1[5])  # north points to Green Maze room
    pointedRoomListInstance1[9].setEastPointer(pointedRoomListInstance1[3])  # east points to Blue Columns room
    pointedRoomListInstance1[9].setSouthPointer(pointedRoomListInstance1[6])  # south points to Blue Maze room
    pointedRoomListInstance1[9].setWestPointer(pointedRoomListInstance1[7])  # west points to Yellow Puzzle room

    # pointers for Red Dais room ( edges ) INDEX 10
    pointedRoomListInstance1[10].setNorthPointer(pointedRoomListInstance1[4])  # north points to Yellow Maze room
    pointedRoomListInstance1[10].setEastPointer(pointedRoomListInstance1[11])  # east points to Red Underwater room
    pointedRoomListInstance1[10].setSouthPointer(pointedRoomListInstance1[12])  # south points to Blue Underwater room
    pointedRoomListInstance1[10].setWestPointer(pointedRoomListInstance1[13])  # west points to Ramp room

    # pointers for Red Underwater room ( edges ) INDEX 11
    pointedRoomListInstance1[11].setNorthPointer(pointedRoomListInstance1[2])  # north points to Red Columns room
    pointedRoomListInstance1[11].setEastPointer(pointedRoomListInstance1[7])  # east points to Yellow Puzzle room
    pointedRoomListInstance1[11].setSouthPointer(pointedRoomListInstance1[3])  # south points to Blue Columns room
    pointedRoomListInstance1[11].setWestPointer(pointedRoomListInstance1[8])  # west points to Yellow Dais room

    # pointers for Blue Underwater room ( edges ) INDEX 12
    pointedRoomListInstance1[12].setNorthPointer(pointedRoomListInstance1[8])  # north points to Yellow Dais room
    pointedRoomListInstance1[12].setEastPointer(pointedRoomListInstance1[0])  # east points to Start room
    pointedRoomListInstance1[12].setSouthPointer(pointedRoomListInstance1[1])  # south points to Green Columns room
    pointedRoomListInstance1[12].setWestPointer(pointedRoomListInstance1[5])  # west points to Green Maze room

    pointedRoomListInstance1[13].setEastPointer(
        pointedRoomListInstance1[8])  # Ramp has only one pointer pointing to Yellow Dais

    pointedRoomSetInstance1 = set(pointedRoomListInstance1)  # Convert List to Set for purposes of the instance class
    instance1 = Instance(pointedRoomSetInstance1)  # instantiate instance.


"""
INSTANCE 2 SETUP
"""


def initializeInstance2():
    global instance2
    global pointedRoomListInstance2
    pointedRoomListInstance2 = [Room("Colorless", "Start")]
    pointedRoomListInstance2.append(Room("Green", "Columns"))  # INDEX 1
    pointedRoomListInstance2.append(Room("Blue", "Columns"))  # INDEX 2
    pointedRoomListInstance2.append(Room("Green", "Maze"))  # INDEX 3
    pointedRoomListInstance2.append(Room("Red", "Maze"))  # INDEX 4
    pointedRoomListInstance2.append(Room("Blue", "Maze"))  # INDEX 5
    pointedRoomListInstance2.append(Room("Yellow", "Puzzle"))  # INDEX 6
    pointedRoomListInstance2.append(Room("Green", "Puzzle"))  # INDEX 7
    pointedRoomListInstance2.append(Room("Red", "Puzzle"))  # INDEX 8
    pointedRoomListInstance2.append(Room("Yellow", "Dais"))  # INDEX 9
    pointedRoomListInstance2.append(Room("Blue", "Dais"))  # INDEX 10
    pointedRoomListInstance2.append(Room("Yellow", "Underwater"))  # INDEX 11
    pointedRoomListInstance2.append(Room("Red", "Underwater"))  # INDEX 12
    pointedRoomListInstance2.append(Room("Colorless", "Ramp"))  # INDEX 13

    # pointers for starting room ( edges ) INDEX 0
    pointedRoomListInstance2[0].setNorthPointer(pointedRoomListInstance2[4])  # north points to Red Maze room
    pointedRoomListInstance2[0].setEastPointer(pointedRoomListInstance2[1])  # east points to Green Columns room
    pointedRoomListInstance2[0].setSouthPointer(pointedRoomListInstance2[8])  # south points to Red Puzzle room
    pointedRoomListInstance2[0].setWestPointer(pointedRoomListInstance2[2])  # west points to Blue Columns room

    # pointers for Green Columns room ( edges ) INDEX 1
    pointedRoomListInstance2[1].setNorthPointer(pointedRoomListInstance2[2])  # north points to Blue Columns room
    pointedRoomListInstance2[1].setEastPointer(pointedRoomListInstance2[3])  # east points to Green Maze room
    pointedRoomListInstance2[1].setSouthPointer(pointedRoomListInstance2[1])  # south points to Green Columns room
    pointedRoomListInstance2[1].setWestPointer(pointedRoomListInstance2[9])  # west points to Yellow Dais room

    # pointers for Blue Columns room ( edges ) INDEX 2
    pointedRoomListInstance2[2].setNorthPointer(pointedRoomListInstance2[3])  # north points to Green Maze room
    pointedRoomListInstance2[2].setEastPointer(pointedRoomListInstance2[12])  # east points to Red Underwater room
    pointedRoomListInstance2[2].setSouthPointer(pointedRoomListInstance2[6])  # south points to Yellow Puzzle room
    pointedRoomListInstance2[2].setWestPointer(pointedRoomListInstance2[1])  # west points to Green Columns room

    # pointers for Green Maze room ( edges ) INDEX 3
    pointedRoomListInstance2[3].setNorthPointer(pointedRoomListInstance2[11])  # north points to Yellow Underwater room
    pointedRoomListInstance2[3].setEastPointer(pointedRoomListInstance2[4])  # east points to Red Maze room
    pointedRoomListInstance2[3].setSouthPointer(pointedRoomListInstance2[10])  # south points to Blue Dais room
    pointedRoomListInstance2[3].setWestPointer(pointedRoomListInstance2[12])  # west points to Red Underwater room

    # pointers for Red Maze room ( edges ) INDEX 4
    pointedRoomListInstance2[4].setNorthPointer(pointedRoomListInstance2[4])  # north points to Red Maze room
    pointedRoomListInstance2[4].setEastPointer(pointedRoomListInstance2[9])  # east points to Yellow Dais room
    pointedRoomListInstance2[4].setSouthPointer(pointedRoomListInstance2[2])  # south points to Blue Columns room
    pointedRoomListInstance2[4].setWestPointer(pointedRoomListInstance2[12])  # west points to Red Underwater room

    # pointers for Blue Maze room ( edges ) INDEX 5
    pointedRoomListInstance2[5].setNorthPointer(pointedRoomListInstance2[12])  # north points to Red Underwater room
    pointedRoomListInstance2[5].setEastPointer(pointedRoomListInstance2[9])  # east points to Yellow Dais room
    pointedRoomListInstance2[5].setSouthPointer(pointedRoomListInstance2[3])  # south points to Green Maze room
    pointedRoomListInstance2[5].setWestPointer(pointedRoomListInstance2[10])  # west points to Blue Dais room

    # pointers for Yellow Puzzle room ( edges ) INDEX 6
    pointedRoomListInstance2[6].setNorthPointer(pointedRoomListInstance2[7])  # north points to Green Puzzle Room
    pointedRoomListInstance2[6].setEastPointer(pointedRoomListInstance2[5])  # east points to Blue Maze room
    pointedRoomListInstance2[6].setSouthPointer(pointedRoomListInstance2[6])  # south points to Yellow Puzzle room
    pointedRoomListInstance2[6].setWestPointer(pointedRoomListInstance2[0])  # west points to Starting room

    # pointers for Green Puzzle room ( edges ) INDEX 7
    pointedRoomListInstance2[7].setNorthPointer(pointedRoomListInstance2[10])  # north points to Blue Dais room
    pointedRoomListInstance2[7].setEastPointer(pointedRoomListInstance2[6])  # east points to Yellow Puzzle room
    pointedRoomListInstance2[7].setSouthPointer(pointedRoomListInstance2[7])  # south points to Green Puzzle room
    pointedRoomListInstance2[7].setWestPointer(pointedRoomListInstance2[4])  # west points to Red Maze room

    # pointers for Red Puzzle room ( edges ) INDEX 8
    pointedRoomListInstance2[8].setNorthPointer(pointedRoomListInstance2[7])  # north points to Green Puzzle room
    pointedRoomListInstance2[8].setEastPointer(pointedRoomListInstance2[11])  # east points to Yellow Underwater room
    pointedRoomListInstance2[8].setSouthPointer(pointedRoomListInstance2[8])  # south points to Red Puzzle room
    pointedRoomListInstance2[8].setWestPointer(pointedRoomListInstance2[9])  # west points to Yellow Dais room

    # pointers for Yellow Dais room ( edges ) INDEX 9
    pointedRoomListInstance2[9].setNorthPointer(pointedRoomListInstance2[5])  # north points to Blue Maze room
    pointedRoomListInstance2[9].setEastPointer(pointedRoomListInstance2[0])  # east points to Starting room
    pointedRoomListInstance2[9].setSouthPointer(pointedRoomListInstance2[8])  # south points to Red Puzzle room
    pointedRoomListInstance2[9].setWestPointer(pointedRoomListInstance2[7])  # west points to Green Puzzle room

    # pointers for Blue Dais room ( edges ) INDEX 10
    pointedRoomListInstance2[10].setNorthPointer(pointedRoomListInstance2[2])  # north points to Blue Columns room
    pointedRoomListInstance2[10].setEastPointer(pointedRoomListInstance2[11])  # east points to Yellow Underwater room
    pointedRoomListInstance2[10].setSouthPointer(pointedRoomListInstance2[11])  # south points to Yellow Underwater room
    pointedRoomListInstance2[10].setWestPointer(pointedRoomListInstance2[0])  # west points to Starting room

    # pointers for Yellow Underwater room ( edges ) INDEX 11
    pointedRoomListInstance2[11].setNorthPointer(pointedRoomListInstance2[0])  # north points to Starting room
    pointedRoomListInstance2[11].setEastPointer(pointedRoomListInstance2[3])  # east points to Green Maze room
    pointedRoomListInstance2[11].setSouthPointer(pointedRoomListInstance2[10])  # south points to Blue Dais room
    pointedRoomListInstance2[11].setWestPointer(pointedRoomListInstance2[13])  # west points to Ramp room

    # pointers for Red Underwater room ( edges ) INDEX 12
    pointedRoomListInstance2[12].setNorthPointer(pointedRoomListInstance2[8])  # north points to Red Puzzle room
    pointedRoomListInstance2[12].setEastPointer(pointedRoomListInstance2[5])  # east points to Blue Maze room
    pointedRoomListInstance2[12].setSouthPointer(pointedRoomListInstance2[9])  # south points to Yellow Dais room
    pointedRoomListInstance2[12].setWestPointer(pointedRoomListInstance2[5])  # west points to Blue Maze room

    pointedRoomListInstance2[13].setEastPointer(
        pointedRoomListInstance2[6])  # Ramp has only one pointer pointing to Yellow Puzzle room

    pointedRoomSetInstance2 = set(pointedRoomListInstance2)  # Convert List to Set for purposes of the instance class
    instance2 = Instance(pointedRoomSetInstance2)  # instantiate instance.


"""
INSTANCE 3 SETUP
"""


def initializeInstance3():
    global instance3
    global pointedRoomListInstance3
    pointedRoomListInstance3 = [Room("Colorless", "Start")]
    pointedRoomListInstance3.append(Room("Yellow", "Columns"))  # INDEX 1
    pointedRoomListInstance3.append(Room("Red", "Columns"))  # INDEX 2
    pointedRoomListInstance3.append(Room("Yellow", "Maze"))  # INDEX 3
    pointedRoomListInstance3.append(Room("Blue", "Maze"))  # INDEX 4
    pointedRoomListInstance3.append(Room("Green", "Puzzle"))  # INDEX 5
    pointedRoomListInstance3.append(Room("Red", "Puzzle"))  # INDEX 6
    pointedRoomListInstance3.append(Room("Blue", "Puzzle"))  # INDEX 7
    pointedRoomListInstance3.append(Room("Green", "Dais"))  # INDEX 8
    pointedRoomListInstance3.append(Room("Red", "Dais"))  # INDEX 9
    pointedRoomListInstance3.append(Room("Yellow", "Underwater"))  # INDEX 10
    pointedRoomListInstance3.append(Room("Green", "Underwater"))  # INDEX 11
    pointedRoomListInstance3.append(Room("Blue", "Underwater"))  # INDEX 12
    pointedRoomListInstance3.append(Room("Colorless", "Ramp"))  # INDEX 13
    pointedRoomListInstance3.append(Room("Green", "Columns"))  # INDEX 14

    # pointers for starting room  ( edges ) INDEX 0
    pointedRoomListInstance3[0].setNorthPointer(pointedRoomListInstance3[11])  # north points to Green Underwater room
    pointedRoomListInstance3[0].setEastPointer(pointedRoomListInstance3[7])  # east points to Blue Puzzle room
    pointedRoomListInstance3[0].setSouthPointer(pointedRoomListInstance3[6])  # south points to Red Puzzle room
    pointedRoomListInstance3[0].setWestPointer(pointedRoomListInstance3[10])  # west points to Yellow Underwater room

    # pointers for Yellow Columns room ( edges ) INDEX 1
    pointedRoomListInstance3[1].setNorthPointer(pointedRoomListInstance3[3])  # north points to Yellow Maze room
    pointedRoomListInstance3[1].setEastPointer(pointedRoomListInstance3[0])  # east points to Starting room
    pointedRoomListInstance3[1].setSouthPointer(pointedRoomListInstance3[1])  # south points to Yellow Columns room
    pointedRoomListInstance3[1].setWestPointer(pointedRoomListInstance3[10])  # west points to Yellow Underwater room

    # pointers for Red Columns room ( edges ) INDEX 2
    pointedRoomListInstance3[2].setNorthPointer(pointedRoomListInstance3[0])  # north points to Starting room
    pointedRoomListInstance3[2].setEastPointer(pointedRoomListInstance3[5])  # east points to Green Puzzle room
    pointedRoomListInstance3[2].setSouthPointer(pointedRoomListInstance3[3])  # south points to Yellow Maze room
    pointedRoomListInstance3[2].setWestPointer(pointedRoomListInstance3[4])  # west points to Blue Maze room

    # pointers for Yellow Maze room ( edges ) INDEX 3
    pointedRoomListInstance3[3].setNorthPointer(pointedRoomListInstance3[11])  # north points to Green Underwater room
    pointedRoomListInstance3[3].setEastPointer(pointedRoomListInstance3[6])  # east points to Red Puzzle room
    pointedRoomListInstance3[3].setSouthPointer(pointedRoomListInstance3[0])  # south points to Starting room
    pointedRoomListInstance3[3].setWestPointer(pointedRoomListInstance3[9])  # west points to Red Dais room

    # pointers for Blue Maze room ( edges ) INDEX 4
    pointedRoomListInstance3[4].setNorthPointer(pointedRoomListInstance3[8])  # north points to Green Dais room
    pointedRoomListInstance3[4].setEastPointer(pointedRoomListInstance3[2])  # east points to Red Columns room
    pointedRoomListInstance3[4].setSouthPointer(pointedRoomListInstance3[0])  # south points to Starting room
    pointedRoomListInstance3[4].setWestPointer(pointedRoomListInstance3[7])  # west points to Blue Puzzle room

    # pointers for Green Puzzle room ( edges ) INDEX 5
    pointedRoomListInstance3[5].setNorthPointer(pointedRoomListInstance3[8])  # north points to Green Dais room
    pointedRoomListInstance3[5].setEastPointer(pointedRoomListInstance3[13])  # east points to Ramp room
    pointedRoomListInstance3[5].setSouthPointer(pointedRoomListInstance3[1])  # south points to Yellow Columns room
    pointedRoomListInstance3[5].setWestPointer(pointedRoomListInstance3[7])  # west points to Blue Puzzle room

    # pointers for Red Puzzle room ( edges ) INDEX 6
    pointedRoomListInstance3[6].setNorthPointer(pointedRoomListInstance3[8])  # north points to Green Dais room
    pointedRoomListInstance3[6].setEastPointer(pointedRoomListInstance3[1])  # east points to Yellow Columns room
    pointedRoomListInstance3[6].setSouthPointer(pointedRoomListInstance3[12])  # south points to Blue Underwater room
    pointedRoomListInstance3[6].setWestPointer(pointedRoomListInstance3[2])  # west points to Red Columns room

    # pointers for Blue Puzzle room ( edges ) INDEX 7
    pointedRoomListInstance3[7].setNorthPointer(pointedRoomListInstance3[2])  # north points to Red Columns room
    pointedRoomListInstance3[7].setEastPointer(pointedRoomListInstance3[9])  # east points to Red Dais room
    pointedRoomListInstance3[7].setSouthPointer(pointedRoomListInstance3[3])  # south points to Yellow Maze room
    pointedRoomListInstance3[7].setWestPointer(pointedRoomListInstance3[12])  # west points to Blue Underwater room

    # pointers for Green Dais room ( edges ) INDEX 8
    pointedRoomListInstance3[8].setNorthPointer(pointedRoomListInstance3[10])  # north points to Yellow Underwater room
    pointedRoomListInstance3[8].setEastPointer(pointedRoomListInstance3[11])  # east points to Green Underwater room
    pointedRoomListInstance3[8].setSouthPointer(pointedRoomListInstance3[4])  # south points to Blue Maze room
    pointedRoomListInstance3[8].setWestPointer(pointedRoomListInstance3[6])  # west points to Red Puzzle room

    # pointers for Red Dais room ( edges ) INDEX 9
    pointedRoomListInstance3[9].setNorthPointer(pointedRoomListInstance3[10])  # north points to Yellow Underwater room
    pointedRoomListInstance3[9].setEastPointer(pointedRoomListInstance3[5])  # east points to Green Puzzle room
    pointedRoomListInstance3[9].setSouthPointer(pointedRoomListInstance3[6])  # south points to Red Puzzle room
    pointedRoomListInstance3[9].setWestPointer(pointedRoomListInstance3[12])  # west points to Blue Underwater room

    # pointers for Yellow Underwater room ( edges ) INDEX 10
    pointedRoomListInstance3[10].setNorthPointer(pointedRoomListInstance3[1])  # north points to Yellow Columns room
    pointedRoomListInstance3[10].setEastPointer(pointedRoomListInstance3[2])  # east points to Red Columns room
    pointedRoomListInstance3[10].setSouthPointer(pointedRoomListInstance3[4])  # south points to Blue Maze room
    pointedRoomListInstance3[10].setWestPointer(pointedRoomListInstance3[8])  # west points to Green Dais room

    # pointers for Green Underwater room ( edges ) INDEX 11
    pointedRoomListInstance3[11].setNorthPointer(pointedRoomListInstance3[11])  # north points to Green Underwater room
    pointedRoomListInstance3[11].setEastPointer(pointedRoomListInstance3[3])  # east points to Yellow Maze room
    pointedRoomListInstance3[11].setSouthPointer(pointedRoomListInstance3[9])  # south points to Red Dais room
    pointedRoomListInstance3[11].setWestPointer(pointedRoomListInstance3[4])  # west points to Blue Maze room

    # pointers for Blue Underwater room ( edges ) INDEX 12
    pointedRoomListInstance3[12].setNorthPointer(pointedRoomListInstance3[12])  # north points to Blue Underwater room
    pointedRoomListInstance3[12].setEastPointer(pointedRoomListInstance3[14])  # east points to Green Columns room
    pointedRoomListInstance3[12].setSouthPointer(pointedRoomListInstance3[5])  # south points to Green Puzzle room
    pointedRoomListInstance3[12].setWestPointer(pointedRoomListInstance3[9])  # west points to Red Dais room

    # Ramp Room has no important pointers INDEX 13.

    # pointers for Green Columns Room ( edges ) INDEX 14
    # this room does exist and contradicts the general topology of the dungeon, however I did not make the dungeon.
    pointedRoomListInstance3[14].setNorthPointer(pointedRoomListInstance3[0])  # north points to Starting Room
    pointedRoomListInstance3[14].setEastPointer(pointedRoomListInstance3[0])  # east points to Starting Room
    pointedRoomListInstance3[14].setSouthPointer(pointedRoomListInstance3[0])  # south points to Starting Room
    pointedRoomListInstance3[14].setWestPointer(pointedRoomListInstance3[0])  # west points to Starting Room

    pointedRoomListInstance3[13].setEastPointer(
        pointedRoomListInstance3[5])  # Ramp has only one pointer pointing to Green Puzzle room

    pointedRoomSetInstance3 = set(pointedRoomListInstance3)  # Convert List to Set for purposes of the instance class
    instance3 = Instance(pointedRoomSetInstance3)  # instantiate instance.


"""
Modified maze-avoidance BFS Algorithm
"""


def prioBFS(instance, start_room, goal_room=None):
    visited = set()
    predecessor = dict()
    pq = []
    counter = itertools.count()  # unique sequence counter
    # Push starting node with priority 0 and unique count
    heapq.heappush(pq, (0, next(counter), start_room))
    visited.add(start_room)
    predecessor[start_room] = (None, None)

    while pq:
        current_priority, _, current_room = heapq.heappop(pq)

        if goal_room is not None and current_room == goal_room:
            path = []
            while current_room is not None:
                prev_room, pointer = predecessor[current_room]
                path.append((current_room, pointer.getDirection() if pointer else None))
                current_room = prev_room
            path.reverse()
            return path

        for pointer in current_room.getNeighboringRooms():
            neighbor_room = pointer.getRoomBeingPointedTo()
            if neighbor_room not in visited:
                priority = 0 if neighbor_room.getType().lower() != "maze" else 4
                visited.add(neighbor_room)
                predecessor[neighbor_room] = (current_room, pointer)
                heapq.heappush(pq, (priority, next(counter), neighbor_room))


"""
The discussion becomes DFS or BFS? is efficiency/memory capacity an issue for the user & if not what are the benefits of BFS?

Answer:
        BFS > DFS in this case because it ensures the same path & the shortest path every iteration
        despite the obvious memory constraints.

Why is memory contrainst not a concern?

Answer:
        The Shadow Crypt topology is not obvious to the user & BFS allows for fewer-hope paths to be found more efficiently 
        (comparitively speaking to DFS), meaning that this tool is more likely to be used in cases where the user mistakenly
        takes the wrong path and allows for the user to correct-course much quicker, and often times this will be by means of
        only a few hops.

NEW CONCERN: 
        Often times, the maze walls within the Shadow Crypt will change based on certain (often unbeknownst to the user) quest objectives.
        The implications of this is that these walls changing can create untraversable rooms giving invalid paths to the player.

MY SOLUTION:
        Implement a priority system within the breadth-first search algorithm prioritizing literally any other room to traverse to
        than the maze. This does not mean that mazes will not be ecountered in certain paths, however it makes it much less likely
        for the user to encounter any path constrainment.
"""


def bold(inputStr):
    return "\033[1m" + inputStr + "\033[0m"


def blue(inputStr):
    return "\033[34m" + inputStr + "\033[0m"


def green(inputStr):
    return "\033[32m" + inputStr + "\033[0m"


def red(inputStr):
    return "\033[31m" + inputStr + "\033[0m"


def yellow(inputStr):
    return "\033[33m" + inputStr + "\033[0m"


def orange(inputStr):
    return "\033[38;2;255;165;0m" + inputStr + "\033[0m"


def underline(inputStr):
    return "\033[4m" + inputStr + "\033[0m"


def colorize(color, input):
    if color.lower() == "yellow":
        return yellow(input)
    elif color.lower() == "green":
        return green(input)
    elif color.lower() == "blue":
        return blue(input)
    elif color.lower() == "red":
        return red(input)
    else:
        return bold(input)


def printPath(path):
    # print("Shortest path from source room to destination room in " + str(instancePathName) + " is:\n")
    directionLetterList = []  # Initialize outside to avoid scope issues

    if path:
        iter = 0
        for room, direction in path:
            if direction is None:
                print(f"Room: {colorize(room.getColor(), str(room))}")
            else:
                if iter < len(path) - 1:
                    print(
                        "Go " + underline(direction.upper()) + " to " + colorize(room.getColor(), str(room)) + "\nthen")
                else:
                    print("Go " + underline(direction.upper()) + " to " + colorize(room.getColor(), str(room)))
                # Append only if direction is a non-empty string
                if direction:
                    directionLetterList.append(direction[0])
            iter += 1
        # If no path found or empty, handle gracefully
        if not directionLetterList:
            print("Congratulations, you're already here!")
    else:
        print("No path found")

    # Only if directionLetterList is populated
    s = ""
    for letter in directionLetterList:
        s += letter.upper()
    if s:
        print("or more simply: " + s)
    print("\n")


def yesNoAssociation(input):
    if (isinstance(input, str)):
        input = input.lower()
        validResponses = {"y", "n", "yes", "no"}
        if input in validResponses:
            return True
        else:
            if input == "":
                return False
            else:
                # print("please enter either of y/n/yes/no (case insensitive)")
                return False
    else:
        print("please enter either of y/n/yes/no (case insensitive)")
        return False


def instanceAssociation(input):
    input = input.lower()
    validResponses = {"r", "g", "b", "red", "green", "blue"}
    if (input in validResponses):
        return True
    else:
        return False


def isExitChar(input):
    if input == "":
        print("Closing Program ... Thank you for using Crypt Router!")
        return True
    else:
        return False


def roomNotInTopologyChar(input):
    return input.strip().lower() == 'x'


def roomTerms(input):
    start = {"s", "start"}
    yellowCol = {"yc", "yellowcolumns"}
    greenCol = {"gc", "greencolumns"}
    redCol = {"rc", "redcolumns"}
    blueCol = {"bc", "bluecolumns"}
    yellowMaze = {"ym", "yellowmaze"}
    greenMaze = {"gm", "greenmaze"}
    redMaze = {"rm", "redmaze"}
    blueMaze = {"bm", "bluemaze"}
    yellowPuz = {"yp", "yellowpuzzle"}
    greenPuz = {"gp", "greenpuzzle"}
    redPuz = {"rp", "redpuzzle"}
    bluePuz = {"bp", "bluepuzzle"}
    yellowDais = {"yd", "yellowdais"}
    greenDais = {"gd", "greendais"}
    redDais = {"rd", "reddais"}
    blueDais = {"bd", "bluedais"}
    yellowUW = {"yu", "yellowunderwater"}
    greenUW = {"gu", "greenunderwater"}
    redUW = {"ru", "redunderwater"}
    blueUW = {"bu", "blueunderwater"}
    ramp = {"r", "ramp"}
    if input in start:
        return "s"
    elif input in yellowCol:
        return "yc"
    elif input in greenCol:
        return "gc"
    elif input in redCol:
        return "rc"
    elif input in blueCol:
        return "bc"
    elif input in yellowMaze:
        return "ym"
    elif input in greenMaze:
        return "gm"
    elif input in redMaze:
        return "rm"
    elif input in blueMaze:
        return "bm"
    elif input in yellowPuz:
        return "yp"
    elif input in greenPuz:
        return "gp"
    elif input in redPuz:
        return "rp"
    elif input in bluePuz:
        return "bp"
    elif input in yellowDais:
        return "yd"
    elif input in greenDais:
        return "gd"
    elif input in redDais:
        return "rd"
    elif input in blueDais:
        return "bd"
    elif input in yellowUW:
        return "yu"
    elif input in greenUW:
        return "gu"
    elif input in redUW:
        return "ru"
    elif input in blueUW:
        return "bu"
    elif input in ramp:
        return "r"
    else:
        return "invalid room"