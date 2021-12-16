"""
    @File :   retrieve_element.py
    @Author : mukul
    @Date :   16-12-2021
"""

list1 = ['Maruti', 20.56, 'Tata', 3000, 'Honda', 20+5j]
print(list1)

""" Positive Index Slicing """
print(list1[2:5])
print(list1[:3])
print(list1[1:])
print(list1[2:5:2])

""" Negative Index Slicing """
print(list1[-4:-1])
print(list1[-4:])
print(list1[:-2])
print(list1[-5:-1:2])

""" Retrieve elements from list using for loop """
for item in list1:
    print(item)
