---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Backlinks:
    - Python Pentagon Space
Creation date: "2026-10-30T09:19:31Z"
Created by:
    - Predator
Links:
    - files\image_1793353083294_0.png
id: bafyreiaqjax5a6xivodhew5ss22wwlxbclwnpj7xo7mwgjukbk6pq5myxu
---
# OOPS - 5   
# Polymorphism   
Poly - many   
morphism - forms   
   
## Types   
1. Compile Time Polymorphism / Method Overloading   
2. Runtime Polymorphism / Constructor Overloading   
   
   
   
1. Compile Time Polymorphism / Method Overloading   
    Python don't support method overloading, it supports method overriding.   
    To do method overloading we need to store the reference in separate variable.   
    ![image_1793353083294_0](files\image_1793353083294_0.png)    
    ```
    
    def sum(a,b,c):
    	print(a+b+c)
    
    s1 = sum
    	
    def sum(a,b,c,d):
    	print(a+b+c+d)
    s2 = sum
    
    
    def sum(a,b):
    	print(a+b)
    s3 = sum
    
    
    s2(1,2,3,4)
    ```
       
       
    - *Method Overriding*   
        It is a process where child class provides it's own implementation for a method that is already defined in the parent class   
           
        ```
        class Parent:
        	def sam():
        		print("This is parent class method")
        
        class Child(Parent):
        	def sam():
        		print("This is child class method")
        	def child():
        		print("Hello everyone")
        
        c1 = Child()
        p1 = Parent()
        c1.sam()
        p1.sam()
        ```
   
   
> **Duck Typing**:   
> Duck typing is a way of achieving polymorphism where type of an object is not important. Instead, It's Behaviour (attributes and Method).   
>    
> If an object has a required method, python allows us to use it regardless of it's class or type.   
>    
> Walk like duck and quacks like duck ⇒ Duck only   
>    


***Example***
   
```
class Dog:
	def sound(self):
		print("bow bow")

class Cat:
	def sound(self):
		print("meow meow")

d1 = Dog()
c1 = Cat()

def make_sound(obj):
	obj.sound()

make_sound(d1)
make_sound(c1)
```
   
  - Operator Overloading   
      Overriding inbuild operator with user defined operator.   
      It is the process of making an inbuilt operator to work on the objects of user defined classes with the help of `dunder methods`.   
      It allows us to give additional meaning to the existing operator when they are used with user defined objects   
   
2. Runtime Polymorphism / Constructor Overloading   
   
   
   
   
   
   
   
   
   
   
   
   
