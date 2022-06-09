def searchlinear(data, element):
	for i in range(len(data)):
		if data[i] == element:
			return True
	return False
print("Enter the valid search either Integer or String otherwise you will get NAME ERRORM for element")
search=input("Enter Integer for search of int else Enter String for str search:")
if (search=="Integer"):
	element=int(input("Enter the Integer:"))
elif (search=="String"):
	element=input("Enter the String:")
data=[1,2,"Ece","kd",5,8,4,"Python","Github",10]
if searchlinear(data, element):
	print("The input element ",element,"is found in the list")
else:
	print("The input element",element,"is not found in the list")
	

