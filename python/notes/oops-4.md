---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Backlinks:
    - Python Pentagon Space
Creation date: "2026-10-29T08:58:17Z"
Created by:
    - Predator
Links:
    - files\image_1793271841550_0.png
id: bafyreietdd5fysbq2dyqomqjwdleqd77stmrd6wqk53mfomdxtwtcynore
---
# OOPS - 4   
## Multi - Level Inheritance   
Multi-level inheritance is a process of deriving properties from one class to another class by considering more than 1 level.   
Here a class derives a properties from another derived class.   
```
class parent:
	attributes and properties

class child1(parent):
		attributes and properties
class child2(child1):
		attributes and properties
class child3(child2):
		attributes and properties
...
class child_n(child_n-1):
		attributes and properties
```
   
```
GP(x) --> P(x,y) --> C(x,y,z) --> .... --> n_GC (x,y,z,...n)
```
   
Chaining   
### **Constructor** **Chaining**   
Constructor chaining is the process of calling parent class constructor inside child class constructor to avoid **Re-initialization** of attributes which are already initialized in parent class.   
We use `**super()**` function inside child class constructor.   
```
class Parent:
	def __init__(self,....):
		initialize instance variable

class Child(Parent):
	def __init__(self,.....):
		super().__init__(args...)
		initialize other instance variables
```
   
   
## Multiple Inheritance   
   
   
```
class parent1:
	attribute

class parent2:
	attribute
.
.
.
class parnet_n:
	attribute

class child(parent1, parent2,...,parent_n)
	attribute
```
   
```
p1 , p2, .........  p_n => child [c + p1 + p2 + ... + p_n]
```
   
### Method Resolution Order   
**Method Resolution Order (MRO)** is the definitive sequence Python follows to look up methods and attributes in a class hierarchy. It becomes critically important in multiple inheritance scenarios to resolve name collisions and ensure a predictable execution path. [1, 2]   
Python calculates the MRO using the **C3 Linearization algorithm**, which enforces three structural guarantees:   
1. Subclasses are checked before their parent classes.   
2. Multiple parents are searched from left to right as listed in the class definition.   
3. The lookup sequence remains monotonic, meaning a class's relative order will not shift unexpectedly down the chain.    
 --- 
   
   
### How to Inspect the MRO   
Python provides two native ways to view a class's resolution order. You must call these on the class itself, not on its instances: [6]   
- `Class.__mro__`: Returns the hierarchy as an immutable **tuple**.   
- `Class.mro()`: Returns the hierarchy as a mutable **list**.   
   
```
class A: pass
class B(A): pass

print(B.__mro__) 
# Output: (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


```
 --- 
   
### ##The Diamond Problem (Visual Example)   
The "Diamond Problem" occurs when a class inherits from two parent classes that both derive from a single grandfather class.    
```
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return "Hello from B"

class C(A):
    def greet(self):
        return "Hello from C"

class D(B, C):
    pass

obj = D()
print(obj.greet())  # Output: Hello from B
print(D.mro())      # Output: [D, B, C, A, object]


```
   
### Why `D.mro()` is [D, B, C, A, object]   
- `D`: Python always checks the target subclass first.   
- `B`: Extracted next because it is the leftmost parent specified in `class D(B, C)`.   
- `C`: Evaluated before `A` because the C3 algorithm guarantees a child class ( `C`) must be evaluated before its parent ( `A`) is stripped out.   
- `A`: Evaluated once its dependent children ( `B` and `C`) have both been accounted for.   
- `object`: The ultimate root class of all objects in Python.    
 --- 
   
   
## Invalid MROs ( TypeError)   
Python will proactively block the creation of inheritance hierarchies that violate local precedence or break monotonicity, raising a `TypeError` at compile time.    
```
class X: pass
class Y(X): pass
class Z(X, Y): pass 
# TypeError: Cannot create a consistent method resolution order (MRO) for bases X, Y


```
- Why it fails: You told Python to search `X` before `Y` (left-to-right). However, `Y` is a subclass of `X`, meaning `Y` must legally appear before `X`. This contradiction breaks C3 linearization. [4, 6]   
   
To advance your understanding, tell me:   
- Are you diagnosing a `TypeError: Cannot create a consistent MRO` error in existing code?   
- Do you need help structuring a complex inheritance pattern using the `super()` function?   
   
   
 --- 
## MRO in Multi level Inheritance   
In **multilevel inheritance**, where a class derives from a child class (e.g., `C` inherits from `B`, and `B` inherits from `A`), the Method Resolution Order (MRO) is exceptionally straightforward.   
Python resolves methods sequentially from **bottom to top**, tracing the direct lineage back to the root `object` class.   
MRO Sequence   
For a classic chain `C ➔ B ➔ A`, the lookup order is always:   
   
