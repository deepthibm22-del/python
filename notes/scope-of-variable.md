---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Backlinks:
    - Python Pentagon Space
Creation date: "2026-10-23T09:29:48Z"
Created by:
    - Predator
id: bafyreif5zbeibfr54va6y6q6kwwxd3cqzaba52exiebz3myfoqv7vineiq
---
# Scope of Variable   
## Scope of Variable   
   
- Represents a region where a particular variable can be accessed.   
- Types   
    1. Global Scope   
        - These are variables declared outside the function and can be accessed from anywhere in program.   
   
           
    2. Local Scope   
        - Variable declared inside the function and can only be used inside the function.   
        - Once function terminates, they are deleted from memory.   
   
       
    3. Enclosing Scope   
       
    4. Built-in Scope   
   
   
- You **can** convert a local variable into a global variable using the `global` keyword, but you **cannot** turn a truly global variable into a local one inside the same global scope.   
   
   
   
- ***Enclosing variable*** are variable in outer function for inner function   
- ***nonlocal*** is used inside inner function to modify ***enclosing variable*** (variable in outer function) inside nested function   
