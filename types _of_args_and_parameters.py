#---------------------------positional argument-----------------------------------------
'''def positional(a,b,c,d):
    print(a+b,c+d)
    positional(1,2,3,4)'''
'''def positional(name,addr,phnno,marks):#order of paarmeter and arguments must be same
    print('name is:',name)
    print('address is:',addr)
    print('phnno is:',phnno)
    print('marks is:',marks)
positional('deepthi','T.Dasarahalli',8765894534,99) '''

#----------------------------default argument------------------------------------------------------------
'''def default(name,addr,phnno,phnno1=None):#we can specify None in parameters also ex:phnno1=None
                                            #and positional arguments first and default arguments in last
    print('name is:',name)
    print('address is:',addr)
    print('phnno is:',phnno)
    print('phnno1 is:',phnno1)
default('deepthi','T.Dasarahalli','None','None')'''

#---------------------------keyword arguments-------------------------------------------------------------
'''def keyword(name,addr,phnno,phnno1):
    print('name is:',name)
    print('address is:',addr)
    print('phnno is:',phnno)
    print('phnno1 is:',phnno1)
keyword(name='deepthi',addr='T.Dasarahalli',phnno=9988776655,phnno1='None') '''
#--------------------------Variable-length argument---------------------------------------------------------
# 1.*args--->0 to n positional
'''def sample(*args):
    print(args)
sample(1,2,3,4,5,6,7)'''#tuple packing----> combining multiple individual elements into a collection.here it is tuple collection


# 2.**kwargs--->0 to n keywords
'''def sample2(**kwargs):
    print(kwargs)
sample2(a=10,b=20,c=30,d=40)'''#dictionery packing-----> here it is dictionery collection

#-------------------------------unpacking-------------------------
'''l=[1,2,6,4,5]
def sam(a,b,c,d,e):
    print(a*b*c*d*e)
sam(*l)'''
#--------------------------------scope of variables-----------------------
#global variables it will give outside the function
'''a=50
b=100
print('outside the function before modification:',a,b)
def scope():
    global a,b,c
    a=5
    b=45
    c=40
    print('inside the function:',a,b,c)
scope()
print('outside the function after modification:',a,b)

#output (legb)
outside the function before modification: 50 100
inside the function: 5 45 40
outside the function after modification: 5 45'''


#
a=30
b=20
def outer():
    x=30
    y=40
    a=500
    print('from outer function')
    print('global;',a,b)
    print('local before:',x,y)
    def inner():
        nonlocal x
        x=400
        m=100
        n=200
        print('from inner func')
        print('global;',a,b)
        print('local :',m,n)
        print('enclosing:',x,y)
    inner()
    print('local after modification:',x,y)
outer()
#LEGB





