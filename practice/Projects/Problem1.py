import random
secret = random.randint(1,1000)
guess = int(input("guess a number"))
while(secret != guess):
	if(guess < 1 or 1000 < guess):
		print(guess, secret)
		print("out of range")
		guess = int(input("guess a number"))
	elif(guess > secret):
		print(guess, secret)
		print("It needs to be smaller")
		guess = int(input("guess a number"))
	elif(secret < guess):
		print(guess, secret)
		print("It needs to be bigger")
		guess = int(input("guess a number"))
print("You are correct! You won!")
