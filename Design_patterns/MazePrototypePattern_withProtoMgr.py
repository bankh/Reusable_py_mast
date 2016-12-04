### Creational Design Pattern
#   Prototype pattern
# TODO: FIX the errors in the last section and add extra properties 

from copy import deepcopy
from enum import Enum

# Abstract Base Class
class MapSite():
    def Enter(self):
        raise NotImplementedError('Abstract Base Class Method')

class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3

#====================================================================
#   Prototype Definition of Door
#=====================================================================

class Door(MapSite):
    def __init__(self, other=None):     # Copy constructor as in the C++
        self._isOpen = False
        if other:                       #Copy constructor
            self._room1 = other._room1
            self._room2 = other._room2
        else:
            self._room1 = None          # Private Members
            self._room2 = None

    def Initialize(self, r1, r2):
        self._room1 = r1                # Initialize private members
        self._room2 = r2

    def Clone(self):
        return Door(self)

    def OtherSideFrom(self, Room):
        print('\t Door obj: This door is a side of Room: {}'.format(Room._roomNumber))
        if 1 == Room._roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1

        return other_room

    def Enter(self):
        if self._isOpen:
            print(' *** You have passed through this door...')
        else:
            print(' ** This door needs to be opened before you can pass through it...')

#====================================================================
#   Prototype Definition of Room
#=====================================================================

class Room(MapSite):
    def __init__(self, roomNo=0):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)

    def GetSide(self, Direction):
        return self._sides[Direction]

    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite

    def Enter(self):
        print(' You have entered room: ' + str(self._roomNumber))

    def Clone(self):
        return deepcopy(self)

    def Initialize(self, roomNo):
        self._roomNumber = int(roomNo)

#====================================================================
#   Prototype Definition of Wall
#=====================================================================

class Wall(MapSite):
    def Enter(self):
        print(' * You just ran into a Wall..')

    def Clone(self):
        return deepcopy(self)

class Maze():
    def __init__(self):
        # Dictionary to hold room_number, room_obj <value, key> pairs
        self._rooms = {}

    def AddRoom(self, room):
        #use roomNumber as lookup value to retrieve room objects
        self._rooms[room._roomNumber] = room

    def RoomNo(self, room_number):
        return self._rooms[room_number]

class MazeFactory():
    @classmethod        #decorator
    def MakeMaze(cls):  # cls, not self
        return Maze()   #return Maze Instance
    
    @classmethod
    def MakeWall(cls):
        return Wall()

    @classmethod
    def MakeRoom(cls, r1, r2):
        return Door(r1, r2)

    
class MazeGame():
    #Abstract Factory
    def CreateMaze(self, factory = MazeFactory):
        aMaze = factory.MakeMaze()
        r1 = factory.MakeRoom(1)
        r2 = factory.MakeRoom(2)
        aDoor = factory.MakeDoor(r1,r2)
        
        aMaze.AddRoom(r1)
        aMaze.AddRoom(r2)
        
        r1.SetSide(Direction.North.value, factory.MakeWall())
        r1.SetSide(Direction.East.value, aDoor)
        r1.SetSide(Direction.South.value, factory.MakeWall())
        r1.SetSide(Direction.West.value, factory.MakeWall())
        
        r2.SetSide(Direction(0).value, factory.MakeWall())
        r2.SetSide(Direction(1).value, factory.MakeWall())
        r2.SetSide(Direction(2).value, factory.MakeWall())
        r2.SetSide(Direction(3).value, aDoor)
        
        return aMaze

#==========================================================================
#   *** Here starts the Prototype Pattern
#==========================================================================
class MazePrototypeFactory(MazeFactory): # Subclass Mazefactory (Inheriting)
    # C++ ctpr: MazePrototypeFactory(Maze*, Wall*, Room*, Door*)
    # in python we use __init__: instead
    def __init__(self, m, w, r, d):
        # initialize prototypes // C++ private members
        # these variables hold class instances of Mazes, Walls, etc.
        self._prototypeMaze = m
        self._prototypeWall = w
        self._prototypeRoom = r
        self._prototypeDoor = d
    
        self.prototype_manager_registry = {} # Store of created prototype

    def register_prototype(self, key, prototype):
        self.prototype_manager_registry[key] = prototype    # add to store

    def unregister_prototype(self, key):
        del self.prototype_manager_registry[key]            # delete from store

    def MakeWall(self):
        return self._prototypeWall.Clone()                  # call Clone() method on prototype
    
    def MakeDoor(self, r1, r2):
        door = self._prototypeDoor.Clone()                  # call Clone() method on Door
        door.Initialize(r1, r2)                             # Initialize the rooms between door
        return door

    def MakeRoom(self, n):
        room = self._prototypeRoom.Clone()                  # call Clone() method on Room
        room.Initialize(n)                                  # initialize room number
        return room


