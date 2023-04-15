def discounted(price, discount):# def - это функция
    price = abs(float(price)) # abs - приводит к абсолютному значению, (по модулю), тем самым игнорируем отрицательные значения.
    discount = abs(float(discount)) # float - приводит к вещественному числу
    if discount >= 100:
        price_with_discout = price
    else:
        price_with_discout = price - price * discount/100
    print (price_with_discout)
    return price_with_discout

product = {
	'name':'iPhone 10',
	'stock': '5',
	'price': 50000.0,
	'discount': 50
    }

product['with_diskount'] = discounted(product['price'], product['discount'])

print (product)