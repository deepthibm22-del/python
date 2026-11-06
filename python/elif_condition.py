#wap to chech wheathr the digit is single,double,triple or more than that.
'''n=int(input("enter:"))
if 0<=n<=9:
    print(n,'is a single digit')
elif 10<=n<=99:
    print(n,'is a double digit')
elif 100<=n<=999:
    print(n,'is a triple digit')
else:
    print(n,'is a more than that digit')'''

'''n=str(n)
if len(n)==1:
    print(n,'is a single digit')
elif  len(n)==2:
    print(n,'is a double digit')
elif  len(n)==3:
    print(n,'is a triple digit')
else:
    print(n,'is a more than that digit')it will not work'''



#wap to check quadrant of x axis and y axis
'''x=int(input('enter:'))
y=int(input('enter:'))
if x==0 and y==0:
    print(f"({x},{y})is origin")
elif x==0 and y>0:
    print('is in y axis')
elif x>0 and y==0:
    print('is in x axis')
elif x>0 and y>0:
    print('Quadrant 1')
elif x>0 and y<0:
    print('Quadrant 4')
elif x<0 and y<0:
    print('Quadrant 3')
else: 
    print('Quadrant 2')'''


#wap to print fizz if the number is multiple of 3,print buzz if
#number is multiple of 5 and print fizzbuzz if it is multiple of 3 and 5
'''x=int(input('enter:'))
if x%3==0 and x%5==0 :
    print(x,'fizzbuzz')
elif x%5==0:
    print(x,'buzz')
elif x%3==0:
    print(x,'fizz')
else:
    print('not divisible by both 3 and 5')'''



#wap to find the greatest of 3 numbers
'''a=int(input('enter the 1st number:'))
b=int(input('enter the 2nd number:'))
c=int(input('enter the 3rd number:'))
if a==b==c:
    print('all are equal')
elif a>b and a>c:
    print(a,'is greatest')
elif b>c:
    print(b,'is greater')
else:
    print(c,'is greatest')'''


#wap to check if it is uppercase convert it to lower case ,if its lower case to uppercase
#it is a digit find square of it
# if iit is special character *5
ch=input("enter a char:")
if 'A'<=ch<='Z':
    print(chr(ord(ch)+32))
elif 'a'<=ch<='z':
    print(chr(ord(ch)-32))
elif '0'<=ch<='9':
    print(int(ch)**2)
else:
    print(ch*5)
        

      
      




    




    

    




    
           
        
