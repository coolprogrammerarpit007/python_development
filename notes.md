<!-- Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 234
y = 35
z = 123
 add = x + y + z
 
SyntaxError: unexpected indent
add = x + y +z
add
392
40 + 2.23
42.23
'chai' + 'code'
'chaicode'
x,y,z
(234, 35, 123)
x + 6 , y + 15
(240, 50)
y % 2
1
x ** 2
54756
result = 1/3.0
result
0.3333333333333333
1 < 2
True
if 1:
    print('hello')

    
hello
x < y < z
False
1 == 2 < 3
False
1 == True
True
1 == 2
False
False < 3
True
1 == 2 and 2 < 3
False
import math
math.floor(3.5)
3
math.trunc(2.8)
2
99999999999999999999999999 + 785
100000000000000000000000784
2 ** 250
1809251394333065553493296640760748560207343510400633813116524750123642650624
2 + 1j * 3
(2+3j)
(2 + 1j) * 4
(8+4j)
0o20
16
0xff
255
oxA
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    oxA
NameError: name 'oxA' is not defined
0xA
10
0o64
52
oct(52)
'0o64'
bin(64)
'0b1000000'
int(3.145)
3
int('64',2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int('64',2)
ValueError: invalid literal for int() with base 2: '64'
x = 1
import random
random.random()
0.657325671451453
random.randint(1,50)
41
41
41


random.choice([1,5,9,65,78,98])
5
0.1 + 0.1 + 0.1
0.30000000000000004
0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17
from decimal import decimal
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    from decimal import decimal
ImportError: cannot import name 'decimal' from 'decimal' (C:\Users\Dell\AppData\Local\Programs\Python\Python313\Lib\decimal.py). Did you mean: 'Decimal'?
from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
Decimal('0.3')
set1 = {1,2,3,4,5}
set1 & {1,3}
{1, 3}
set1 | {1,3,7}
{1, 2, 3, 4, 5, 7}
{1,2,2,3,3}
{1, 2, 3}
{1,2,2,3,3,5,9} | {9,8,5,3,1}
{1, 2, 3, 5, 8, 9}
set1 - {1,2,3,4,5}
set()
type(set())
<class 'set'>
true
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
True
True
True == 1
True
False == 0
True
True + 100
101
!False
SyntaxError: invalid syntax
False
False
not(False)
True
True
True
5 !== 3
SyntaxError: invalid syntax
5 != 4
True
""" Hello"""
' Hello'
chai = "Masala Chai"
first_char = chai[0]
print(first_chai)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print(first_chai)
NameError: name 'first_chai' is not defined. Did you mean: 'first_char'?
print(first_char)
M
sliced_chai = chai[0:6]
sliced_chai
'Masala'
num_list = [0,1,2,3,4,5,6,7,8,9]
num_list[:]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list[7:]
[7, 8, 9]
str = "0123456789"
str[0:8:2]
'0246'
chai.lower()
'masala chai'
chai.upper()
'MASALA CHAI'
chai = "         Lemon Tea ";
chai.strip()
'Lemon Tea'
print(chai.replace("Lemon","Ginger"))
         Ginger Tea 
str = "Lemon,Ginger,Masala,Mint"
str.split(',')
['Lemon', 'Ginger', 'Masala', 'Mint']
chai = "Masala Chai"
chai.find('c')
-1
chai.find('L')
-1
chai.find('M')
0
chai = "Masala chai chai chai"
chai.count('chai')
3
chai_type = "Masala"
quantity = 10
order = f"I ordered {quantity} cups of {chai_type} chai"
order
'I ordered 10 cups of Masala chai'
str
'Lemon,Ginger,Masala,Mint'
chai_variety = str.split(',)
                         
SyntaxError: unterminated string literal (detected at line 1)
chai_variety = str.split(',')
                         
chai_variety
                         
['Lemon', 'Ginger', 'Masala', 'Mint']
chai_str = " ".join(chai_variety)
                         
for chai in chai_variety:
            print(chai)

                         
Lemon
Ginger
Masala
Mint
chai_quote = "He said, \"Masala Chai is Awesome \" "
                         
chai_quote
                         
'He said, "Masala Chai is Awesome " '
'He said, "Masala Chai is Awesome " '
                         
'He said, "Masala Chai is Awesome " '
masala_chai = "Masala \n Chai"
                         
masala_chai
                         
'Masala \n Chai'
masala_chai = r"Masala \n Chai"
                         
masala_chai
                         
'Masala \\n Chai' -->
