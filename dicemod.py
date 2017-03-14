def getsome():
	D = int(input("what dice do you want to roll?"))
	P1 = random.randrange(1,D)
	P2 = random.randrange(1,D)
	return(P1,P2)

import random
import webbrowser
url = 'https://www.google.com/search?client=ubuntu&channel=fs&q=the+answer+to+the+life+and+universe&ie=utf-8&oe=utf-8#channel=fs&q=the+answer+to+life+the+universe+and+everything&*'
P1 = 0
P2 = 0
P1avg = 0
P2avg = 0
P1temp = 0
P2temp = 0
count = 0
change = getsome()
P1 = change[0]
P2 = change[1]
Start = raw_input("write start to start the game")
while(Start == "start"):
		print("P1 got:" + str(P1) + " P2 got:" + str(P2))
		P1avg += P1
		P2avg += P2
		P1temp += P1
		P2temp += P2
		count+=1
		P1temp /= count
		P2temp /= count
		#print("Current P1 Avg: " + str(P1temp))
		#print("Current P2 Avg: " + str(P2temp))
		Start = raw_input("write start to start the next round write stop to finish")
		if(Start == "start"):
			change = getsome()
			P1 = change[0]
			P2 = change[1]
if(Start == "stop"):
	P1avg /= count
	P2avg /= count
	if(P1avg > P2avg):
		print("P1 Avg " + str(P1avg) + " P2 Avg " +str(P2avg))
		print("Player 1 Wins!")
	if(P2avg>P1avg):
		print("P1 Avg " + str(P1avg) + " P2 Avg " +str(P2avg))
		print("Player 2 Wins!")
	if(P1avg == P2avg):
		print("Draw!")
	if(P1avg == 42 or P2avg == 42):
		webbrowser.open(url)

