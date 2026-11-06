

##############################

#simple - if

#q4. wap to print the cube of a number only if it is divisible by 9 or 6
'''
n=int(input('enter to check divisibility by 9 or 6:'))
if n%9==0 or n%6==0:
    print(f"Cube of {n} is {n**3}")
'''

#q5. Wap to check whether the given integer is 3 Digit number.
'''
n=int(input('Enter to check whether digit is 3 digit:'))
if len(str(n))==3:
    print('it is a 3 digit number')
'''

#q6. Wap to check whether the last digit of a given number is 5.
'''
n=int(input('Enter a no. to check its last digit is 5:'))
if n%10==5:
    print('last digit is 5')
'''
    

#q7. Wap to check whether the given data is float.
'''
n=input('Enter a number to check if its float')
if type(n)==float:
    print('It is float')
'''


    
#q8. Wap to check whether the data is single value data.
'''
n=eval(input('Enter to check if is SVD:'))
if type(n)==float or type(n)==int or type(n)==bool or type(n)==complex:
    print("It is a single value data")
'''

#q10.Wap to check whether the given integer is multiple of 3.
'''
n=int(input('Enter a no to check if it is multiple of 3'))
if n%3==0:
    print('It is a multiple of 3')
'''

##########################

#if-else

#q18.Consider a tuple of length 2 and check whether the tuple is homogenous or not
'''
t=eval(input('Enter a tuple:'))
if type(t[0])==type(t[1]):
    print('It is a homogeneous')
else:
    print('It is not homogeneous')
'''


##############################


#elif

#q22. wap to check whether the given integer is single digit or 2 or 3 or or more than 3 digits
'''
n=int(input('enter an integer:'))
if len(str(n))==1:
    print('It is a 1 digit number')
elif len(str(n))==2:
    print('It is a 2 digit number')
elif len(str(n))==3:
    print('It is a 3 digit number')
else:
    print('It is more than 3 digit number')
'''


#q25. wap to find the smallest of 3 numbers
'''
print('To find the smalles number')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
if a<b and a<c:
    print(a,'is smallest')
elif b<c:
    print(b,'is smallest')
else:
    print(c,'is smallest')
'''    
    
#q26 wap to check the relation between 2 integer numbers
'''
print('To find the relation between 2 numbers')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
if a>b:
    print(f'{a} is greater than {b}')
elif a<b:
    print(f'{a} is greater than {b}')
else:
    print(f'{a} is equal to {b}')
'''
    
#q27. wap to convert lower to upper, upper to lower, if digit print its remainder divided by 3,
#if it is special print its ascii
'''
c=input('Enter a character:')
if 'a'<=c<='z':
    print(chr((ord(c))-32))
elif 'A'<=c<='Z':
    print(chr(ord(c)+32))
elif '0'<=c<='9':
    print(int(c)%3)
else:
    print('ascii of',c,'is',ord(c))
'''


####################
#nested if


#q29. Wap to login into the Instagram with valid username and password.(enter
# password only if the user name is valid
'''
username='abc'
password='abc123'
print('Login to Instagram:')
u=input('Username:')
if u==username:
    p=input('Password:')
    if p==password:
        print('Logged in successfully')
    else:
        print('Invalid password!')
else:
    print('Invalid username!')
'''

#q32.Wap to find the greatest of 4 numbers
'''
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
d=int(input('Enter 4th number:'))

if a>b and a>c and a>d:
    print(a,'is greatest')
elif b>c and b>d:
    print(b,'is greatest')
elif c>d:
    print(c,'is greatest')
else:
    print(d,'is greatest')
'''

#q33.  Wap to print the value as it is only if the length of the value is even.
'''
n=int(input('Enter:'))
if len(str(n))%2==0:
    print(n)
'''

