import random
from textwrap import dedent


class Items():
	"""Class that creates items and describes them"""
	def __init__(self, name, attack, defence, heal):
		self.name = name
		self.attack = attack
		self.defence = defence
		self.heal = heal

	def look(self):
		if self.attack > 0:
			print(f"This is a {self.name}, its attack stat is: {self.attack}")
		if self.defence > 0:
			print(f"This is a {self.name}, its defence stat is {self.defence}")
		if self.heal > 0:
			print(f"The {self.name} heals {self.heal} hit points.")

class Armoury():
	"""Class that creates a room with an empty list to fill with items (calls Item class)"""
	def __init__(self, roomname):
		self.roomname = roomname
		self.items = []

	def additem(name, attack, defence, heal):
		item = Items(name, attack, defence, heal)
		items.append(item)

	def showitems(self):
		for x in self.items:
			Items.look(x)

	def run_armoury(self):
		print(dedent("""
	You come round in the armoury... the ship's siren is sounding. The red glow bathing 
	the walls tells you the ship is running on emergency power.
	"""))
		locker = 'shut'
		while locker == 'shut':
			decision = input("What would you like to  do? Check locker / check bag / leave room > ")
			if decision == 'check bag':
				luke.check_inventory()
				continue
			if decision == 'check locker':
				print("You took your 9mm handgun and your kevlar vest")
				luke.addtoinvent(Items("9mm", 10, 0, 0))
				luke.addtoinvent(Items("Kevlar Vest", 0, 10, 0))
				locker = 'open'
				break
			if decision == 'leave room':
				print("I should check my locker first...")
				continue
			else:
				print("Please enter some valid input")
		leave = 'no'
		while leave == 'no':
			decision = input("What would you like to do? check bag / leave room > ")
			if decision == 'check bag':
				luke.check_inventory()
				continue
			if decision =='leave room':
				cleared_rooms.append("Armoury")
				print("You leave the armoury and head into the corridor....")
				corridor()
				break
			else:
				print("Please enter some valid input")




class EightArmedAlien():
	def __init__(self, name, health, attack, defence, inventory):
		self.inventory = inventory
		self.name = name
		self.health = health
		self.attack = attack
		self.defence = defence


class Engineer():
	"""Class to create main character 
	and functions available to character"""
	def __init__(self, name, age):
		self.inventory = []
		self.name = name
		self.age = age
		self.health = 100

	def addtoinvent(self, item):
		self.inventory.append(item)

	def check_inventory(self):
		print(f"Current inventory contents: ")
		for x in self.inventory:
			print(x.name)

	def check_hp(self):
		print(f"You current health points are: {self.health}")


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
arm = Armoury("Armoury")
arm.run_armoury()