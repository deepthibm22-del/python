#Inheritance-->1.single inheritance
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



#2.Multilevel Inheritance
'''class Resume_10:
    def __init__(self,name,contact,email,per_10,yop_10,sname,board_10):
        self.name=name
        self.contact=contact
        self.email=email
        self.per_10=per_10
        self.yop_10=yop_10
        self.sname=sname
        self.board_10=board_10

    def display(self):
        print(self.name,self.contact,self.email,self.per_10,self.yop_10,self.sname,self.board_10,sep='\n')

    def update_contact(self,new):
        self.contact=new

class Resume_12(Resume_10):
    def __init__(self,name,contact,email,per_10,yop_10,sname,board_10,per_12,yop_12,cname,board_12):
        super().__init__(name,contact,email,per_10,yop_10,sname,board_10)#it inherit the properties from the parent class
        self.per_12=per_12
        self.yop_12=yop_12
        self.cname=cname
        self.board_12=board_12
    def display(self):
        super().display()# to combine and call all the functions once
        print(self.per_12,self.yop_12,self.cname,self.board_12)

class Resume_degree(Resume_12):
    def __init__(self,name,contact,email,per_10,yop_10,sname,board_10,per_12,yop_12,cname,board_12,cgpa,yop,college,university):
        super().__init__(name,contact,email,per_10,yop_10,sname,board_10,per_12,yop_12,cname,board_12)
        self.cgpa=cgpa
        self.yop=yop
        self.college=college
        self.university=university
    def display(self):
        super().display()
        print(self.cgpa,self.yop,self.college,self.university)
        
Deepthi=Resume_degree('Deepthi',9985562778,'deepthbm22@gmail.com',98,2020,'SRVN','State',91,2023,'GPUC','PUC',8.56,2026,'MLACW','BCU')
Deepthi.display()
#Deepthi.display_10()
#Deepthi.display_12()'''

#Multiple Inheritance--->process of a where a single child class inherits properties from multiple parent class
##Method resolution order-->order by which a childclass take properties in the order of the first mentioned parent class(ex:batsman)
'''
class Batsman:
    def __init__(self,name,team,age,runs,century):
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century
    def bat(self):
        print(self.name,'is batting')
        return self

class Bowler:
    def __init__(self,name,team,age,wickets,dot_balls):
        self.name=name
        self.team=team
        self.age=age
        self.wickets=wickets
        self.dot_balls=dot_balls
    def bowl(self):
        print(self.name,'is bowling')
        return self
        
class AllRounder(Batsman,Bowler):#Method resolution order
    def __init__(self,name,team,age,runs,century,wickets,dot_balls):
        self.name=name
        self.team=team
        self.age=age
        self.runs=runs
        self.century=century
        self.wickets=wickets
        self.dot_balls=dot_balls
    def field(self):
        print(self.name,'is fielding')
        return self
        
ob=AllRounder('Krunal pandya','RCB',32,5000,20,500,4000)       
#ob.bat()
#ob.bowl()
#ob.field()
ob.bat().bowl().field()#method chaining-->process of calling multiple methods in a single line on the same object.
print(AllRounder.mro())#to find mro we use mro() function .1.mro(),2.__mro__

'''
#heirarchial inheritance-->
'''class Employee:
    def __init__(self,name,empId,salary):
        self.name=name
        self.empId=empId
        self.salary=salary
    def emp(self):
        print(self.name,'emp of this company')
        return self
class Developer(Employee):
    def __init__(self,name,empId,salary,role):
        super().__init__(name,empId,salary)
        self.role=role
    def developer(self):
        print(self.name,'is a developer')
        return self
class TestEngineer(Employee):
    def __init__(self,name,empId,salary,role):
        super().__init__(name,empId,salary)
        self.role=role
    def test(self):
        print(self.name,'is a Testengineer')
        return self
ob1=Employee('deepthi','Emp34',25000)
ob2=Developer('laxmi','Emp34',25000,'developer')
ob3=TestEngineer('anu','Emp34',25000,'tester')

ob1.emp()
ob2.developer()
ob3.test()'''


#hybrid
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def per(self):
        print(self.name,'is a person')
        return self
class Teacher(Person):
    def __init__(self,name,age,role):
         super().__init__(name,age)
         self.role=role
    def teach(self):
        print(self.name,'is teaching')
        return self
class Student(Person):
    def __init__(self,name,age,role):
        super().__init__(name,age)
        self.role=role
    def study(self):
        print(self.name,'is a studying')
        return self
class AIassitant(Teacher,Student):
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
    def Ai(self):
        print(self.role,'the student and teacher')
        return self
'''ob1=Person('smitha',26)
ob1.per()

ob2=Teacher('sushma',32,'Teacher')
ob2.per()
ob2.teach()

ob3=Student('vidhya',15,'student')
ob3.per()
ob3.study()'''
#ob3.teach()


ob4=AIassitant('ChatGPT',10,'guiding','listening')
ob4.teach() .Study() .Ai()

'''ob1.per()
ob2.teach()
ob3.study()
#ob4.Ai()
   ''' 
      

    





    
    

















        
