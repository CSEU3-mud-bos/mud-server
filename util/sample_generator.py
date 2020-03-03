# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.
import random
# from .models import Room
print(Room)


roomTitles = ["Red", "Easter Bunny", "Mamba", "Egg Sandwhich", "Beast", "Gypsy", "Gems", "German Dungeon", "Gulag",
              "Lebron's Hairline", "Nerd", "Wiz Khalifia's Magic Box", "Dirty Hair", "Michael Jackson's Rollercoaster", "Zippers", "Red Rummmmm"]

descriptions = ["You have reached the room where the magic happens", "You have reached the room where you take off your hat", "You have reached the room where the party starts", "You have reached the room where kiss the sand", "You have reached the room where your elbows get ashy", "You have reached the room where lights go out", "You have reached the room where its haunted", "You have reached the room where there is no return Mwuahahahahha", "You have reached the room where you let the dogs out", "You have reached the room where you become a man", "You have reached the room where you pick your pronouns", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus",
                "You have reached the room where you've been CURED from the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've met your creator", "You have reached the room where you've given up on Django", "You have reached the room where you've voted for Trump", "You have reached the room where you've voted for Bernie Sanders", "You have reached the room where you've made it to the coast"]


class Rooms:
    def __init__(self, id, name, description, n_to, s_to, e_to, w_to, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.x = x
        self.y = y

    # def __repr__(self):
    #     if self.e_to is not None:
    #         return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
    #     return f"({self.x}, {self.y})"

    # def __repr__(self):

    #     return f"Room {self.id} \n{self.name}\n{self.description}\n{self.n_to}\n{self.s_to}\n{self.e_to}\n{self.w_to}\n{self.x}\n{self.y}\n-----------------------------------------------"

    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)

    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


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
            self.list1.append(room)

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
# w.print_rooms()

# for i in w.list1:
#     #
#     print(f"Room {i.id} \nName: {i.name}\nDescription: {i.description}\nNorth: {i.n_to}\nSouth: {i.s_to}\nEast: {i.e_to}\nWest: {i.w_to}\nX: {i.x}\nY: {i.y}\n-----------------------------------------------")
# print(
#     f"\\nnWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")

# World

# world -> id 1

# Rooms

# room -> id 1, y 0, x 0
# room -> id 2, y 0, x 1
# room -> id 3, y 0, x 2
# room -> id 4, y 0, x 3

# room -> id 5, y 1, x 0
# room -> id 6, y 1, x 1
# room -> id 7, y 1, x 2
# room -> id 8, y 1, x 3


# room where y = 0

# 0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15

# 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 20


# for room_count, item in enumerate(list):
#     r = Room(id=i.id,
#              description=i.description,
#              x=i.x,
#              y=i.y,
#              n_to=i.n_to,
#              s_to=i.s_to)
#     r.save()

# if room_count == 0:
#     n_to = None
#     s_to = None
#     e_to = room_count - 1
#     w_to = None
# elif room_count % 14 == 0 and direction < 0:
#     n_to = room_count+1
#     s_to = None
#     e_to = room_count - 1
#     w_to = None
# elif room_count % 14 == 0 and direction > 0:
#     n_to = room_count+1
#     s_to = None
#     w_to = room_count - 1
#     e_to = None
# elif (room_count - 1) % 14 == 0 and direction < 0:
#     s_to = room_count - 1
#     n_to = None
#     w_to = room_count + 1
#     e_to = None
# elif (room_count - 1) % 14 == 0 and direction > 0:
#     s_to = room_count - 1
#     n_to = None
#     e_to = room_count + 1
#     w_to = None
# elif direction > 0:
#     w_to = room_count - 1
#     e_to = room_count + 1
#     n_to = None
#     s_to = None
# elif direction < 0:
#     w_to = room_count + 1
#     e_to = room_count - 1
#     n_to = None
#     s_to = None


# list[room_count - 1] % 14 ==


# print(0 % 14)
