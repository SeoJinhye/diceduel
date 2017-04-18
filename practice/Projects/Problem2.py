import random
secret = raw_input("write the number")
guess = random.randint(1,1000)
while(secret != guess):
	if(guess > secret):
		print("It is smaller")
		guess = random.randint(1,guess)
	if(secret > guess):
		print("It is bigger")
		guess = random.randint(guess,1000)
print("You are correct! You won!")
	