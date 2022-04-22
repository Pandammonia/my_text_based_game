from random import *

class EightArmedAlien():
	def __init__(self, name, health, attack, defence, inventory):
		self.inventory = inventory
		self.name = name
		self.health = health
		self.attack = attack
		self.defence = defence
	def enemyatk(self):
		hit = randint(0,self.attack)
		return hit
	def currenthp(self):
		health = self.health
		return health
	def healthchange(self, change):
		self.health = self.health-change



class Engineer():
	"""Class to create main character 
	and functions available to character"""
	def __init__(self, name, age):
		self.inventory = []
		self.weapons = []
		self.name = name
		self.age = age
		self.health = 100

	def addweapontoinvent(self,item):
		self.weapons.append(item)

	def healthchange(self, change):
		self.health = self.health-change

	def addtoinvent(self, item):
		self.inventory.append(item)

	def attack(self):
		hit = randint(0,10)
		return hit 

	def checkweapons(self):
		print(f"Current weapons: ", end = "")
		for x in self.weapons:
			print(x.name)

	def check_inventory(self):
		print(f"Current inventory contents: ")
		for x in self.inventory:
			print(x.name)

	def check_hp(self):
		hp = self.health
		return hp

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

	def attack(self, item):
		wepattack = item.attack
		damage = randint(0,wepattack)
