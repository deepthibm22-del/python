#to print diagonla
'''*
     *
        *
           *
              *'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''

'''
*         
* *       
* * *     
* * * *   
* * * * *

for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''

##
##* * * * * 
##  * * * * 
##    * * * 
##      * * 
##        *
'''for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''



#to print secondary diagonal
#            * 
#         *   
#        *     
#      *       
#    *         
#  *           
#*      

'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


#1         
#1 2       
#1 2 3     
#1 2 3 4   
#1 2 3 4 5 

'''for i in range(1,6):
    for j in range(1,6):
        if i<=j:
            print(j,end=' ')
        else:
             print(' ',end=' ')
    print()'''

#1         
#2 2       
#3 3 3     
#4 4 4 4   
#5 5 5 5 5 
'''for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(i,end=' ')
        else:
             print(' ',end=' ')
    print()'''




##    * * * * * 
##    *       * 
##    *       * 
##    *       * 
##    * * * * * 

'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''





##* * * * * 
##*   *   * 
##* * * * * 
##*   *   * 
##* * * * * 
'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==(n//2)+1  or j==(n//2)+1 :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''

##* * * * * * * 
##*           * 
##*           * 
##*     *     * 
##*           * 
##*           * 
##* * * * * * * 
'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==(n//2)+1   and i==j :
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''

##*       * 
##  *   *   
##    *     
##  *   *   
##*       * 
'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''

##        *         
##      *   *       
##    *       *     
##  *           *   
##* * * * * * * * * 

'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n*2):
        if i==n or i+j==n+1 or j-i==n-1:
            print('*',end=' ')
        else:
             print(' ',end=' ')
    print()'''


'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n*2):
        if i>=j:
            if j%2==0:
                print(j**2,end=' ')
            else:
                print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

##        *  
##      *  *  
##    *  *  *  
##  *  *  *  *  
##*  *  *  *  * 

'''n=5
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print('* ',end=' ')
    print()'''
##    * 
##   * * 
##  * * * 
## * * * * 
##* * * * * 
## * * * * 
##  * * * 
##   * * 
##    * 

'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for s in range(n-i):
        print(' ',end=' ')
    for j in range(i):
        print('* ',end=' ')
    print()
for i in range(1,n):
        for s in range(i):
            print(' ',end=' ')
        for j in range(n-i):
            print('* ',end=' ')
        print()'''
#another approch
##    * 
##   * * 
##  * * * 
## * * * * 
##* * * * * 
## * * * * 
##  * * * 
##   * * 
##    * 
'''n=5
for i in range (1,n+1):
    print(' '*(n-i)+'* '*(i))
for i in range (1,n):
    print(' '*(i)+'* '*(n-i))'''
#secondary lower

##enter a number:5
##        5 
##      4 5 
##    3 4 5 
##  2 3 4 5 
##1 2 3 4 5


'''n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print(j,end=' ')
        else:
             print(' ',end=' ')
    print()'''

#primary lower

##1         
##2 2       
##3 3 3     
##4 4 4 4   
##5 5 5 5 5 
'''for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print(i,end=' ')
        else:
             print(' ',end=' ')
    print()'''


#primary upper
##A B C D E 
##  A B C D 
##    A B C 
##      A B 
##        A 

'''for i in range(1,6):
    ch=ord('A')
    for j in range(1,6):
        if i<=j:
            print(chr(ch),end=' ')
            ch+=1
        else:
             print(' ',end=' ')
    print()'''


#secondary upper
'''n=int(input("enter a number:"))
for i in range(1,n+1):
    ch=ord('A')+i-1
    for j in range(1,n+1):
        if i+j<=n+1:
            print(chr(ch),end=' ')
            ch+=1
        else:
             print(' ',end=' ')
    print()'''
#primary upper and lower,secondary lower and upper diagonal
##        5 1         
##      4 5 2 2       
##    3 4 5 3 3 3     
##  2 3 4 5 4 4 4 4   
##1 2 3 4 5 5 5 5 5 5 
##A B C D E A B C D E 
##  A B C D B C D E   
##    A B C C D E     
##      A B D E       
##        A E  

n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print(j,end=' ')
        else:
             print(' ',end=' ')
    for j in range(1,6):
        if i>=j:
            print(i,end=' ')
        else:
             print(' ',end=' ')
    print()
for i in range(1,6):
    ch=ord('A')
    for j in range(1,6):
        if i<=j:
            print(chr(ch),end=' ')
            ch+=1
        else:
             print(' ',end=' ')
        
    ch=ord('A')+i-1
    for j in range(1,n+1):
        if i+j<=n+1:
            print(chr(ch),end=' ')
            ch+=1
        else:
             print(' ',end=' ')
    print()
             
    







        
            
    
