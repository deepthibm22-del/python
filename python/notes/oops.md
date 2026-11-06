---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Tag:
    - Dunner
    - OOPS
Backlinks:
    - Python Pentagon Space
Creation date: "2026-10-24T09:08:44Z"
Created by:
    - Predator
id: bafyreifrnj4qc3pvyccatp2lppose5rjjow5ejxmxbbe7kua3jgo7acnyu
---
# OOPS   
*OOPS (Object Oriented Programming Systems)*   
- Used to work with real world entites.   
- OOPS is used to deal with real world project.   
- OOPS is used to give structure to data.   
   
**Example**:   
  Evert user that uses an application can be considered as object.   
   
- Oops is **programming paradigm** that provide us a way to deal with real world objects as **class** and **objects**   
- Class is a blueprint/container that store properties/attributes and behavior of a Real-time entity.   
- Object is an instance of class.   
   
   
## Meta Class   
- A **metaclass** is a class that defines how other classes are created and behave.   
- ***type*** is meta class of all class (Super Class)   
- In python all data type is inbuild class.   
   
   
```
a = 10
type(a) # <class 'int'>
type(int) # <class 'type'>
type(type) # <class 'type'>
```
   
***Extra:***   
Core Concept   
**Regular class:** A blueprint for creating **objects** (instances). (For example, a `Dog` class creates individual dog objects like `buddy`).   
**Metaclass:** A blueprint for creating **classes** themselves. (A metaclass creates and controls the `Dog` class).   
Just as an object is an instance of a class, a class is an instance of a meta class.   
   
How It Works in Python   
**Default Metaclass:** In Python, the built-in `type` is the default metaclass used to create all standard classes.   
**Custom Metaclasses:** You can create your own custom metaclass by inheriting from `type` and overriding methods like `__new__` or `__init__` to intercept and modify class creation.   
**Syntax:** In Python 3, you specify a metaclass using the `metaclass=` keyword argument in a class definition   
```
class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass
```
   
   
   
## Creating User Defined Class in Python   
Syntax:   
```
class ClassName:
	# Attributes and Methods/Behaviour

object_name = ClassName(arg1, arg2, arg3...., arg_n)
```
   
 --- 
   
### *Properties-*   
- There are 2 types   
    1. Generic Properties.   
        - Properties that belongs to a class and common for its object.   
        - These properties will be share to every object created using the class.   
        - When changes are made to it in class it will affect it's objects properties also. But changes made to object individually will not affect the class's generic properties.   
   
           
    2. Object Specific Properties.   
        - Properties specific to particular object   
        - It can be passed through `args` when creating an object   
        - Example   
   
        ```
        class Human:
        	pass
        
        human1 = Human('Manu', 26, 'Male')
        ```
        - It will be unique to that class   
- We can create any number of objects   
- Without class we cannot create object.   
   
   
```
class Human:
	eyes = 2 # Generic Properties
	nose = 1 # Generic Properties
	ear = 2 # Generic Properties
	brain = 1 # Generic Properties

prasad = Human()
harsha = Human()
sayanth = Human()
```
   
- We use **dot notation** access the properties of an object or initialize generic properties or modify generic properties   
   
   
### *Creating class using Generic Properties*   
```
class Human:
	eyes = 2
	nose = 1
	ear = 2
	brain = 1

prasad = Human()
harsha = Human()
sayanth = Human()

Human.hands = 2 # Initialize generic properties and updates objects
Human.eyes = 1 # Modify the generic properties add associated objects

print(prasad.eyes) # Access the generic properties

prasad.eyes = 5 
print(prasad.eyes)
print(Human.eyes)
```
   
### *Creating class using Object Specific Properties:*   
   
```
class Human:
	pass

prasad = Human()
prasad.age = 23
prasad.contact = 9356524562
prasad.address = 'Belur'
prasad.qual = 'B.E'

print(f"""
Human Name: Prasad
Age: {prasad.age}
Address: {prasad.address}
Contact: {prasad.contact}
Qualification: {prasad.qual}
"""
)
```
   
   
### *Creating class using constructor*   
   
- Constructors are class methods to initialize instance properties.   
- In python, we define `__init__( )` inside class to create a constructor.   
- `__init__` is called Dunder Method/ Magic Method.   
- `Dunner Method` Invoke Itself   
   
   
Syntax:   
```
class Cname:
	# class Attribues if any

	# create a constructor
	def __init__(self, para_1, para_2,..., para_n):
		self.para_1 = para_1
		self.para_2 = para_2
		self.para_3 = para_3
		...
		self.para_n = para_n

object_name = Cnmae(arg_1, arg_2, arg_3,..., arg_n)
		
```
   
- `self` is a naming convention for a parameter that is used inside a class to point to the address of the current `object`.   
   
   
***Example:***   
```
class Human:
	eyes = 2
	nose = 1
	ears = 2
	brain = 1
	
	# Create constructor
	def __init__(self, name, age, contact, address, qual):
		self.name = name
		self.age = age
		self.contact = contact
		self.address = address
		self.qual = qual

	def __str__(self):
		return f"The object has followig details:\n\tName:{self.name} \n\tage:{self.age}\n\tQual:{self.qual}"

human1 = Human('Prasad', 23, 9353918278, 'Belur', 'B.E')
print(human1)
```
   
   
<details>
<summary>Q) Create a class named school with some properties</summary>

```
class School:
	def __init__(self, name, branch):
		self.name = name
		self.branch = branch

	class Student:
		def __init__(self1, name, age, std, add):
			self1.name = name
			self1.age = age
			self1.std = std
			self1.add = add
```

</details>

   
   
   
## How Class is stored in memory?   
It is stored in for of dictionary.   
```
class Human:
	eyes = 2
	nose = 1
	ears = 2
	brain = 1
	# Create constructor
	def __init__(self, name, age, contact, address, qual):
		self.name = name
		self.age = age
		self.contact = contact
		self.address = address
		self.qual = qual

print(Human.__dict__)
```
   
   
   
   
