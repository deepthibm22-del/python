#exception handling
#specific except block
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a/b)
except ValueError as e:
    print(e)
except NameError as e:
    print(e)
except ZeroDivisionError as e:
    
else:
    print('no errors found')
finally:
    print('execution completed')'''




#generric except code
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a/b)
    for i in range(1,500):
        print(i)
except KeyboardInterrupt:
    print('user wanted to stop')
except Exception as e:
    print(e)
else:
    print('no errors found')
finally:
    print('execution completed')'''


#bare/default except block
'''try:
    a=int(input("enter:"))
    b=int(input("enter:"))
    print(a/b)
    for i in range(1,1000):
        print(i)
except:
    print('error handled')
else:
    print('no errors found')
finally:
    print('execution completed')'''



#create our own errors
'''1.built-in error
2.coustom or user defined error
3.Asseration-->inbuilt error when we only call it it will come it is a builtin'''

#creating error for oddd number
'''class TypeError (Exception):
    pass
n=int(input("enter a number:"))
if n%2==0:
    print(n,'is even')
else:
    raise TypeError ('is it odd number')'''


#creating 
'''class NotPalindromeError(Exception):
    pass
s=input("enter a word:")
if s==s[::-1]:
    print(s,'it is a palindrome')
else:
    raise NotPalindromeError('it is not a palindrome')'''

#output
##enter a word:hii
##Traceback (most recent call last):
##  File "C:/Users/karth/OneDrive/Desktop/python/exception_handling.py", line 72, in <module>
##    raise NotPalindromeError('it is not a palindrome')
##NotPalindromeError: it is not a palindrome


'''rev=0
org=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
    if rev==org:
        print(num,'it is a palindrome')
    else:
        raise NotPalindromeError('it is not a palindrome')'''

#assertion error--> here, we assert keyword
'''if assert condition is true,'msg'
#statement block'''

#postive and negative number checking
'''n=int(input("enter a number:"))
assert n>0,'number is negative'
print('number is positive:',n**2)'''


#output
'''Traceback (most recent call last):
  File "C:/Users/karth/OneDrive/Desktop/python/exception_handling.py", line 103, in <module>
    assert n>0,'number is negative'
AssertionError: number is negative'''

#create bank class and to withdraw ,if withdraw money is greaetr than bal print error
class withdrawal(Exception):
    pass
n=int(input("enter amount:"))
bal=400
if bal>n:
    print(,'balance')
else:
    raise withdrawal('insuffcient balance')















    
