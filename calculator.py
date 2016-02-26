#foodcost = 35.98
#taxrate = .0975
#tiprate = .15

#mealcost = foodcost + (foodcost * taxrate) + (foodcost * tiprate)
#tipcost = foodcost * tiprate

#print (round(tipcost, 2))
#print (round(mealcost, 2))


def taxtipandtotal(foodcost, taxrate, tiprate):
	taxcost = foodcost * taxrate
	tipcost = foodcost * tiprate
	mealtotal = foodcost + (foodcost * taxrate) + (foodcost * tiprate)

	print(taxcost, tipcost, mealtotal)

taxtipandtotal(35.98, .0975, .15)