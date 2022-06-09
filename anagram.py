str1=input("enter the string 1:")
str2=input("enter the string 2:")
str1_l=str1.lower()
str2_l=str2.lower()
if (sorted(str1_l) == sorted(str2_l)):
	print("given string is anagram")
else:
	print("given string is not anagram")
