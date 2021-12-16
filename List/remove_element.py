"""
    @File :   remove_element.py
    @Author : mukul
    @Date :   16-12-2021
"""

list1 = ['Maruti', 20.56, 'Tata', 3000, 'Honda', 20+5j]
print(list1)

""" Remove the element from the list remove() """
list1.remove('Maruti')
print(list1)

""" Remove the element from the list using pop() """
list1.pop(3)
print(list1)

""" Remove all elements from the list using clear() """
list1.clear()
print(list1)
