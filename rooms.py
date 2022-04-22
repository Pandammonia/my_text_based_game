from textwrap import dedent
from characters import *

luke = Engineer('Luke', '29')
firstenemy = EightArmedAlien("KwawawaPararaYannaManSardan", 30, 5, 5, 25)
cleared_rooms = []
rooms = []
inventory = []
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
				luke.addweapontoinvent(Items("9mm", 10, 0, 0))
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
				cor.start_corridor()
				break
			else:
				print("Please enter some valid input")

class Corridor():
	def __init__(self, roomname):
		self.roomname = roomname

	def start_corridor(self):
		print("An enemy eight armed alien!")
		while firstenemy.currenthp() > 0:
			print("You current weapons are: ", end ="")
			luke.checkweapons()
			wepchoice = input("Choose a weapon to attack with: > ")
			if wepchoice == '9mm':
				hit = luke.attack()
				print(f"You hit the alien for {hit} damage!")
				firstenemy.healthchange(hit)
				print(f"The alien has {firstenemy.currenthp()} health points left!")
				eatk = firstenemy.enemyatk()
				print(f"The enemy hits you for {eatk} damage!")
				luke.healthchange(eatk)
				print(f"You have {luke.check_hp()} health points left!")
			else:
				print("Please pick a weapon you own")
		print("Well done, you defeated your first enemy!")

cor = Corridor("Corridor")

