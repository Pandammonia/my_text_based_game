import random

class Items():
	def __init__(self, name, attack, defence, heal):
		self.name = name
		self.attack = attack
		self.defence = defence
		self.heal = heal

	def look(self):
		if self.attack > 0:
			print(f"The {self.name} has an attack stat of {self.attack}")
		if self.defence > 0:
			print(f"The {self.name}, has an armour rating of {self.defence}")
		if self.heal > 0:
			print(f"The {self.name} heals {self.heal} hit points.")


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

	"""def addtoinvent(self, items):
		for x in items:
			self.inventory.append(x)"""

	def check_inventory(self):
		print(f"Current inventory contents: ")
		for x in self.inventory:
			print(x)

	def check_hp(self):
		print(f"You current health points are: {self.health}")

def addtoinvent(items):
	for x in items:
		inventory.append(x)

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


def corridor():
	print("You cautiously enter the corridor leading to the ship's hangar")
	print("There is an 8 armed alien up ahead with no way past it")
	print("You draw your 9mm and move forward to engage the alien")


def armoury_start():
	print("You come round in the armoury... the ship's siren is sounding.")
	print("The red glow bathing the walls tells you the ship is running on emergency power.")
	while True:
		decision = input("What would you like to do? [check bag / open personal locker / leave room]\n")
		if decision == 'leave room' and 'medkit' not in inventory:
			print("I'd check the locker if i were you")
			continue
		if decision == 'check bag':
			luke.check_inventory()
		if decision == 'open personal locker':
			if 'medkit' not in inventory:
				locker = ["medkit", "9mm pistol", "9mm magazine", "set of lockpicks"]
				addtoinvent(locker)
				print("Your personal effects are in your locker, they have been added to your inventory.")
			else:
				print("You have already checked your locker.")
				continue
		if decision == 'leave room':
			cleared_rooms.append("Armoury)")
			showmap()




"""doorcode = f"{random.randint(0,9)}{random.randint(0,9)}"
print(doorcode)"""
cleared_rooms = []
rooms = []
inventory = []
luke = Engineer('Luke', '29')
armoury_start()
