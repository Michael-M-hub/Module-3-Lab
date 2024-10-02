#Module 3




TAX = 0.06
numberofcoffee = 0
numberofmuffin = 0
print('***************************************')
print('        My Coffee and Muffin Shop')
numberofcoffee  = int(input('Number of coffees bought :'))
numberofmuffin = int(input('Number of muffins bought :'))
print('***************************************')
priceofcoffee = numberofcoffee * 5
priceofmuffin = numberofmuffin * 4
tax = (priceofcoffee + priceofmuffin) * TAX
print('***************************************')
print('        My Coffee and Muffin Shop Receipt')
print(numberofcoffee, f'Coffee at $5 each :${priceofcoffee:.2f}' )
print(numberofmuffin, f'Coffee at $4 each :${priceofmuffin:.2f}' )
print(f'6% tax :{tax:.2f}')
print('---------')
print(f'total :${priceofcoffee + priceofmuffin + tax:.2f}')
print('***************************************')
