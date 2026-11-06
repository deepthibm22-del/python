#Decorators
'''def instagram(func):
    def wrapper(*args,**kwargs):
        print('go to website')
        print('login')
        func(*args,*kwargs)
        print('logout')
    return wrapper
@instagram
def Deepthi(name):
    print('text with',name)
@instagram
def Kavya(name):
    print('make reel with',name)
@instagram
def Likhi(name):
    print('mention story with',name)'''
#output
'''Deepthi('hitha')
go to website
login
text with hitha
logout
Kavya('shreya')
go to website
login
make reel with shreya
logout
Likhi('gagana')
go to website
login
mention story with gagana
logout'''

#create a decorator to calculate the  execution time for any program
'''import time
def calc_time(func):
    def wrapper(*args,**kwargs):
        st=time.time()
        func(*args,**kwargs)
        et=time.time()
        print('the total time taken is:',et-st)
    return wrapper
@calc_time
def sam():
    for i in range(1,10):
        print('its raining')'''
#output
'''sam()
its raining
its raining
its raining
its raining
its raining
its raining
its raining
its raining
its raining
the total time taken is: 0.11052632331848145'''


#create a decorator to calculate a delay time
'''
import time
def calc_time(func):
    def wrapper(*args,**kwargs):
        time.sleep(5)
        func(*args,**kwargs)
        time.sleep()
    return wrapper
@calc_time
def sam():
    for i in range(1,10):
        print('its raining')'''

#prgrm to write when we call function 1 time it should print. 2nd times it should print 2 times
'''def func_count(func):
    count=0
    def wrapper(*args,**kwargs):
        nonlocal count
        func(*args,**kwargs)
        count+=1
        print(f'the function called for {count} times')
    return wrapper
@func_count
def sam():
    print('decorator')'''
    
#sam()
'''decorator
the function called for 1 times
sam()
decorator
the function called for 2 times
sam()
decorator
the function called for 3 times'''
    




        

