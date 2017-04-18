mood = raw_input("How are you today?")
while(mood != "Overheated" and mood != "overheated" and mood != "OVERHEATED"):
	print("that's the wrong answer")
	mood = raw_input("How are you doing today?")
print("that's the right answer!")
