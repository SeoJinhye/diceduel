import random
import pygame
from pygame import mixer
P1 = random.randint(1,6)
P2 = random.randint(1,6)
P1win = 0
P2win = 0

mixer.init()
s = mixer.Sound('bgm.wav')
Start = raw_input("write start to start the game")

if(Start == "start"):
	s.play()
	while(P1win != 3 or P2win != 3):
		print("P1 got:" + str(P1) + " P2 got:" + str(P2))
		if(P1 > P2):
			print("Player 1 wins this round")
			P1win+=1
		if(P2 > P1):
			print("Player 2 wins this round")
			P2win+=1
		if(P1 == P2):
			print("draw!")
			
		if(P1win == 3 or P2win == 3):
			break
		print("Current score: " + str(P1win) + " : " +str(P2win))
		Start = raw_input("write start to start the game")
		if(Start == "start"):
			s.play()
			P1 = random.randint(1,6)
			P2 = random.randint(1,6)
	if(P1win > P2win):
		print("Final Score: " + str(P1win) + " : " +str(P2win))
		print("Player 1 wins!")
	if(P2win>P1win):
		print("Final score: " + str(P1win) + " : " +str(P2win))
		print("Player 2 wins!")