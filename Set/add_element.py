"""
    @File :   add_element.py
    @Author : mukul
    @Date :   16-12-2021
"""

set1 = {'Maruti', 20.56, 'Tata', 3000, 'Honda', 20+5j}
print(set1)
"""
    add(element) -> add element in set
    update(element) -> update the set or add another set elements
"""

set1.add('Toyota')
print(set1)

set2 = [2154, 'Mahindra']
set1.update(set2)
print(set1)
