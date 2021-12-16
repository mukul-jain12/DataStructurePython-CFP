"""
    @File :   tuple_methods.py
    @Author : mukul
    @Date :   16-12-2021
"""

"""
    A tuple is a collection which is ordered and unchangeable.
    So in tuple we cannot add, remove, update the elements
"""

tuple1 = ('Maruti', 20.56, 'Tata', 3000, 'Honda', 20+5j, 3000)
print(tuple1)

""" Retrieve index of a particular method using index() method """
print("Index of the element is : ", tuple1.index(20.56))

""" Retrieve the count of element in tuple """
print("Number of times 3000 came in tuple is :", tuple1.count(3000))
