#wap to print the number from 1 t0 5
'''i=1
while i<=10:
    print(i)
    i=i+1'''
#wap to print the number from 1 t0 5
'''i=10
while i>=1:
    print(i)
    i=i-1'''

#wap tp print the even number between 1 to n
'''n=int(input('enter the n:'))
i=1
while i<=n:
    if i%2==0:
        print(i)
    i=i+1 or

n=int(input('enter the n:'))
i=2
while i<=n:
    print(i)
    i=i+2'''

#wap to print the factors of a number
'''n=int(input("enter the number:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i=i+1 or'''


'''n=int(input("enter the number:"))
i=1
while i<=n/2:
    if n%i==0:
        print(i)
    i=i+1
print(n)'''

#wap to find the sum of n natural numbers
'''n=int(input("enter the number:")'''


#wap to find the product of n natural number or factorial of a number
'''n=int(input("enter the number:"))
prod=1
i=2
while i<=n:
    prod=prod*i
    i=i+1
print(prod)'''

#wap to  print the multiplication table of a given number
'''n=int(input("enter the number:"))
i=1
while i<=10:
    print(f'{n}*{i}={n}*{i}')
       i=i+1'''

#wap to check number is perfect number or not
'''n=int(input("enter the number:"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum+=i
    i=i+1
if sum==n:
    print("perfect number")'''

#wap to count the number of digits present in number
'''n=int(input("enter the digit"))
count=0
while n>0:
    count+=1
    n=n//10
print(count)'''

#wap to reverse a number
'''n=int(input("enter the digit:"))
reverse=0
while n>0:
    d=n%10
    reverse=(reverse*10)+d
    n=n//10
print(reverse,"reversed")'''


#wap to reverse a number an palindrome
'''n=int(input("enter the digit:"))
temp=n
reverse=0
while n>0:
    d=n%10
    reverse=(reverse*10)+d
    n=n//10
if reverse==temp:
    print("palindrome")'''

#wap to convert an int to binary
'''n=int(input("enter the digit:"))
i=0
q=0
while n>0:
    d=n%2
    q=n//2
    i=+d
print(i)'''

#wap to convert an binary to int
'''binary=int(input("enter the digit:"))
i=0
d=1
while binary>0:
    digit=binary%10
    i=i+digit*d
    d=d*2
    binary=binary//10
print(i)'''

#wap to extract the char present in at even index
'''n=input("enter the string:")
i=0
em=''
while i<=len(n)-1:
    if i%2==0:
        em=em+n[i]
    i=i+1
print(em,"string extracted")'''

#wap to extract vowels present in a string
'''n=input("enter the string:")
i=0
em=''
while i<=len(n)-1:
    if n[i] in 'aeiouAEIOU':
        em=em+n[i]
    i+=1
print(em,"vowels present")'''
#wap to get the following output
#s1='00110101101'
#s2='01011010101'
#out=5
'''n1=input("enter the string1:")
n2=input("enter the string2:")
i=0
count=0
while i<=len(n1)-1:
    if i<=len(n2)-1:
        if n1[i]==n2[i]:
            count=count+1
    i=i+1
print("count:",count) space will be wasted
or'''
'''n1=input("enter the string1:")
n2=input("enter the string2:")
i=0
count=0
while i<=len(n1)-1 and i<=len(n2)-1:
        if n1[i]==n2[i]:
            count=count+1
        i=i+1
print("count:",count)'''


#wap to replace the space present in a string by *
'''n=input("enter the string:")
i=0
new_str=''
while i<=len(n)-1:
    if n[i]==' ':
        new_str=new_str+'*'
    else:
        new_str=new_str+n[i]
    i+=1
print(new_str,"is a new string")'''

#wap to check wheather the number is armstroung or not

     
    
    









      
