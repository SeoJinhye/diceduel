def getsome(word, num):
	Rword = ""
	for word in num:
		Rword = Rword+word
	return Rword


hi = getsome("That's Not Guud", 2)
print(hi)