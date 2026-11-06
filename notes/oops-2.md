---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Backlinks:
    - Python Pentagon Space
Creation date: "2026-10-28T09:07:05Z"
Created by:
    - Predator
id: bafyreidvd5yryflliu5v4unk2aqfjxjju3367atgvvkqbtu5ouw5ye6uzu
---
# OOPS - 2   
## Method   
A method is a function that belongs to an object or a class.   
   
## Types of Methods   
   
1. Object/Instance Method   
2. Class Method   
3. Static Method   
   
   
1. Object/Instance Method   
    An method associated with an object is called object method.   
    ***Syntax***   
    ```
    class Cname:
    	def methodName(self, para1, para2, para3,...., para_n):
    		# Statement Blocks
    
    object_1 = Cname()
    object_1.methodName(para1, para2, para3,..., para3)
    ```
       
2. Class Method   
    Decorator:   
      Decorators are special method that are used to give additional functionalities to a method with modifying the original class.   
      ```
      class cname:
      	@classmethod
      	def mname(clsm para1, para2,...) {
      		# S.B
      	}
      
      obj = canme()
      cname.mname
      ```
         
         
3. Static Method   
    Acts as an isolated utility function inside the class   
    Does not belong to either of class or object, but works with both class and object.   
    ```
    class BankAccount:
            bname = "Canara"
            branch = "Belur"
    
            def __init__(self, uname, accNo, bal):
                self.uname = uname
                self.accNo = accNo
                self.bal = bal
    
            def deposit(self, dep):
                self.bal += dep
                print(f"Deposited {dep} Successfully!")
                print()
    
    
            def withdraw(self, amt):
                if self.bal >= amt:
                    self.bal -= amt
                    print(f"Withdraw (amount: {amt}) Successfully!")
                    print()
                    return
                print("Insufficient Balance")
                print()
    
    
            def balance(self):
                self.static()
                print(f"Balance: {self.bal}")
                print()
    
    
            @classmethod
            def display(cls):
                cls.static()
                print(f"Bank Name: {cls.bname}\nBank Branch: {cls.branch}")
                print()
    
            @staticmethod
            def static():
                 print("The Details are: ")
    ```
   
   
   
   
