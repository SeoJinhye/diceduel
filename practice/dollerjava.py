print("How much do you earn each hour?")
i = float(raw_input(">"))
print("How much hour did you work?")
H = float(raw_input(">"))

if(H > 40):
	H1 = H-40
	i1 =  i*1.5
	final = i*40 + H1 * i1
else:
	final = i*H

print(final)