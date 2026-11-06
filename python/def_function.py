#without args 


'''def sum():
    n1=int(input("enter:"))
    n2=int(input("enter:"))
    print(n1+n2)
   sum()
    '''

#wap to reverse a string
'''def reverse():
    s=input("enter the string:")
    rev=''
    for i in s:
        rev=i+rev
    print(rev)
reverse()'''


'''def reverse():
    s=input("enter the list:")
    rev=''
    r=list(reversed(s))
    ''.join(r)
    print(rev)'''

#second type of function with args

'''def add(n1,n2):
    print(n1+n2)
add(20,10)'''


#wap to find the factorial of a number

'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(5)'''
#using while loop

'''def factorial(n):
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
    print(fact)
factorial(5)'''

#3rd type of function
#function with arguments with return

'''def sum():
    n1=int(input("enter:"))
    n2=int(input("enter:"))
    return n1+n2,n1-n2
#print(sum())
a=sum()
print(a)'''

#wap to check wheather the number is prime or not
'''def is_prime():
    n=int(input("enter a number:"))
    for i in range(2,n):
        if n%i==0:
            return f'{n} is not prime'
    return f'{n} is a prime number'
print(is_prime())'''

#fourth type of functions
#with args with return

'''def sum(a,b):
    return a+b
print(sum(1,2))'''


#wap to remove duplicates from list
'''def remove_dup(l):
    out=[]
    for i in l:
        if i not in out:
            out.append(i)
    return out
print(remove_dup(eval(input("enter:"))))'''

'''print(remove_dup([1,2,2,3,4,5,5,6,7,8,9]))'''

#wap to find perfect number
def perfect_num(n):
    sum_factorial=0
    for i in range(1,n):
        if n%1==0:
            sum_factorial+=i
    return sum_factorial==n
    return True
##print(perfect_num(6)


#wap to strong number
'''def strong_num(n):
    sum=0
    temp=n
    while n>0:
        d=n%10
        fact=1
        for i in range(1,d+1):
            fact*=1
        sum+=fact
        n//=10
    return sum==temp''' 

# using for loop
'''def is_strong(n):
    sum=0
    for d in str(n):
        fact=1
        for i in range(1,int(d)+1):
            fact*=i
        sum+=fact
    return sum==n'''

#using nested function we can generate a strong number
'''def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
def is_strong(n):
    sum=0
    for d in str(n):
        sum+=factorial(int(d))
    return sum==n

#wap to print the strong numbers between 1 to 10000
# imp : to execute this uncomment above one
def strong_numbers():
    for i in range(1,500001):
        if is_strong(i):
            print(i)'''

'''def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True


#wap to print the prime numbers between 1 to 1000

def prime_numbers():
    for i in range(1,1001):
        if is_prime(i):
            print(i)'''

#wap to print the perfect numbers between 1 to 1000

'''def perfect_numbers():
    for i in range(1,1001):
        if perfect_num(i):
            print(i)'''

#wap to print the arm strong numbers between 1 to 1000
def arm_strong(n):
    temp=n
    sum=0
    l=len(str(n))
    while n>0:
        d=n%10
        sum+=d**l
        n=n//10
    if sum==temp:
        return true
    return false

def armstrong_numbers():
    
    
    
    



     

  


        
 

    
    

 