#q34. Wap to print the last value of a list only if it is palindrome string starting with vowel.
'''
l=eval(input('Enter a list:'))
if type(l[-1])==str:
    if l[-1][0] in 'aeiouAEIOU':
        if l[-1]==l[-1][::-1]:
            print(l[-1])
        else:
            print('Not a palindrome')
    else:
        print('Not starting with a vowel')
else:
    print('Not a string')
'''

#q35. Wap to print the reversed string only if it is starting with vowel ,ending with consonant and having a middle value.
'''
s=input('Enter a string:')
if len(s)%2==1:
    if ('a'<=s[0]<='z' or 'A'<=s[0]<='Z') and ('a'<=s[-1]<='z' or 'A'<=s[-1]<='Z'):
        if s[0] in 'aeiouAEIOU':
            if s[-1] not in 'aeiouAEIOU':
                print('Reversed string:',s[::-1])
            else:
                print('not ending with consonant')
        else:
            print('not starting with vowel')
    else:
        print('not starting or ending with alphabet')
else:
    print('it does not have middle value')
'''
#q36. Wap to find the second greatest of 4 values.-?
''' #THIS IS NOT COMPLETED -ONLY ROUGH WORK
print('To find 2nd greatest of 4 numbers')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
d=int(input('Enter 4th number:'))

abcd
b a
a b
c

if a>b:
    if a>c:
        if a>d:
            print(a)
        else:
            print(d)
    elif c>d:
        print(c)
    else:
        print(d)
elif 



if a>=b and a>=c and a>=d:
    print(a)
elif b>=c and


if b>=a or c>=a or d>=a:
    print(a)
elif 
    
if b>=c and b>=d:
    if b>a:
        print(b)
    else:
        print(a)
elif c>=d and c>=a:
    if c>b:
        print(c)
    else:
        print(b

a b c d
'''
#q37. Wap to find the smallest of 4 numbers.
'''
print('To find smallest of 4 numbers')
a=int(input('Enter 1st number:'))
b=int(input('Enter 2nd number:'))
c=int(input('Enter 3rd number:'))
d=int(input('Enter 4th number:'))
print('smallest:',end='')
if a<=b and a<=c and a<=d:
    print(a)
elif b<=c and b<=d:
    print(b)
elif c<=d:
    print(c)
else:
    print(d)
'''

#q38. Write a program to print middle Character of the given string only if it is upper Case Charact
'''
s=input('Enter a string:')
if len(s)%2==1:
    if 'a'<=s[len(s)//2]<='z' or 'A'<=s[len(s)//2]<='Z':
        if 'A'<=s[len(s)//2]<='Z':
            print(s[len(s)//2])
        else:
            print('mid char is not upper case')
    else:
        print('mid char is not an alphabet')
else:
    print('there is no middle char')
'''


##################################

#while loop

#q44. Wap to print all the characters of a string
'''
print('to print all the characters of a string')
s=input('enter a string:')
i=0
while i<len(s):
    print(s[i])
    i=i+1
'''

#45.Wap to print all the characters present at even index of a string.
'''
print('to print all the characters present at even index of a string.')
s=input('enter  a string:')
i=0
while i<len(s):
    if i%2==0:
        print(s[i])
    i=i+1
'''

#46.Wap to extract all the lowercase characters present in a string.
'''
print('to extract all the lowercase characters present in a string.')
s=input('enter a string:')
i=0
out=''
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=s[i]
    i=i+1
print('string after extracting only lowercase characters:',out)
'''

#49.Wap to toggle a string.
'''
print('to toggle a string')
s=input('enter a string to toggle it:')
i=0
out=''
while i<len(s):
    if 'a'<=s[i]<='z':
        out+=chr(ord(s[i])-32)
    elif 'A'<=s[i]<='Z':
        out+=chr(ord(s[i])+32)
    else:
        out+=s[i]
    i+=1
print('toggled string:',out)
'''

#53.Wap to login to phonepe by entering correct otp.-?
'''
otp='2412'
p=input('enter otp to login to phonepe:')
if p==otp:
    print('logged in successfully')
else:
    print('loign unsuccessful')
'''

