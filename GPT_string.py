# объявление строки
string = "Python is a high-level programming language that is widely used in different areas of computer science and beyond."

# вывести строку
print(string)

# длина строки
print(len(string))

# индекс первого вхождения символа "a"
print(string.index('a'))

# количество вхождений подстроки "Python"
print(string.count('Python'))

# разделить строку по символу " "
words = string.split(' ')
print(words)

# соединить список слов в одну строку через пробел
new_string = ' '.join(words)
print(new_string)

# привести строку к верхнему регистру
print(string.upper())

# привести строку к нижнему регистру
print(string.lower())

# заменить все вхождения подстроки "programming language" на "language for programming"
new_string = string.replace('programming language', 'language for programming')
print(new_string)
