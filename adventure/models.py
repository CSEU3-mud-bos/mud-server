import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import random


roomTitles = ["Red", "Easter Bunny", "Mamba", "Egg Sandwhich", "Beast", "Gypsy", "Gems", "German Dungeon", "Gulag",
              "Lebron's Hairline", "Nerd", "Wiz Khalifia's Magic Box", "Dirty Hair", "Michael Jackson's Rollercoaster", "Zippers", "Red Rummmmm"]

descriptions = ["You have reached the room where the magic happens", "You have reached the room where you take off your hat", "You have reached the room where the party starts", "You have reached the room where kiss the sand", "You have reached the room where your elbows get ashy", "You have reached the room where lights go out", "You have reached the room where its haunted", "You have reached the room where there is no return Mwuahahahahha", "You have reached the room where you let the dogs out", "You have reached the room where you become a man", "You have reached the room where you pick your pronouns", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus",
                "You have reached the room where you've been CURED from the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've been INFECTED with the coronavirus", "You have reached the room where you've met your creator", "You have reached the room where you've given up on Django", "You have reached the room where you've voted for Trump", "You have reached the room where you've voted for Bernie Sanders", "You have reached the room where you've made it to the coast"]


class Room(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")
    n_to = models.IntegerField(default=None, blank=True, null=True)
    s_to = models.IntegerField(default=None, blank=True, null=True)
    e_to = models.IntegerField(default=None, blank=True, null=True)
    w_to = models.IntegerField(default=None, blank=True, null=True)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)

    # def connectRooms(self, destinationRoom, direction):
    #     destinationRoomID = destinationRoom.id
    #     try:
    #         destinationRoom = Room.objects.get(id=destinationRoomID)
    #     except Room.DoesNotExist:
    #         print("That room does not exist")
    #     else:
    #         if direction == "n":
    #             self.n_to = destinationRoomID
    #         elif direction == "s":
    #             self.s_to = destinationRoomID
    #         elif direction == "e":
    #             self.e_to = destinationRoomID
    #         elif direction == "w":
    #             self.w_to = destinationRoomID
    #         else:
    #             print("Invalid direction")
    #             return
    #         self.save()

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
