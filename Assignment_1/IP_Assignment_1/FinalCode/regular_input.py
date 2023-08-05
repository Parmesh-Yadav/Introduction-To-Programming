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
print(l)

