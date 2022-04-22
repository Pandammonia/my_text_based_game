import random


class Engineer():
	"""Class to create main character 
	and functions available to character"""
	def __init__(self, name, age):
		self.inventory = []
		self.name = name
		self.age = age
		self.health = 100

	def addtoinvent(self, items):
		for x in items:
			self.inventory.append(x)

	def check_inventory(self):
		print(f"Current inventory contents: ")
		for x in self.inventory:
			print(x)

	def check_hp(self):
		print(f"You current health points are: {self.health}")






def armoury_start():
	print("You come round in the armoury... the ship's siren is sounding.")
	print("The red glow bathing the walls tells you the ship is running on emergency power.")
	while True:
		decision = input("What would you like to do? [check bag / open personal locker / leave room]\n")
		if decision == 'check bag':
			luke.check_inventory()
		if decision == 'open personal locker':
			if 'medkit' not in inventory:
				locker = ["medkit", "9mm pistol", "9mm magazine", "set of lockpicks"]
				luke.addtoinvent(locker)
				print("Your personal effects are in your locker, they have been added to your inventory.")
			else:
				print("You have already checked your locker.")
				continue
		if decision == 'leave room':
			print("There is an electronic keypad on the door")
			doorcode = randint(0,9), randint(0,9), randint(0,9)




doorcode = f"{random.randint(0,9)}{random.randint(0,9)}"
print(doorcode)
inventory = []
luke = Engineer('Luke', '29')
luke.check_inventory()
luke.check_hp()
armoury_start()
