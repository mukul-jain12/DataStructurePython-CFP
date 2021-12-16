"""
    @File :   remove_pair
    @Author : mukul
    @Date :   16-12-2021
"""

car_brand = {'Maruti': 2000, 'Tata': 3000, 'Honda': 5000}
print(car_brand)

""" Remove key-value pair from dictionary using pop() """
car_brand.pop('Tata')
print(car_brand)

""" Remove key-value pair from dictionary using del """
del car_brand['Maruti']
print(car_brand)
