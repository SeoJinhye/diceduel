def swap(x,y):
	z = x
	x = y
	y = z
	return (x,y)

values = [5,6,3,47,4,5,9]
x= 6
y = 10
x,y = swap(x,y)

values
valuesLength = len(values)-1
for count in range(valuesLength):
	if(count != valuesLength and values[count]>values[count+1]):
		(values[count], values[count+1]) = swap(values[count],values)
print(values)