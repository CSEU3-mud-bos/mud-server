import uuid
from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
import random


roomTitles = ["Red", "Easter Bunny", "Mamba", "Egg Sandwhich", "Beast", "Gypsy", "Gems", "German Dungeon", "Gulag",
              "Lebron's Hairline", "Nerd", "Wiz Khalifia's Magic Box", "Dirty Hair", "Michael Jackson's Rollercoaster", "Zippers", "Red Rummmmm"]

descriptions = ["You have reached the room where the magic happens", "You have reached the room where you take off your hat", "You have reached the room where the party starts", "You have reached the room where kiss the sand", "You have reached the room where your elbows get ashy", "You have reached the room where lights go out", "You have reached the room where its haunted", "You have reached the room where there is no return Mwuahahahahha", "You have reached the room where you let the dogs out", "You have reached the room where you become a man", "You have reached the room where you pick your pronouns", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus",
                "You have reached the room where you've been CURED from the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've met your creator", "You have reached the room where you've given up on Django", "You have reached the room where you've voted for Trump", "You have reached the room where you've voted for Bernie Sanders", "You have reached the room where you've made it to the coast"]


class Room(models.Model):
    id = models.IntegerField()
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()

    # def playerNames(self, currentPlayerID):
    #     return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    # def playerUUIDs(self, currentPlayerID):
    #     return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


# class Player(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     currentRoom = models.IntegerField(default=0)
#     uuid = models.UUIDField(default=uuid.uuid4, unique=True)

#     def initialize(self):
#         if self.currentRoom == 0:
#             self.currentRoom = Room.objects.first().id
#             self.save()

#     def room(self):
#         try:
#             return Room.objects.get(id=self.currentRoom)
#         except Room.DoesNotExist:
#             self.initialize()
#             return self.room()


# @receiver(post_save, sender=User)
# def create_user_player(sender, instance, created, **kwargs):
#     if created:
#         Player.objects.create(user=instance)
#         Token.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_player(sender, instance, **kwargs):
#     instance.player.save()


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.list1 = []
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1  # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:
            print(room_count)

            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            if room_count == 0:
                self.n_to = None
                self.s_to = None
                self.e_to = room_count + 1
                self.w_to = None
            elif (room_count + 1) % 15 == 0 and direction < 0 and room_count >= 14:
                self.n_to = room_count+1
                self.s_to = None
                self.e_to = room_count - 1
                self.w_to = None
            elif (room_count + 1) % 15 == 0 and direction > 0 and room_count >= 14:
                self.n_to = room_count+1
                self.s_to = None
                self.w_to = room_count - 1
                self.e_to = None
            elif room_count % 15 == 0 and direction < 0 and room_count >= 14:
                self.s_to = room_count - 1
                self.n_to = None
                self.w_to = room_count + 1
                self.e_to = None
            elif room_count % 15 == 0 and direction > 0 and room_count >= 14:
                self.s_to = room_count - 1
                self.n_to = None
                self.e_to = room_count + 1
                self.w_to = None
            elif direction > 0:
                self.w_to = room_count - 1
                self.e_to = room_count + 1
                self.n_to = None
                self.s_to = None
            else:
                self.w_to = room_count + 1
                self.e_to = room_count - 1
                self.n_to = None
                self.s_to = None

            # Create a room in the given direction
            room = Room(id=room_count, title=random.choice(roomTitles),
                        description=random.choice(descriptions), n_to=self.n_to,  s_to=self.s_to,  e_to=self.e_to, w_to=self.w_to, x=x, y=y)
           # print(room.n_to)
            room.save()

            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            self.grid[y][x] = room

            # Connect the new room to the previous room
            # if previous_room is not None:
            #     previous_room.connect_rooms(room, room_direction)

            # Update iteration variables
            previous_room = room
            room_count += 1
        # for i in self.list1:
        #     print(i.id)

#     def print_rooms(self):
#         '''
#         Print the rooms in room_grid in ascii characters.
#         '''

#         # Add top border
#         str = "# " * ((3 + self.width * 5) // 2) + "\n"

#         # The console prints top to bottom but our array is arranged
#         # bottom to top.
#         #
#         # We reverse it so it draws in the right direction.
#         reverse_grid = list(self.grid)  # make a copy of the list
#         reverse_grid.reverse()
#         for row in reverse_grid:
#             # PRINT NORTH CONNECTION ROW
#             str += "#"
#             for room in row:
#                 if room is not None and room.n_to is not None:
#                     str += "  |  "
#                 else:
#                     str += "     "
#             str += "#\n"
#             # PRINT ROOM ROW
#             str += "#"
#             for room in row:
#                 if room is not None and room.w_to is not None:
#                     str += "-"
#                 else:
#                     str += " "
#                 if room is not None:
#                     str += f"{room.id}".zfill(3)
#                 else:
#                     str += "   "
#                 if room is not None and room.e_to is not None:
#                     str += "-"
#                 else:
#                     str += " "
#             str += "#\n"
#             # PRINT SOUTH CONNECTION ROW
#             str += "#"
#             for room in row:
#                 if room is not None and room.s_to is not None:
#                     str += "  |  "
#                 else:
#                     str += "     "
#             str += "#\n"

#         # Add bottom border
#         str += "# " * ((3 + self.width * 5) // 2) + "\n"

#         # Print string
#         print(str)


# print(0 % 14)
w = World()
num_rooms = 100
width = 15
height = 7
w.generate_rooms(width, height, num_rooms)
