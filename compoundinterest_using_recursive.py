#recursive function for finding coumpound interest 
def compound_interest(product,rate,n,t,power):
	if power==0:
		return product
	product=product*(1+(rate/(100*n)))
	return compound_interest(product,rate,n,t,(power-1))
#Enter the input values to calculate compound interest
principle_amount=int(input("enter the principle amount:"))
rate=int(input("enter the rate of interest:"))
n=int(input("enter the terms of pay per year:"))
t=int(input("enter the no of years:"))
#apply formula ci=A-p , A=p*((1+(r/100*n))**(n*t))
#recursive function is used to calculate (1+(r/100*n))**(n*t)
prod_value=compound_interest(1,rate,n,t,(n*t))
final_amount=prod_value*principle_amount
compoundinterest=final_amount-principle_amount
#print compound interest
print(compoundinterest,"is the compound interest")
