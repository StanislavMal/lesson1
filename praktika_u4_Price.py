def format_price(price):
    price = int(price)
    cena = f'Цена:{price} руб.'
    return cena

price = format_price(56.24)
print (price)