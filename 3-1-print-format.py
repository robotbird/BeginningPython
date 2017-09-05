width = input('Please enter width: ')
price_width = 10
item_width = width - price_width
header_format = '%-*s%*s'
format1        = '%-*s%*.2f'

print '=' * width
print header_format % (item_width,'Item',price_width, 'Price')
print '-' * width
print format1 % (item_width, 'Apples',price_width,0.4)
print format1 % (item_width, 'Pears',price_width,0.5)
