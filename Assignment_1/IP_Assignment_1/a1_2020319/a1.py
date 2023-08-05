'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.

- Feel free to add new helper functions, but DO NOT modify/delete the given functions. 

- You MUST complete the functions defined below, except the ones that are already defined. 
'''


def show_menu():

	from tabulate import tabulate
	list = [[0,'Tshirt','Apparels',500],[1,'Trousers','Apparels',600],[2,'Scarf','Apparels',250],[3,'Smartphone','Electronics',20000],[4,'iPad','Electronics',30000],[5,'Laptop','Electronics',50000],[6,'Eggs','Eatables',5],[7,'Chocolate','Eatables',10],[8,'Juice','Eatables',100],[9,'Milk','Eatables',45]]
	table = tabulate(list, headers=['CODE','DISCRIPTION','CATEGORY','COST(Rs)'])
	print(table)

def get_regular_input():
	'''
	Description: Takes space separated item codes (only integers allowed). 
	Include appropriate print statements to match the output with the 
	screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i. 
	'''
	l_ = []
	l = [0,0,0,0,0,0,0,0,0,0]
	print('--------------------------------------------------------------------')
	print('ENTER ITEMS YOU WISH TO BUY')
	print('--------------------------------------------------------------------')
	items = input('Enter the item codes (space-separated:)')
	print()
	l_ = items.split(' ')
	for i in l_:
		if i.isalpha() or int(i) < 0 or int(i) > 9:
			print('Item skipped - Invalid Input =',i)
		else:
			l[int(i)] = l[int(i)] + 1
	return l



def get_bulk_input():
	'''
	Description: Takes inputs (only integers allowed) from a bulk buyer. 
	For details, refer PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: No parameters
	
	Returns: Returns a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	'''
	l_ = []
	l = [0,0,0,0,0,0,0,0,0,0]
	a = {0:'Tshirt',1:'Trousers',2:'Scarf',3:'Smartphone',4:'iPad',5:'Laptop',6:'Eggs',7:'Chocolate',8:'Juice',9:'Milk'}
	while True:
		item = input('Enter code and quantity (leave blank to stop):')
		if item == '':
			print('Your order has been finalized')
			break
		else:
			l_ = item.split(' ')
			if l_[1].isalpha() or l_[0].isalpha():
				print('Invalid Quantity. Try again')
			else:
				if int(l_[0]) < 0 or int(l_[0]) > 9 or int(l_[1]) <= 0:
					print('Invalid Quantity. Try again')
				else:
					l[int(l_[0])] = l[int(l_[0])] + int(l_[1])
					print('You added',int(l_[1]),a[int(l_[0])])
					print()
	return l 



def print_order_details(quantities):
	'''
	Description: Prints the details of the order in a manner similar to the
	sample given in PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: No return value
	'''
	a = {0:'Tshirt',1:'Trousers',2:'Scarf',3:'Smartphone',4:'iPad',5:'Laptop',6:'Eggs',7:'Chocolate',8:'Juice',9:'Milk'}
	c = {0:500,1:600,2:250,3:20000,4:30000,5:50000,6:5,7:10,8:100,9:45}
	print('--------------------------------------------------------------------')
	print('ORDER DETAILS')
	print('--------------------------------------------------------------------')
	b = 1
	for i in range(10):
		if quantities[i] != 0:
			print('[',b,']',a[i],'x',quantities[i],'=','Rs',c[i],'*',quantities[i],'= Rs',c[i]*quantities[i])
			b += 1
			
	


def calculate_category_wise_cost(quantities):
	'''
	Description: Calculates the category wise cost using the quantities
	provided. Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes a list of integers of length 10, where the i_th
	element represents the quantity of the item with item code i.
	
	Returns: A 3-tuple of integers in the following format: 
	(apparels_cost, electronics_cost, eatables_cost)
	'''
	a_c,e_c,ea_c = 0,0,0
	a = {0:'Apparels',1:'Apparels',2:'Apparels',3:'Electronics',4:'Electronics',5:'Electronics',6:'Eatables',7:'Eatables',8:'Eatables',9:'Eatables'}
	c = {0:500,1:600,2:250,3:20000,4:30000,5:50000,6:5,7:10,8:100,9:45}
	for i in range(10):
		if quantities[i] != 0:
			if a[i] == 'Apparels':
				a_c = a_c + c[i]*quantities[i]
			elif a[i] == 'Electronics':
				e_c = e_c + c[i]*quantities[i]
			else:
				ea_c = ea_c + c[i]*quantities[i]
	print('--------------------------------------------------------------------')
	print('CATEGORY-WISE COST')
	print('--------------------------------------------------------------------')
	print('Apparels =', a_c)
	print('Electronics =', e_c)
	print('Eatables =', ea_c)
	cws = (a_c,e_c,ea_c)
	return cws





def get_discount(cost, discount_rate):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- discount_rate: Float: 0 <= discount_rate <= 1

	Returns: The discount on the cost provided.
	'''
	return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the discounted category-wise price, if applicable. 
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables'
	
	Returns: A 3-tuple of integers in the following format: 
	(discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost). 
	'''
	a_d,e_d,ea_d = 0,0,0
	if apparels_cost >= 2000:
		a_d = get_discount(apparels_cost,0.1)
	if electronics_cost >= 50000:
		e_d = get_discount(electronics_cost,0.1)
	if eatables_cost >= 500:
		ea_d = get_discount(eatables_cost,0.1)
	dac = apparels_cost - a_d
	dec = electronics_cost - e_d
	deac = eatables_cost - ea_d
	td = a_d + e_d + ea_d
	tc = dac + dec + deac
	print('--------------------------------------------------------------------')
	print('DISCOUNT')
	print('--------------------------------------------------------------------')
	if a_d != 0:
		print('[APPAREL] Rs',apparels_cost,'- Rs',a_d,'= Rs',dac)
	if e_d != 0:
		print('[ELECTRONICS] Rs',electronics_cost,'- Rs',e_d,'= Rs',dec)
	if ea_d != 0:
		print('[EATABLES] Rs',eatables_cost,'- Rs',ea_d,'= Rs',deac)
	print()
	print('TOTAL DISCOUNT = Rs',td)
	print('TOTAL COST = Rs',tc)
	tcad = (dac,dec,deac)
	return tcad


def get_tax(cost, tax):
	'''
	Description: This is a helper function. DO NOT CHANGE THIS. 
	This function must be used whenever you are calculating discounts.
	
	Parameters: Takes 2 parameters:
	- cost: Integer
	- tax: 	Float: 0 <= tax <= 1

	Returns: The tax on the cost provided.
	'''
	return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
	'''
	Description: Calculates the total cost including taxes.
	Include appropriate print statements to match the output with the
	screenshot provided in the PDF.
	
	Parameters: Takes 3 integer parameters:
	- apparels_cost: 	cost for the category 'Apparels'
	- electronics_cost: cost for the category 'Electronics'
	- eatables_cost: 	cost for the category 'Eatables' 
	
	Returns: A 2-tuple of integers in the following format: 
	(total_cost_including_tax, total_tax)
	'''
	a_t,e_t,ea_t = 0,0,0
	a_t = get_tax(apparels_cost,0.10) 
	e_t = get_tax(electronics_cost,0.15)
	ea_t = get_tax(eatables_cost,0.05)
	tt = a_t + e_t + ea_t
	tcit = apparels_cost + electronics_cost + eatables_cost + tt
	print('--------------------------------------------------------------------')
	print('TAX')
	print('--------------------------------------------------------------------')
	if a_t != 0:
		print('[APPAREL] Rs',apparels_cost,'* 0.10 = Rs',a_t)
	if e_t != 0:
		print('[ELECTRONICS] Rs',electronics_cost,'* 0.15 = Rs',e_t)
	if ea_t != 0:
		print('[EATABLES] Rs',eatables_cost,'* 0.05 = Rs',ea_t)
	print()
	print('TOTAL TAX = Rs',tt)
	print('TOTAL COST = Rs',tcit)
	tcat = (tcit,tt)
	return tcat
	

	


def apply_coupon_code(total_cost):
	'''
	Description: Takes the coupon code from the user as input (case-sensitive). 
	For details, refer the PDF. Include appropriate print statements to match 
	the output with the screenshot provided in the PDF.
	
	Parameters: The total cost (integer) on which the coupon is to be applied.
	
	Returns: A 2-tuple of integers:
	(total_cost_after_coupon_discount, total_coupon_discount)
	'''
	print('--------------------------------------------------------------------')
	print('COUPON CODE')
	print('--------------------------------------------------------------------')
	total_cost1 = total_cost
	disc = 0
	while True:
		cc_ = input('Enter Coupon Code (Else leave blank):')
		if cc_ == '':
			print('No coupon code applied')
			print()
			print('TOTAL COUPON DISCOUNT = Rs 0')
			print("TOTAL COST = Rs",total_cost)
			break
		elif cc_ != 'HELLE25' and cc_ != 'CHILL50':
			print('Invalid coupon code. Try Again')
		elif cc_ == 'HELLE25':
			if total_cost >= 25000:
				disc = total_cost * 0.25
				if disc <= 5000:
					total_cost = total_cost - disc
				else:
					disc = 5000
					total_cost = total_cost - disc
			else:
				print('Coupon Code Not Applicable on this order')
			print('[HELLE] min(5000, Rs',total_cost1,'* 0.25) = Rs',disc)
			print('TOTAL COUPON DISCOUNT = Rs', disc)
			print("TOTAL COST = Rs",total_cost)
			break
		elif cc_ == 'CHILL50':
			if total_cost >= 50000:
				disc = total_cost * 0.50
				if disc <= 10000:
					total_cost = total_cost - disc
				else:
					disc = 10000
					total_cost = total_cost - disc
			else:
				print('Coupon Code Not Applicable on this order')
			print('[CHILL50] min(10000, Rs',total_cost1,'* 0.50) = Rs',disc)
			print('TOTAL COUPON DISCOUNT = Rs', disc)
			print("TOTAL COST = Rs",total_cost)
			break
	tcacd = total_cost
	tcd = disc
	tcicd = (tcacd,tcd)
	return(tcicd)

			

	


def main():
	'''
	Description: This is the main function. All production level codes usually
	have this function. This function will call the functions you have written
	above to design the logic. You will see how splitting your code into specialised
	functions makes the code easier to read, write and debug. Include appropriate 
	print statements to match the output with the screenshots provided in the PDF.
	
	Parameters: No parameters
	
	Returns: No return value
	'''
	print('--------------------------------------------------------------------')
	print('                              MY BAZAAR                             ')
	print('--------------------------------------------------------------------')
	print()
	print()
	print('Hello! Welcome to my gorcery store!\n\nFollowing are the products available in the shop:')
	print()
	print()
	show_menu()
	print()
	print()
	cob = input('Would you like to buy in bulk?(y or Y/ n or N)')
	print()
	print()
	if cob == 'y' or cob == 'Y':
		order = get_bulk_input()
		#print(order)#delete later
	elif cob == 'n' or cob == 'N':
		order = get_regular_input()
		#print(order)#delete later
	else:
		print('Invalid Input')
	print()
	print()
	print_order_details(order)
	print()
	print()
	cws_ = calculate_category_wise_cost(order)
	#print(cws_)#delete later
	print()
	print()
	tcad = calculate_discounted_prices(cws_[0],cws_[1],cws_[2])
	#print(tcad)#delete later
	print()
	print()
	tcat = calculate_tax(tcad[0],tcad[1],tcad[2])
	#print(tcat)#delete later
	print()
	print()
	tcacd = apply_coupon_code(tcat[0])
	print()
	print()
	print('Thank you for visiting')
	
	




if __name__ == '__main__':
	main()
