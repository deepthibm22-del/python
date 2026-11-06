Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#homogeneous list
s[2.5,3.5,4.5,8.5]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s[2.5,3.5,4.5,8.5]
NameError: name 's' is not defined
s=[2.5,3.5,4.5,8.5]
s
[2.5, 3.5, 4.5, 8.5]
s[0]
2.5
s[2]
4.5
>>> id(1[])
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> id(s)
2117811213632
>>> len(s)
4
>>> #heterogeneous list
>>> student=[100,9.5,deepthi,m,true,622]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    student=[100,9.5,deepthi,m,true,622]
NameError: name 'deepthi' is not defined
>>> student=[100,9.5,deep,m,true,622]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    student=[100,9.5,deep,m,true,622]
NameError: name 'deep' is not defined
>>> student=[100,9.5,'deepthi','m','true',622]
>>> student
[100, 9.5, 'deepthi', 'm', 'true', 622]
>>> student[0]
100
>>> student[3][2]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    student[3][2]
IndexError: string index out of range
>>> student[2][2]
'e'
>>> student[3]
'm'
>>> student[4][2]
'u'
>>> student[3]
'm'
>>> student[2]
'deepthi'
>>> student[2]='anusha'
>>> student
[100, 9.5, 'anusha', 'm', 'true', 622]
>>> len(student)
6
>>> #nested list
>>> students=['details'['deepthi',21,'True'],['anusha',20,'False'],'filled']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    students=['details'['deepthi',21,'True'],['anusha',20,'False'],'filled']
TypeError: string indices must be integers, not 'tuple'

students=['details',1,['deepthi',21,'True'],2,['anusha',20,'False'],'filled']

stu
