luggage = []

print(luggage)
print("you have space for 5 items")

while(len(luggages) < 5):
	item = input("what whould you like to bring?")
	luggage.append(item)
	print(luggage)

for item in luggage:
		print(item)