---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Backlinks:
    - Python Pentagon Space
Creation date: "2026-10-22T08:35:23Z"
Created by:
    - Predator
id: bafyreiaw6yr4ryjbml6rtqifohxxbc2lqt4mccw53c64oma5ccqr5rvote
---
# Arguments   
Parameter → Formal Argument   
Arguments → Actual Argument   
   
## Types of Arguments/ parameter   
   
1. Positional Arguments   
2. Default Arguments   
3. Keyword Arguments   
4. Variable Length Argument   
   
   
 --- 
   
### 1. Positional Argument   
   
- These are the mandatory arguments that are passed during functional call, where number of arguments are equal to number of parameters present in defined function.   
- Order of passing the arguments also matters   
   
   
```
def positional(name, age, place):
	print(
	"Name: ", name,
	"\nAge: ", age,
	"\nPlace: ", place
	)
positional(22, 'Raj', 'Bang')
```
   
 --- 
   
### 2. Default Argument   
   
- Default Parameter a **fallback value** assigned to a function parameter in its definition.   
- If you call the function without passing a value for that parameter, Python **automatically uses the default value**.    
- If you do provide a value, it **overrides (overwrites) the default**.   
- All Default Parameter should come after Positional Parameter.   
   
   
```
def default(name, age, place=None, phoen):
	print(
	"Name: ", name,
	"\nAge: ", age,
	"\nPlace: ", place
	)
default(22, 'Raj', 'Bang')
```
   
 --- 
   
### Keyword Argument   
   
- A **keyword argument** is an argument passed to a function by explicitly specifying both the **parameter name and its value** using the `name = value` syntax.   
   
   
```
def keyword(name, age):
	print("Name: ", name, "\nAge: ", age)

keyword(age=10, name='Raj')
```
   
 --- 
   
### Variable Length Argument   
- It is capable of accepting `0 to n` number of arguments.   
- ***Packing*** is the process of combining multiple values into a collection   
- There are Two types   
    1. \*args → accepts `0 to n` number of positional arguments   
        - Creates Tuple packing of all arguments   
   
        ```
        def sample(*args):
        	print(args)
        sample(1,2,4,5,6,7)
        ```
    2. \*\*kwargs → accepts `0 to n` number if keyword arguments   
        - Creates Dictionary Packing of all arguments   
   
        ```
        def sample(**kwargs):
        	print(kwargs)
        sample(a=10, b=20, c=30)
        ```
           
- *Unpacking: * When calling Function if use \*collection , it unpacks collection allocates to corresponding parameters. And the condition for this to work is -
   
    1. \*collection has to be index based   
    2. Length of collection = Number of parameters in function definition.   
   
```
l = [1,2,3,4,5]
def sam(a,b,c,d,e):
	print(a+b+c+d+e)
sam(*l)

```
   
```
a,*b = [1,2,3,4,5]
print(a) # 1
print(b) # [2,3,4,5]

```
   
```
a, *b, c = [1,2,3,4,5]
print(a) # 1
print(b) # [2,3,4]
print(c) # 5

```
   
   
   
   
   
   
   
   
   
   
   
