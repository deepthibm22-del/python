#lambda
'''add=lambda a,b:a+b
print(10,20)
'''

#map()-->it applies the given functionn to each and every value present in a n itearable
'''l=[1,2,3,4,5]
square=lambda num:num**2
out=map(square,l)
print(list(out))'''


#filter
'''even=lambda num:num%2==0
out=filter(even,l)
print(list(out))'''

#comprehension
a=[3 for i in (1,2,3)]
print(a)
