"""
    @File :   remove_element.py
    @Author : mukul
    @Date :   16-12-2021
"""

set1 = {'Maruti', 20.56, 'Tata', 3000, 'Honda', 20+5j}
print(set1)
"""
    discard(element) -> remove element from set without raising any error
    remove(element) -> remove element from set
    pop() -> remove last element from set
    clear() -> remove all element from set
"""

set1.discard('Tata')
print(set1)

set1.remove(3000)
print(set1)

set1.pop()
print(set1)

set1.clear()
print(set1)