#54.Wap to run infinite loop until user enters the correct password
'''
otp='4211'

while otp!=p:
    p=input('Enter otp:')
print('logged in successfully')
'''

#55.Wap to extract all the even integers present in a tuple at odd index.
'''
t=eval(input('Enter a tuple:'))
i=0
l=[]
while i<len(t):
    if t[i]%2==0:
        l.append(t[i])
    i+=1
print(tuple(l))
'''

#56.Wap to remove duplicates from a list without converting into set.
'''
l=eval(input('Enter a list to remove duplicates:'))
out=[]
i=0
while i<len(l):
    if l[i] not in out:
        out.append(l[i])

    i+=1
print(out)
'''

#57.Wap to find the sum of all the odd numbers between the given range
'''
start=int(input('enter start of range:'))
end=int(input('enter end of range:'))
i=start
sum=0
while i<=end:
    if i%2==1:
        sum+=i
    i+=1
print(sum)
'''

#58.Wap to find the greatest number in a given list of integers.
'''
l=eval(input('Enter a list of integers to find the greatest number:'))
greatest=l[0]
i=0
while i<len(l):
    if l[i]>greatest:
        greatest=l[i]
    i+=1
print('greatest is:',greatest)
'''

#59.Wap to find the sum of cube of a number in a string.-? all numbers or only one digit?
'''
s=input('enter  a string containing a number:',)
i=0
sum=0
while i<len(s):
    if '0'<=s[i]<='9':
        sum=sum+int(s[i])**3
    i+=1
print('sum of all numbers in string:',sum)
'''

#62.Wap to check the given number is prime or not.(while loop)
'''
n=int(input('enter to check for prime:'))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print('it is prime')
else:
    print('it is not prime')
'''

#64.Wap to find the HCF of two numbers.
'''
a=int(input('enter num 1:'))
b=int(input('enter num 2:'))
i=1
hcf=1
while i<=a//2 and i<=b//2:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1
print('hcf:',hcf)
'''

#67.Wap to count the number of words in a string.
'''
s=input('Enter a sentence:')
count=0
i=0
while i<len(s):
    print(s[i],end='')
    if s[i]==' ':
        count+=1
    i+=1
print('count of words:',count+1)
'''

#68.Wap to guess the number.
'''
n=132
print('guess the number')
num=int(input('enter your guess:'))
while num!=n:
    num=int(input('try again:'))
print('correct!')
'''

#69.Wap to find the common elements in two sets -?cos set cant be indexed
'''
s1=eval(input('enter set1:'))
s2=eval(input('enter set2:'))
print('common elements:',s1&s2)
'''

#70.Wap to find the product of all the digits present in a number.
'''
n=int(input('enter a number:'))
prod=1
while n>0:
    d=n%10
    prod=prod*d
    n=n//10
print('product of digits:',prod)
'''


############################

#for loop

#71.Wap to print all the integers present in a list.
'''
l=eval(input('enter a list:'))
for i in l:
    if type(i)==int:
        print(i)
'''

#72.Wap to find the length of homogenous tuple without len()
'''
t=eval(input('enter a tuple:'))
count=0
for i in t:
    count+=1
print('length of tuple:',count)
'''

#73.Wap to extract all the even numbers present in a list.
'''
l=eval(input('enter a list:'))
out=[]
for i in l:
    if type(i)==int:
        if i%2==0:
            out.append(i)
print('even nos in list:',out)
'''        

#74.Wap to remove duplicates from list
'''
l=eval(input('enter a list:'))
out=[]
for i in l:
    if i not in out:
        out.append(i)
print('after removing duplicates:',out)
'''

#75.Wap to reverse a string without using slicing.
'''
s=input('enter a string:')
rev=''
for i in s:
    rev=i+rev
print('reversed string:',rev)
'''
    