![image_1793271841550_0](files\image_1793271841550_0.png)    
   
   
 --- 
Code Blueprint   
```
class Grandparent:
    def action(self):
        return "Action from Grandparent"

class Parent(Grandparent):
    def action(self):
        return "Action from Parent"

class Child(Parent):
    pass

# Checking the MRO
print(Child.mro())
# Output: [<class 'Child'>, <class 'Parent'>, <class 'Grandparent'>, <class 'object'>]

obj = Child()
print(obj.action()) 
# Output: "Action from Parent" (Stops at the first match it finds)


```
   
 --- 
### How `super()` Traverses Multilevel MRO   
The `super()` function does not just look at the immediate parent; it follows the MRO array step-by-step. This allows you to extend behavior down the entire chain cleanly:   
   
```
class Grandparent:
    def __init__(self):
        print("Grandparent initialized")

class Parent(Grandparent):
    def __init__(self):
        super().__init__()  # Triggers Grandparent.__init__
        print("Parent initialized")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Triggers Parent.__init__
        print("Child initialized")

instance = Child()
# Output:
# Grandparent initialized
# Parent initialized
# Child initialized


```
   
## Method Chaining   
It is a process of calling multiple methods in a single line on the same object.   
Every method should `return self`.   
   
***Task***: Write example for below.   
# Hierarchical Inheritance   
Single parent → Multiple Child   
```
class Parent:


class child1(Parent):
	attributes a

class child2(Parent):
	attributes b

class child2(Parent):
	attributes c
```
   
# Hybrid Inheritance   
## 1. Hybrid Inheritance   
- **Definition:** A hybrid inheritance structure is a combination of two or more types of inheritance (e.g., combining **Multiple Inheritance** and **Multilevel Inheritance**, or **Hierarchical** and **Multiple**).   
- **The Challenge:** Because classes inherit from multiple paths that may eventually share a common base class, it introduces structural ambiguity and the famous **Diamond Problem**.   
 --- 
   
## 2. The Diamond Problem   
- **Scenario:**   
- Class `A` is the root base class.   
- Class `B` and Class `C` both inherit from `A` (Hierarchical/Multiple path).   
- Class `D` inherits from *both* `B` and `C` (Multiple inheritance).   
- **The Conflict:** If `A` defines a method `show()`, and both `B` and `C` override it (or don't), which version of `show()` does `D` execute when called?   
- Without a strict resolution mechanism, this causes ambiguity, code duplication, or multiple execution of the base constructor (`A`'s `__init__` running twice).   
 --- 
   
## 3. What is MRO (Method Resolution Order)?   
- **Definition:** **MRO** is the specific order in which a programming language (like Python) searches for a method, attribute, or variable in an inheritance hierarchy.   
- **Why it matters:** It provides a predictable, linearized lookup path that completely solves the Diamond Problem and ensures proper method chaining via `super()`.   
- **How to check MRO in Python:**   
- `ClassName.__mro__` (returns a tuple)   
- `ClassName.mro()` (returns a list)   
 --- 
   
## 4. Python’s C3 Linearization Algorithm   
Python uses the **C3 Linearization** algorithm to compute the MRO. It follows three core rules to maintain a consistent hierarchy:   
1. **Local Precedence Order:** Child classes are always checked before parent classes. If a class inherits from `B` then `C` (`class D(B, C):`), `B` comes before `C` in the MRO.   
2. **First-Appearance / Monotonicity:** If a class appears in multiple inheritance paths, it is kept only in its *rightmost/deepest valid position* in the linearization, ensuring a class isn't visited prematurely before its parents are fully resolved.   
3. **Extended Monotonicity:** The relative order of parents in any base class is preserved in the derived class's MRO.   
 --- 
   
## 5. Quick Code Example & Walkthrough   
```
class A:
    def process(self):
        print("A process")

class B(A):
    def process(self):
        print("B process")
        super().process()

class C(A):
    def process(self):
        print("C process")
        super().process()

class D(B, C):
    pass

# Check the Method Resolution Order
print(D.__mro__)
# Output path: D -> B -> C -> A -> object

obj = D()
obj.process()


```
### Execution Flow:   
1. `D` has no `process()`, so it looks at its first parent: `B`.   
2. `B` prints `"B process"` and calls `super().process()`.   
3. According to `D`'s MRO (`D -> B -> C -> A`), the class *after* `B` is `**C**`, not `A`!   
4. Therefore, `super()` in `B` routes to `**C**` (`"C process"`).   
5. `C` calls `super().process()`, which routes to `**A**` (`"A process"`).   
   
   
   
   
   
   
   
   
   
   
   
   
   
