import random
from textwrap import dedent
from characters import *
from rooms import *

def showmap():
	print("/---------\\     ==========      ")
	print("| Armoury |====  Corridor    ")
	print("\\---------/     ==========")
	corridor()

def mapchoice():
	mapchoice = True
	while mapchoice:
		mapchoice = input("Please enter next room")
		if mapchoice.lower() in cleared_rooms:
			print("I need to keep moving forward!")


"""doorcode = f"{random.randint(0,9)}{random.randint(0,9)}"
print(doorcode)"""
cleared_rooms = []
rooms = []
inventory = []
luke = Engineer('Luke', '29')
firstenemy = EightArmedAlien("KwawawaPararaYannaManSardan", 100, 5, 5, 25)
arm = Armoury("Armoury")
cor = Corridor("Corridor")
arm.run_armoury()