"""
    @File :   retrieve_key_and_value.py
    @Author : mukul
    @Date :   16-12-2021
"""

car_brand = {'Maruti': 2000, 'Tata': 3000, 'Honda': 5000}
print(car_brand)

""" 
    1. Retrieve the value of all keys from dictionary 
    2. Retrieve the key-value pair from dictionary using loop
    3. Retrieve all keys from dictionary
    4. Retrieve the value of a particular key from dictionary
"""
print(car_brand.values())

print(car_brand.keys())

print(car_brand.get("Maruti"))

for key, value in car_brand.items():
    print(f"{key} : {value}")
