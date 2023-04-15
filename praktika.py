weather_city = {'city': 'Москва', 'temperature': '20'}
print (weather_city['city'])
weather_city['temperature'] = int(weather_city['temperature']) + 5
print (weather_city['temperature'])
print (weather_city)
print (weather_city.get('country'))
weather_city['country'] = 'Россия'
print (weather_city)
weather_city['date'] = '27.05.2019'
print (weather_city)
print (len(weather_city))