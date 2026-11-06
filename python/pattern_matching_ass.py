##        *       9
99

##      *   *       
##    * * * * *     
##  *           *   
##*               * 

#c=5
#r=5
'''c=int(input("enter the columns:"))
r=int(input("enter the row:"))
for i in range(1,r+1):
   for j in range(1,c+1):
       #if i+j==6 or j-i==4 or (i==3 and 4<=j<=6):
       if j==1 or j==c  or  ( i==1 and (j==2 or j==c-1)):
           print('*',end=' ')
       else:
           print(' ',end=' ')
   print()'''




#B
#n=5
'''for row in range (1,n+1):
    for b in range(1,n+1):
        if b==1 or row==1 and b!=n or row==n//2+1 and b!=n or row==n//2 and b==n or row==n//2+3 and b!=n or row==n//2+2 and b==n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''


#C
'''for row in range (1,n+1):
    for c in range(1,n+1):
        if row==1 and c!=1 or c==1 and row!=1 and row!=n or row==n and c!=1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#D
'''for row in range (1,n+1):
    
    for d in range(1,n+1):
        if row==1 and d!=n or d==1 or row==n and d!=n or d==n and row!=1 and row!=n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''


#E
'''for row in range (1,n+1):
    for e in range(1,n+1):
        if row==1 or e==1 or row==n//2+1 or row==n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()#or row==1 or row==n//2+1:
print()'''


#F
'''n=5
for row in range (1,n+1):
   for f in range(1,n+1):
      if row==1 or f==1 or row==n//2+1:
         print("*",end=' ')
      else:
         print(' ',end=' ')
   print()  
print()'''

#G
'''n=5
for row in range (1,n+1):
    for g in range(1,n+1):
        if  row==1 and g!=1  or g==1 and row!=1 or g!=1 and row==n or g==n and row!=n//2 or row//2+1 and g!=n//2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''


#H
'''n=5
for row in range (1,n+1):
    for c in range(1,n+1):
        if c==1 or c==n or row==n//2+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#I
'''n=5
for row in range (1,n+1):
    for i in range(1,n+1):
        if row==1 or i==n//2+1 or row==n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''


#J
n=5
'''for row in range (1,n+1):
    for j in range(1,n+1):
        if row==1 or j==n//2+1 or row==n and j!=n and j!=n-1 and j!=1 or row==n and j==1 or row==n-1 and j==1: 
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#K
'''for row in range (1,n+1):
    for k in range(1,n+1):
        if k==1 or row+k==n or row-k==1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''


#L
'''for row in range (1,n+1):
    for l in range(1,n+1):
        if l==1 or row==n :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#M
'''for row in range (1,n+1):
    for m in range(1,n+1):
        if m==1 or m==n or row==m and m<=n//2 or row==m+n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

##11 12 13 14 15    
##21 22 23 24 25
##31 32 33 34 35
##41 42 43 44 45
##51 52 53 54 55
#N
'''for row in range (1,n+1):
    for j in range(1,n+1):
        if j==1 or  row==j or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()'''


#O
'''for row in range (1,n+1):
    for o in range(1,n+1):
        if o==1 and row!=1 and row!=n or row==1 and o!=1 and o!=n or o==n and row!=1 and row!=n or row==n and o!=1 and o!=n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#P
'''for row in range (1,n+1):
    for p in range(1,n+1):
        if p==1 or row==1 and p!=n or p==n and row==n//2 or row==n//2+1 and p!=n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#Q
'''for row in range (1,n+1):
    for q in range(1,n+1):
        if q==1 and row!=1 and row!=n or row==1 and q!=1 and q!=n :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

'#R
'''for row in range (1,n+1):
    for r in range(1,n+1):
        if r==1 or row==1 and r!=n or row==n//2 and r==n or row==n//2+1 and r!=n or row>n//2 and row==r:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#s
'''for row in range (1,n+1):
    for s in range(1,n+1):
        if row==1 or s==1 and row<=n//2+1 or row==n//2+1 :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#t
'''for row in range (1,n+1):
    for t in range(1,n+1):
        if row==1 or t==n//2+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#u
'''for row in range (1,n+1):
    for u in range(1,n+1):
        if u==1  or row==n or u==n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()

#v
for row in range (1,n+1):
    for v in range(1,n+1):
        if row==v and row!=n and row!=n-1 :
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#w
'''for row in range (1,n+1):
    for w in range(1,n+1):
        if w==1 or w==n or row+w==6 and row>2 or row==w or row>2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#x
'''for row in range (1,n+1):
    for x in range(1,n+1):
        if row==x or row+x==6:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''

#y
'''for row in range (1,n+1):
    for y in range(1,n+1):
        if row==y and row<=3 or row+y==6:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()'''


 #z   
'''for row in range (1,n+1):
    for z in range(1,n+1):
        if row==1 or row+z==6 or row==n:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()'''
