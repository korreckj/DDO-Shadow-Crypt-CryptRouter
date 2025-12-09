from room import Room

class Instance:
    def __init__(self, roomsInInstance=None):
        if roomsInInstance is None:
            self.roomsInInstance = set()
        else:
            if isinstance(roomsInInstance, set) and all(isinstance(e, Room) for e in roomsInInstance):
                self.roomsInInstance = roomsInInstance
            else:
                raise TypeError("Set must contain only Room instances")

    def getRoomsInInstance(self):
        return self.roomsInInstance

    def setRoomsInInstance(self, roomSet):
        if isinstance(roomSet, set):
            self.roomsInInstance = roomSet
        else:
            print("Given data type must be a set")

    def addRoomObjToInstance(self, room):
        if len(self.roomsInInstance) < 12:
            if isinstance(room, Room):
                self.roomsInInstance.add(room)
            else:
                raise TypeError("Elements added to the set of rooms must also be rooms")
        else:
            raise ValueError("Set cannot have more than 12 rooms")

    def addRoomToInstance(self, color, structure):
        if len(self.roomsInInstance) < 12:
            tempRoom = Room(color, structure)
            self.roomsInInstance.add(tempRoom)
        else:
            raise ValueError("Set cannot have more than 12 rooms")

    def __str__(self):
        tempString = ""
        for room in self.roomsInInstance:
            tempString += str(room) + "\n"
        finalString = "Rooms in this instance: " + tempString
        return finalString
