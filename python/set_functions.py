Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/pollution/SQL PENTAGON/python/function set.py
>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__',
 '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__',
 '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear',
 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
 'symmetric_difference_update', 'union', 'update']
>>> 
>>> 
>>> s1={1,2,3}
>>> s2={4,2,6}
>>> s1.difference(s2)
{1, 3}
>>> s1
{1, 2, 3}
>>> s1.difference_update(s2)
>>> s1
{1, 3}
>>> s2
{2, 4, 6}
>>> s1.discard(3)
>>> s1
{1}
>>> s2.remove(6)
>>> s2
{2, 4}
>>> s1.discard(5)
>>> s1
{1}
>>> s1.remove(5)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s1.remove(5)
KeyError: 5
>>> s1.discard(3)
>>> s1={1,2,3,4,5,100,6}
>>> s2={5,3,7,8,9}
>>> s1.intersection(s2)
{3, 5}
>>> s1.isdisjoint(s2)
False
>>> t1={1,2,3}
>>> t2={4,5,6}
>>> t1.isdisjoint(t2)
True
>>> True
True



