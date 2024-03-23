'''
Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name.
It should then accept an arbitrary number of keyword arguments.
Call the function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
'''

def car_company(manufacturer, model_name, **more_info):
    car_info = {}
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    for key, value in more_info.items():
        car_info[key] = value
    return car_info

car_info = car_company('subaru','outback',
                       color = 'red',
                       tow_package = 'True')
print(car_info)