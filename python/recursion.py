#-------------------RECURSION------------------------------------
#sum of list
'''l=[1,2[4,5,(9,8,{12,34,(9,11,17,),35},12,18),19,89],66,1,5]

def sum_int(l):
    sum=0
    for i in l:
        if type(i)==int:
            sum+=i
        elif type(i) in [list,tuple,set]:
            sum+=sum_int(i)
    return sum
print(sum_int(l))'''


#------------------2syntaxes----------------------
#1 st syntax

'''def fname(par1,par2....):
    if base_condition:
        return value
    statement-block
    return fname(arg1,arg2...argn)
print(fname(arg1,arg2....arg3)


#2nd syntax
      
def fname(par1,par2....):
    if base_condition:
        return 
    statement-block
    fname(arg1,arg2...argn)
print(fname(arg1,arg2....arg3)'''

#-------123454321------------
'''def sample(n,i=1):
    print(i,end=" ")
    if i==n:
        return
    sample(n,i=i+1)#recursion
    print(i,end=" ")
sample(5)'''

#-------reverse a str-------------
'''def reverse(s,rev='',i=0):
    if i>=len(s):
        return rev
    rev=s[i]+rev
    return reverse(s,rev,i=i+1)
print(reverse('deepthi'))'''

#------------revrse a number-------------
def reverse(n,rev=0):
    if n<=0:
        return rev
    d=n%10
    rev=(rev*10)+d
    n=n//10
    return reverse(n,rev)
print(reverse(1234))








