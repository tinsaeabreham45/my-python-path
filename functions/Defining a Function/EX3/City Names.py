'''
Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned
'''


def city_country(city, country):
    return f'"{city.title()}, {country.title()}"'


location1 = city_country('addis ababa', 'ethiopia')
location2 = city_country('mombasa', 'kenya')
location3 = city_country('mombai', 'india')

print(location1)
print(location2)
print(location3)
