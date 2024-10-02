#Module 3



#declare the variable and constants for this program
TAX = 0.06
numberofcoffee = 0
numberofmuffin = 0
numberofpizza = 0
numberofwine = 0
print('***************************************')
print('        My Coffee and Muffin Shop')
#Get input from the user
#I add pizza and wine to the menu
numberofcoffee  = int(input('Number of coffees bought :'))
numberofmuffin = int(input('Number of muffins bought :'))
numberofpizza  = int(input('Number of pizza bought :'))
numberofwine  = int(input('Number of wine bought :'))
print('***************************************')
#calculate the price
priceofcoffee = numberofcoffee * 5
priceofmuffin = numberofmuffin * 4
priceofpizza = numberofpizza * 15
priceofwine = numberofwine * 10
tax = (priceofcoffee + priceofmuffin + priceofpizza + priceofwine) * TAX
#display the receipt to the user
print('***************************************')
print('        My Coffee and Muffin Shop Receipt')
print(numberofcoffee, f'Coffee at $5 each :${priceofcoffee:.2f}' )
print(numberofmuffin, f'Coffee at $4 each :${priceofmuffin:.2f}' )
print(numberofpizza, f'pizza at $15 each :${priceofpizza:.2f}' )
print(numberofwine, f'wine at $10 each :${priceofwine:.2f}' )
print(f'6% tax :{tax:.2f}')
print('---------')
print(f'total :${priceofcoffee + priceofmuffin + priceofpizza + priceofwine + tax:.2f}')
print('***************************************')
