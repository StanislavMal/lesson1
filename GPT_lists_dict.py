products = [
    {'name': 'iPhone 10', 'stock': 5, 'price': 120000.0},
    {'name': 'Samsung Galaxy S21', 'stock': 10, 'price': 110000.0},
    {'name': 'Xiaomi Redmi Note 10', 'stock': 7, 'price': 30000.0},
    {'name': 'Huawei P40 Pro', 'stock': 3, 'price': 80000.0}
]

print('Исходный список продуктов:')
print(products)

# Сортируем список по возрастанию цены
products.sort(key=lambda x: x['price'])

print('Список продуктов, отсортированный по возрастанию цены:')
print(products)

# Подсчитываем количество продуктов с именем "iPhone 10"
count_iphone = 0
for product in products:
    if product['name'] == 'iPhone 10':
        count_iphone += 1

print('Количество продуктов iPhone 10: ', count_iphone)

# Удаляем два элемента из списка
del products[0]
del products[1]

print('Список продуктов после удаления двух элементов:')
print(products)
