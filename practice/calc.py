print(''' Welcome to calculator 
Just type simple equation 
with two oprands and one operator.

Examples:
> 5+6
11

>8-2
6

>4*3
12

>6/3
02

''')

equation = raw_input(">")
firstnumber = int(equation[0])
seondnumber = int(equation[2])
if('+' == equation[1]):
	print(firstnumber + seondnumber)
if('-' == equation[1]):
	print(firstnumber - seondnumber)
if('/' == equation[1]):
	print(firstnumber / seondnumber)
if('*' == equation[1]):
	print(firstnumber * seondnumber)