class Pointer:
    def __init__(self, roomBeingPointedTo, direction):
        self.roomBeingPointedTo = roomBeingPointedTo
        self.direction = direction
    def getDirection(self):
        return self.direction
    def getRoomBeingPointedTo(self):
        return self.roomBeingPointedTo
    def setRoomBeingPointedTo (self, room):
        if isinstance(room, Room):
            self.roomBeingPointedTo = room
        else:
            raise TypeError("Data must be of Room type")
    def setDirection (self, direction):
        validDirections = {"north", "east", "south", "west"}
        if(isinstance(direction, str)):
            if direction.lower() in validDirections:
                self.direction = direction
            else:
                raise AttributeError("Not a valid direction")
        else:
            raise TypeError("Directions can only be Strings")
    def __str__(self):
        return "This pointer points to " + str(self.roomBeingPointedTo) + self.direction


class Room:

    def __init__(self, color, structure):
        self.color = color
        self.structure = structure
        self.northPointer = None  # need to keep track of where a given rooms north exit leads.
        self.eastPointer = None  # need to keep track of where a given rooms east exit leads.
        self.southPointer = None  # need to keep track of where a given rooms south exit leads.
        self.westPointer = None  # need to keep track of where a given rooms north exit leads.
        self.neighboringRooms = set()  # Need to maintain a neighboringRoom set to manage routing among rooms.

    # room attribute retrieval methods
    def getColor(self):
        return self.color

    def getType(self):
        return self.structure

    def getNorthPointer(self):
        return self.northPointer

    def getEastPointer(self):
        return self.eastPointer

    def getSouthPointer(self):
        return self.southPointer

    def getWestPointer(self):
        return self.westPointer

    def getNeighboringRooms(self):
        return self.neighboringRooms

    # room attribute mutator methods

    def setNorthPointer(self, room):
        # logic is to update the northmost room and keep record within the set.
        if self.northPointer not in self.neighboringRooms:
            self.northPointer = Pointer(room, "north")
            self.neighboringRooms.add(self.northPointer)
        else:
            self.neighboringRooms.remove(self.northPointer)
            self.northPointer = Pointer(room, "north")
            self.neighboringRooms.add(self.northPointer)

    def setEastPointer(self, room):
        # logic is to update the eastmost room and keep record within the set.
        if self.eastPointer not in self.neighboringRooms:
            self.eastPointer = Pointer(room, "east")
            self.neighboringRooms.add(self.eastPointer)
        else:
            self.neighboringRooms.remove(self.eastPointer)
            self.eastPointer = Pointer(room, "east")
            self.neighboringRooms.add(self.eastPointer)

    def setSouthPointer(self, room):
        # logic is to update the southmost room and keep record within the set.
        if self.southPointer not in self.neighboringRooms:
            self.southPointer = Pointer(room, "south")
            self.neighboringRooms.add(self.southPointer)
        else:
            self.neighboringRooms.remove(self.southPointer)
            self.southPointer = Pointer(room, "south")
            self.neighboringRooms.add(self.southPointer)

    def setWestPointer(self, room):
        # logic is to update the westmost room and keep record within the set.
        if self.westPointer not in self.neighboringRooms:
            self.westPointer = Pointer(room, "west")
            self.neighboringRooms.add(self.westPointer)
        else:
            self.neighboringRooms.remove(self.westPointer)
            self.westPointer = Pointer(room, "west")
            self.neighboringRooms.add(self.westPointer)

    def __str__(self):
        # toString method for printing the objects
        finalStr = ""
        if (self.color.lower() == "colorless"):
            finalStr = str(self.structure)
        else:
            finalStr = str(self.color + " " + self.structure)
        return finalStr