#76.wap to extract all the lowercase characters in a string only if the ascii value is even.
'''
s=input('enter a string:')
out=''
for ch in s:
    if 'a'<=ch<='z':
        if ord(ch)%2==0:
            out+=ch
print('lowercase characters with even ascii:',out)
'''

#77.Wap to check whether the last digit of an integer is even or not.-?
'''
n=int(input('enter a number:'))
if (n%10)%2==0:
    print('last digit is even')
else:
    print('last digit is not even')
'''

 #78.Wap to extract all the key value pairs from the dictionary only if the keys are of
 #string datatype and values are integers.
'''
d=eval(input('enter a dictionary:'))
out={}
for k in d:
    if type(k)==str and type(d[k])==int:
        out[k]=d[k]
print('output:',out)
'''

 #79.Wap to extract key value pairs from the dictionary only if both keys and values are exactly same.
'''
d=eval(input('enter a dictionary:'))
out={}
for k in d:
    if k==d[k]:
        out[k]=d[k]
print('result:',out)       
'''

 #80.Wap to get the following output using len function.
 #S=’power star’
 #Out={‘power’:5,’star’:4}
'''
s=input('enter a sentence')
s=s+' '
out={}
word=''
for ch in s:
    if ch!=' ':
        word+=ch
    else:
        out[word]=len(word)
        word=''
print('output:',out)
'''

 #81.Wap to get the following output.
 #S=’power star’
 #Out={‘power’:’rewop’,’star’:’rats’}
'''
s=input('enter a sentence:')
s=s+' '
word=''
out={}
for ch in s:
    if ch!=' ':
        word=word+ch
    else:
        out[word]=word[::-1]
        word=''
print('output:',out)
'''

#82. wap to extract all the non default values from a list.
'''
l=eval(input('enter a list:'))
out=[]
for i in l:
    if bool(i)==True:
        out.append(i)
print('non default values of the list are:',out)
'''

 #83.Wap to check whether the list is homogenous or not.-?
'''
l=eval(input('enter a list:'))
item1=l[0]
for item in l:
    if type(item)==type(item1):
'''        


 #84.Wap to replace the space by * present in a string
'''
s=input('enter:')
out=''
for ch in s:
    if ch==' ':
        out+='*'
    else:
        out+=ch
print('result:',out)
'''

 #85.Wap to count the number of occurrence of a specified character.

'''
s=input('enter a string:')
ch=input('enter character to find its frequency:')
count=0
for c in s:
    if c==ch:
        count+=1
print(f'Frequncy of {ch} in {s} is {count}')
'''


#86. Wap to get the following output.
# S=’always keep smiling’
 #Out-‘syawla peek gnilims’
'''
s=input('enter a sentence:')
s=s+' '
word=''
out=''
for ch in s:
    if ch!=' ':
        word=ch+word
    else:
        out=out+word+ch
        word=''
print('result:',out)
'''

 #87. Wap to get the following output.
 #In=’push maadi kushi padi’
 #Out={‘push’:’ph’,’maadi’:’a’,’kushi’:’s’,’padi’:’pi’}
'''
s=input('enter a sentence:')
d={}
s=s+' '
word=''
for ch in s:
    if ch!=' ':
        word=word+ch
    else:
        if len(word)%2==0:
            d[word]=word[0]+word[-1]
        else:
            d[word]=word[len(word)//2]
        word=''
print('result:',d)
'''

#88.Wap to toggle a string.
# 89.Wap extract upper, lower, digit and special characters present in a string to different. output variable
 #90. Wap to get the following output.
 #S=’hai hello ‘
 #Out={‘hai’:’ai’,’hello:’eo’}
 #91. Wap to get the following output.
 #S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org’]
 #Out=[‘com’,’py’,’html’,’org’]
 #92. Wap to get the following output.
 #S=[‘jiocinema.com’,’file.py’,’web.html’,’amazom.com’,’www.org ’python.py’]
 #Out={‘com’:[‘jiocinema’,’amazon’],’py’:[‘file’,’python’],’html’:[‘web’],’org’:[‘www’]}