if __name__ == '__main__':

    # Create a prototypical/ default maze factory
    # initialize with basic component objects
    simpleMazeFactory = MazePrototypeFactory(
        Maze(), Wall(), Room(), Door()              #Pass in instances of components
    )

    # Pass the prototype into the game
    play_game(simpleMazeFactory)

    # Change type of maze by initializing the MazePrototypeFactory
    # with a different set of prototypes
    bombedMazeFactory = MazePrototypeFactory(
        Maze(), BombedWall(), 
        RoomWithABomb(), Door()
    )

    # Pass the prototype into the game
    play_game(bombedMazeFactory)

    #Create a maze that will consist of 100 rooms with 400 walls
    complexMazeFactory = MazePrototypeFactory(
        Maze(), Wall(), Room(), Door()          # Pass in instances of components
    )

    game = MazeGame()
    maze = game.CreateMaze(complexMazeFactory)  # Create 2 rooms with a door in between

    # Print current maze objects
    from pprint import pprint
    pprint(maze._rooms)
    print()

    # Create 98 more rooms and add them to the maze -- they are not connected to each other
    for roomNo in range(3, 101):         # Create 98 more rooms
        new_room = Room()
        new_room.Initialize(roomNo)     # Give room unique number
        maze.AddRoom(new_room)          # Add room to maze

    pprint(maze.__dict__)               # Print maze object
    print()
    pprint(complexMazeFactory.__dict__) # Print complex

    print()
    print(maze.RoomNo(99))
    print(maze.RoomNo(99).GetSide(0))                       # 0 = North
    print(maze.RoomNo(99).GetSide(Direction(0).value))      # 0 = North
    print(maze.RoomNo(99).GetSide(Direction.South.value))   # Room has either Door nor Wall
    print()

    # Create 400 walls and add them to the 100 rooms
    for room in range(3, 101):
        for site_dir in range(4):
            new_wall = Wall()
            maze.RoomNo(room).SetSide(site_dir, new_wall)
            print(maze.RoomNo(room).GetSide(site_dir))
    print()

    # Print out the 4 sides of some rooms (any room between 1 - 100)
    for side in range(4):
        print(' Room: ' + '12', Direction(side), maze.RoomNo(12).GetSide(side))
    
    print()
    for side in range(4):
        print('Room: ' + '100', Direction(side), maze.RoomNo(100).GetSide(side))

    print()

    # We are building a maze consisting of 100 rooms
    # We use this as a prototype to build different mazes, all consisting of 100 roms
    # but with doors that can be located in different directions of any rooms.
    #

    # Now that we have created an expensive object, let us register this prototype maze
    complexMazeFactory.register_Prototype('100_Rooms', maze)
    print(maze)
    print()
    print(complexMazeFactory.prototype_manager_registry)

    # Clone maze
    # We are creating a copy of the already created maze object
    original = complexMazeFactory.prototype_manager_registry['100_rooms']
    print('\nproto Maze:', clone, clone.__class__)  #same class, different object in memoryview

    print()
    print(clone.RoomNo(100).GetSide(3))

    clone.RoomNo(100).SetSide(3, BombedWall())  #Change the type of Wall
    print(clone.RoomNo(100).GetSide(3))

    #Helper function to find rooms that have doors
    def find_doors(the_clone, first_room, last_room):
        for room_number in range(first_room, last_room):
            for room_direction in range(4):
                site = the_clone.RoomNo(room_number).GetSide(room_direction)
                if 'Door' in str(site):
                    print('Room:' + str(room_number).GetSide(room_direction),site)
                        #print('Room: ' + str(room_number), site)
                        # 
    print('\n Doors in Rooms 1 to 100') # clone has one door between Room1 and Room2
    find_doors(clone, 1, 101)
    
    # Add a door to Room2
    new_door = Door()
    clone.RoomNo(2).SetSide(Direction.East.value, new_door)
    clone.RoomNo(3).SetSide(Direction.West.value, new_door)

    print('\nDoors in Rooms 1 to 10')
    find_doors(clone, 1, 10)

    # Make another clone from the prototype manager registry
    another_clone = deepcopy(original)
    print('\nanother_clone:', another_clone, another_clone.__class__) # Same class, different object

    # Add a door to room 2
    new_door = Door()
    another_clone.RoomNo(2).SetSide(Direction.North.value, new_door)
    another_clone.RoomNo(3).SetSide(Direction.South.value, new_door)

    print('\nDoors in Rooms 1 to 10')
    find_doors(another_clone, 1, 10)
    