'''a=10
print(type(a))#<class 'int'>
print(type(int))#<class 'type'>
print(type(type))#<class 'type'>

#-----creation of class-----#
class Human:
    eyes=2
    nose=1
#---object creation------#
a=Human()
b=Human()

#access class properties#
print('access using class name eyes:',Human.eyes,'nose:',Human.nose)
#not specified attributes cannot be accessed it throws an error#
#print('access using class name legs:',Human.legs)


#access object properties#
print('access using object name a:',a.eyes,a.nose,'b:',b.eyes,b.nose)

#initialize new class properties#
Human.ears=2

#class properties on all objects#
print('new attribute for human ears:',Human.ears)
print('New attribute ears for a and b as well:',a.ears,b.ears)


#modify existing class properties
Human.eyes=3
Human.mouth=1
print("modified human eyes:",Human.eyes,'mouth:',Human.mouth )
#initalize new object properties
a.legs=2
print(a.legs)
#print(Human.legs)#error
#4print(b.legs)#error'''


#-----------------------------------CONSTRUCTOR-------------------------------------------------
'''class School:
    school_name='Pentagon space'
    Location='Vijaynagar bengaluru'
    school_principal='Pradeep Mysuru'

    def __init__(self,age,contact,addr,quali,course):
        self.age=age
        self.contact=contact
        self.addr=addr
        self.quali=quali
        self.course=course
deepthi=School(21,9980234455,'bengalore','BCA','Computer Applications')
hitha=School(31,8976574894,'hyderabad','BCA','JAVA')
kavya=School(22,7856437584,'Mysore','BCA','python')'''


#access dict of cname and objname
'''cname__dict__
objname__dict__'''


#using function to repeatedly printing the indvidual objectname

'''class School:
    school_name='Pentagon space'
    Location='Vijaynagar bengaluru'
    school_principal='Pradeep Mysuru'

    def __init__(self,name,age,contact,addr,quali,course):
        self.name=name
        self.age=age
        self.contact=contact
        self.addr=addr
        self.quali=quali
        self.course=course   
    
    
    def details_school(self):
        print(self.name,self.age,self.contact,self.addr,self.quali,self.course)
        
deepthi=School('deepthi',21,9980234455,'bengalore','BCA','Css')
hitha=School('hitha',31,8976574894,'hyderabad','BCA','JAVA')
kavya=School('kavya',22,7856437584,'Mysore','BCA','python')
hitha.details_school()
kavya.details_school()
deepthi.details_school()'''

#bank withdraw,deposite,balance

class Bank:
    bank_name='Canara bank'
    location='Peenya'
    bank_manager='deepthi'

    def __init__(self,name,ifsccode,accno,aadharno,addr):
        
        self.name=name
        self.ifsccode=ifsccode
        self.accno=accno
        self.aadharno=aadharno
        self.addr=addr
        self.balance=0

    def deposite(self):
        amount=int(input("enter the  deposite amount:"))
        self.balance=self.balance+amount
        print(f'deposite RS.{amount} successfully')
        
        

    #def withdraw(self):
        

    def details(self):
        print(self.name,self.ifsccode,self.accno,self.aadharno,self.addr)
        
deepthi=Bank('deepthi','ISFC8990',2345678906748,847345673489,'Bengaluru')

deepthi.details()
deepthi.deposite()'''

#different methods of class and objects

'''class School:
    school_name='Pentagon space'
    Location='Vijaynagar bengaluru'
    school_principal='Pradeep Mysuru'

    def __init__(self,name,age,contact,addr,quali,course):
        self.name=name
        self.age=age
        self.contact=contact
        self.addr=addr
        self.quali=quali
        self.course=course   
    
    @classmethod
    def update_principal(cls,new):
        cls.school_principal=new
        
    #object method
    def upadate_std(self,new):
        self.std=new
        
    #static method
    @staticmethod
    def static_print():
        print('the details of the students are:')
        
    def details_school(self):
        self.static_print()
        print(self.name,self.age,self.contact,self.addr,self.quali,self.course)
        
deepthi=School('deepthi',21,9980234455,'bengalore','BCA','Css')
hitha=School('hitha',31,8976574894,'hyderabad','BCA','JAVA')
kavya=School('kavya',22,7856437584,'Mysore','BCA','python')
hitha.details_school()
kavya.details_school()
deepthi.details_school()'''

#inheritance

'''class Vehicle:
    brand='Suzuki'
    fuel_type='petrol'
    def start(self):
        print('the vehicle is starting')

class Bike(Vehicle):
    color='black'
    price=150000
    models='BS4'
    wheels=2
    def ride(self):
        print('today i am going to bike ride')
u1=Bike()
u1.start()
print(u1.brand)
print(u1.fuel_type)
u1.ride()
print(u1.color)
print(u1.brand)
print(u1.price)
print(u1.models)
print(u1.wheels)'''


    



    
    
    


        






