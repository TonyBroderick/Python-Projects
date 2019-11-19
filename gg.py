import random 

random_number = random.randint(1,10)
user = None

while user != random_number:
	user = input("Guess a number between 1 to 10: ")
	user = int(user)
	if user < random_number:
		print("TOO LOW")
	elif user > random_number:
		print("TOO HIGH")
	else:
		print("YOU WON!!!!")
print(random_number)