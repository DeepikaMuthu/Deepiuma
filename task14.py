1)#IndexError:
L1=[1,2,3]
>>> L1[3]
Traceback (most recent call last):
File "<pyshell#18>", line 1, in <module>
            
L1[3]

IndexError: list index out of range

#ModuleNotFound:
import notamodule
Traceback (most recent call last):
File "<pyshell#10>", line 1, in <module>
import notamodule

ModuleNotFoundError: No module named 'notamodule'

#KeyError:
	D1={'1':"aa", '2':"bb", '3':"cc"}
>>> D1['4']
Traceback (most recent call last):
File "<pyshell#15>", line 1, in <module>

D1['4']
KeyError: '4'

#ImportError:
	from math import cube
Traceback (most recent call last):
File "<pyshell#16>", line 1, in <module>
from math import cube

ImportError: cannot import name 'cube'

#Stoplteration:
it=iter([1,2,3])
>>> next(it)
1
>>> next(it)
2
>>> next(it)
3
>>> next(it)
Traceback (most recent call last):
File "<pyshell#23>", line 1, in <module>
            
next(it)
StopIteration

#TypeError:
	'2'+2
Traceback (most recent call last):
File "<pyshell#23>", line 1, in <module>
            
'2'+2
TypeError: must be str, not int

#ValueError:
	int('xyz')
Traceback (most recent call last):
File "<pyshell#14>", line 1, in <module>
            
int('xyz')
ValueError: invalid literal for int() with base 10: 'xyz'

#NameError:
	age
Traceback (most recent call last):
File "<pyshell#6>", line 1, in <module>
            
age
NameError: name 'age' is not defined

#ZeroDivisionError:
	=100/0
Traceback (most recent call last):
File "<pyshell#8>", line 1, in <module>
            
x=100/0
ZeroDivisionError: division by zero

#KeyboardInterrupt:
name=input('enter your name')
enter your name^c
Traceback (most recent call last):
File "<pyshell#9>", line 1, in <module>
            
name=input('enter your name')
KeyboardInterrupt

2)#simple calculator with try and except function:
	 try:
  # prompt user
    num1 = float(input("Please Enter The first number: "))
    operator = input("Please choose the operator (+) for addition, (-) for subtraction, (*) for multiplication"
                     "(/) for division , (%) for remainder: ")
    num2 = float(input("Please Enter The second number: "))
    
    if operator == '+':
        result = num1 + num2
        print("The result is: ", result)
    elif operator == '-':
        result = num1 - num2
        print("The result is: ", result)
    elif operator == '*':
        result = num1 * num2
        print("The result is: ", result)
    elif operator == '/':
        try:
            if True:
                result = num1 / num2
                print(result)
        except ZeroDivisionError as err:
            print(err, " oops! zero division occur ")
    elif operator == '%':
        if operator == '%':
            result = num1 % num2
            print("The result is: ", result)
    else:
        raise TypeError


except ValueError:
    print("wrong value, suggest integer or decimal")
finally:
    print("All Done")
    
3)
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
  4)
  age=int(input('Enter your age: '))

if age <= 21:
    print('You are not allowed to enter, you are too young.')
else:
    print('Welcome, you are old enough.')