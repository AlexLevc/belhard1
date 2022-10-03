# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
data = { 'Belarus': 'Minsk',
         'Russia': 'Moscow',
         }
search_town = input()
for country, town in data.items() :
    if town == search_town:
        print (country)