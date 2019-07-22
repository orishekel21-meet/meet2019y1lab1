Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=5
>>> b
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> a=10
>>> a=b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=b
NameError: name 'b' is not defined
>>> b=10
>>> a=5
>>> a=b
>>> b=a
>>> a
10
>>> b
10
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> a=5
>>> b=10
>>> a=b
>>> a
10
>>> a=5
>>> c=a
>>> b
10
>>> a=b
>>> b=c
>>> b
5
>>> a
10
>>> b
5
>>> four='4'
>>> print(four*3)
444
>>> five=4
>>> print(5)
5
>>> print(five**3)
64
>>> print(five*3)
12
>>> my_name='student'
>>> print("hi,"+Myname')
	  
SyntaxError: EOL while scanning string literal
>>> print('hi'+my_name)
	  
histudent
>>> my_age = 15
>>> print('I am ' + my_age + 'years old')
	  
SyntaxError: multiple statements found while compiling a single statement
>>> 5*4
	  
20
>>> score=4
	  
>>> count=
