#method overloading--->same method name performin different task based on the parametrers
'''def sam(a,b):
    print(a+b)
def sam(a,b,c):
    print(a+b-c)
def sam(a,b,c,d):
    print(a+b,c+d)
sam(1,2)'''

#TypeError: sam() missing 2 required positional arguments: 'c' and 'd'
#so we can use this method storing it another variable
'''def sam(a,b):
    print(a+b)
temp1=sam
def sam(a,b,c):
    print(a+b-c)
temp2=sam
def sam(a,b,c,d):
    print(a+b,c+d)
sam(1,2,3,4)
temp1(10,20)'''

#method overriding
'''class Parent:
    def sam(self):
        print("i'm from parent class")
ob1=Parent()
class Child(Parent):
    def sam(self):
        print("i'm from child class")
    def child(self):
        print('hello everyone')
ob=Child()
ob.sam()
ob.child()'''

#duck-typing--->where the type of an object is not imp instead of its behaviour (attributes and methods)is important
'''class Dog:
    def sound(self):
        print('bow bow')
class Cat:
    def sound(self):
        print('meow meow')
c=Cat()
d=Dog()

def make_sound(obj):
    obj.sound()

c.sound()
d.sound()'''

#operator overloading
#dir(int)#-->to see inbuilt function


'''class Sam:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    def __sub__(self,other):
        return self.a-other.a
    def __mul__(self,other):
        return self.a*other.a
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
    def __pow__(self,other):
        return self.a^other.a
x=Sam(10)
print('sum is',x)

y=Sam(20)
print(y)'''


#ob=sam([2,2,3,4])

#relational and bitwise operator overloading
'''class Sam:
    def __init__(self,a):
        self.a=a
    def __ge__(self,other):
        return self.a+other.a
    def __le__(self,other):
        return self.a-other.a
    def __eq__(self,other):
        return self.a*other.a
    def __gt__(self,other):
        return self.a/other.a
    def __lt__(self,other):
        return self.a//other.a
    #def __pow__(self,other):
        #return self.a^other.a
x=Sam(10)
print(x)
y=Sam(20)
print(y)
ob=Sam([2,2])'''

#encapsulation
class Bank:
    bname='Canara bank'
    branch='Peenya'
    _manager='deepthi'#protected
    __ifsc='sbi110031'#private
    def __init__(self,name,phno,accno,bal):
        self.name=name
        self.__phno=phno#private
        self.__accno=accno#private
        self._bal=bal#protected
    @classmethod
    def display(cls):
        print(cls.__bname,cls.__branch,cls.manager,cls.__ifsc)
    def get_accno(self):#first we should create public methods to acess and modify private attribut decoratros
        print(self.__accno)
    @property
    def phno(self):
        print(self.__phno)
    @phno.setter
    def phno(self,new):
        self.phno=new
    '''def get_phno(self):
       print(self.__phno)
    def set_phno(self,new):
       self.__phno=new'''
       

c1=Bank('deepthi',9984657274,987654567890,95000)
#output for public -->without underscore everything
'''c1.phnno
9984657274
c1.name
'deepthi'
c1.accno
987654567890
c1.bal
95000'''
#ouput for protected-->single undescore 
'''Bank._manager
'deepthi'
c1._bal
95000'''
#output for private--->double underscore with class
'''Bank._Bank__ifsc
'sbi110031'
c1._Bank__accno
987654567890
c1._Bank__phnno
9984657274'''













    
