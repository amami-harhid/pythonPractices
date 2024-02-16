
from sub01 import *
from sub02 import *
# function definition
def main01():
    '''docstring
    numeric calculation
    '''
    sum01 = sub01()
    print("main01, sum01=", sum01)  # <--- main01, sum01= 3
    
    sum02 = sub02( 5, 6)
    print("main01, sum02=", sum02)  # <--- main01, sum02= 11

    sum03 = sub02( 5.5, 6.2)
    print("main01, sum03=", sum03)  # <--- main01, sum03= 11.7

    # integer + float
    sum04 = sub02( 12, 3.333)
    print("main01, sum04=", sum04)  # <--- main01, sum04= 15.333


print(main01.__doc__)

def main02():
    # [+]operations of different types will result in an error.
    try:
        sum01 = sub02( 'ABC', 5)  
        print('main02, sum04=', sum01)
    except TypeError as e:
        print("sub02()=>", e)   # TypeError: can only concatenate str (not "int") to str

    # string + string
    sum02 = sub02( 'ABC', 'xyz')    # "ABC" + "xyz" = "ABCxyz"
    print("main02, sum05=", sum02)  # <--- main02, sum02= ABCxyz


def main03():
    sum01 = sub03(5, 10)            # 5 - 10 = -5
    print('main03, sum01=', sum01)  # <--- main03, sum01= -5
    
def main04():
    sum01 = sub04(5, 10)            # 5 * 10 = 50
    print('main04, sum01=', sum01)  # <--- main04, sum01= 50

def main05():
    sum01 = sub05(5, 10)            # 5 / 10 = 0.5
    print('main05, sum01=', sum01)  # <--- main05, sum01= 0.5

def main06():
    sum01 = sub06(25, 3)            # 25 // 3 = 8
    print('main06, sum01=', sum01)  # <--- main06, sum01= 8

def main07():
    sum01 = sub07(25, 3)            # 25 % 3 = 1
    print('main07, sum01=', sum01)  # <--- main07, sum01= 1

main01()
main02()
main03()
main04()
main05()
main06()
main07()

print( "string01() =" , string01() )  # "1" + "2" = "12"
print( "string02() =" , string02( "5" , "01" ) )  # "5" + "01" = "501"

try:
    print( "string03() =" , string03( "5" , "01" ) )  # "S" - "01" => typeError
except TypeError as e:
    print("string03()=>", e)   # TypeError: unsupported operand type(s) for -: 'str' and 'str'

try:
    print( "string04() =" , string04( "5" , "01" ) )  # "5" * "01" =>  typeError
except TypeError as e:
    print("string04()=>", e)   # TypeError: can't multiply sequence by non-int of type 'str'

try:
    print( "string05() =" , string05( "5" , "01" ) )  # "5" / "01" =>  typeError
except TypeError as e:
    print("string05()=>", e)   # TypeError: unsupported operand type(s) for /: 'str' and 'str'

try:
    print( "string06() =" , string06( "5" , "01" ) )  # "5" // "01" =>  typeError
except TypeError as e:
    print("string06()=>", e)   # TypeError: unsupported operand type(s) for //: 'str' and 'str'

try:
    print( "string07() =" , string07( "5" , "01" ) )  # "5" % "01" =>  typeError
except TypeError as e:
    print("string07()=>", e)   # TypeError: not all arguments converted during string formatting


try:
    print( "string08() =" , string08( "5" , "01" ) )  # "5" % "01" =>  typeError
except TypeError as e:
    print("string08()=>", e)   # TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'str'


# index
indexTestStr = "abcdefg"
print("indexTestStr zero index = ", indexTestStr[0]) # a

# slice 
sliceTestStr = "abcdefg"
print("sliceTestStr 1:5  = ", indexTestStr[1:5]) # bcde

# escape sequence
escapeTestStr = "abcdefg\nXyz"
print("escapeTestStr = ", escapeTestStr)    # abcdefg
                                            # Xyz

# tab sequence
tabTestStr = "abcdefg\tXyz"
print("tabTestStr = ", tabTestStr)       # abcdefg  Xyz

# singleQuotation in singleQuotation
singleQuotTestStr = 'Abcd doesn\'t'
print("singleQuotTestStr = ", singleQuotTestStr)       # Abcd doesn't

# doubleQuotation in doubleQuotation
doubleQuotTestStr = "Name is \"Name\". "
print("doubleQuotTestStr = ", doubleQuotTestStr)       # Name is "Name".

# variables in String(1) double Quot
name = "Gooooo"
variableTestStr1 = f"Name is {name}. "
print("variableTestStr(1) = ", variableTestStr1)       # Name is "Name".

# variables in String(2)  singleQuot
name = "this color's name"
variableTestStr2 = f'What is {name}. '
print("variableTestStr(2) = ", variableTestStr2)       # What is this color's name.

# format
variableTestStr3 = "I was born in {} in {}".format("Amami","2000") 
print("variableTestStr(3) = ", variableTestStr3)       # I was born in Amami in 2000

# if condition 
value = 20

if value < 20:
    print('if condition value < 20')
elif value < 15:
    print('if condition value < 15')
elif value == 20:
    print('if condition value == 20')
else:
    print('if condition others')

# Argument check
def test_func(name, old, address):
    print(f"(1) Name is {name}.")
    print(f"(2) {old} years old.")
    print(f"(3) Address is {address}.")

# Keyword argument-1
test_func( name='Tom', old=20, address='Amami City' )
test_func( address='Amami City', old=20,  name='Tom' )

# Positional argument
test_func( 'Tom', 20, 'Amami City' )

# Keyword argument-2
test_func( **{'address': 'Amami City', 'old': 20,  'name': 'Tom' })

# Lambda ( 1 line method )
add_lambda = lambda a, b : a + b

print( 'add_lambda= ', add_lambda( 12, 20 ))  # --> 32


# Builtin function
## len
testStr = 'Python practice'
print('testStr len = ', len(testStr)) # -->  15

## type
print('testStr type = ', type(testStr)) # -->  <class 'str'>

## dir
print('testStr dir = ', dir(testStr)) 
print('testStr upper = ', testStr.upper()) 

# Loop
## for in array
print('--- for in array ---')
word_lists = ["Python","Pygame","Panda3D"]
for word in word_lists:
    print(word)
    
## wihle condition
print('--- while condition ---')
num = 0
while num < 5:
    print(num)
    num += 1
    
## wihle break
print('--- while break ---')
num = 0
while True:
    print(num)
    num += 1
    if(num > 10) :
        break

## range
print('--- for range ---')
for i in range(5):
    print(i)

for i in range(1, 6):
    if i == 3:
        break
    print(i)

## continue
print('--- continue ---')
for num in range(2, 6):
    if num % 2 == 0:
        print(str(num)+" : even")
        continue
    print(str(num)+" : odd")
    
## for enumerate
print('--- for enumerate ---')
word_lists = ["Python","Pygame","Panda3D"]
for i, word in enumerate(word_lists):
    print(i, word)
    
## for else
print('--- for else ---')
for i in range(5):
    print(i)
else:
    print("-- end --")
    
## for zip
print('--- for zip ---')
num_lists = [1, 2, 3]
word_lists = ["Python","Pygame","Panda3D"]
for num, word in zip(num_lists, word_lists):
    print(num, word)


# Data Stored Objects

## List
sample_list=[ 1, 2, 3, 4, 5 ]  

### List index 
print( 'DataStoredObject List index ', sample_list[ 1 ] )  # --> 2
### List slice
print( 'DataStoredObject List slice ', sample_list[ 2 : 4 ] )  # --> [ 3, 4 ]
### List add
print( 'DataStoredObject List add ', sample_list + [ 9, 'A', 'B'] )  # --> [1, 2, 3, 4, 5, 9, 'A', 'B']
### List append
sample_list.append('X')
print( 'DataStoredObject List append ', sample_list )  # --> [1, 2, 3, 4, 5, 'X']
### List extend
sample_list.extend([99, 100])
print( 'DataStoredObject List append ', sample_list )  # --> [1, 2, 3, 4, 5, 'X', 99, 100]
### List insert
sample_list.insert( 3, 999 )
print( 'DataStoredObject List insert ', sample_list )  # --> [1, 2, 3, 999, 4, 5, 'X', 99, 100]
### List remove
sample_list.remove( 4 )
print( 'DataStoredObject List remove ', sample_list )  # --> [1, 2, 3, 999, 5, 'X', 99, 100]
### List clear
sample_list.clear()
print( 'DataStoredObject List clear ', sample_list )  # --> [ ]

## Tuple

### normal example
t1 = ( 10, "a", [1,2] )   # Can have any type element, separated with commas
print('Tupple(1) = ', t1)  #  (10, 'a', [1, 2])

### example without parentheses
t1 = 10, "a", [1,2]   # Can have any type element, separated with commas
print('Tupple(2) = ', t1)  #  (10, 'a', [1, 2])

### nested structure
t2 = t1, (5, "b", 7)
print('Tupple(3) = ', t2)  #  ( (10, 'a', [1, 2]),  (5, 'b', 7) )

### empty tuple
empty_tuple = ()
print('Tupple(4) = ', empty_tuple)  #  ( )

### number of items = 1 
single_tuple01 = ( "hello" )
print('Tupple(5) = ', single_tuple01)  #  ( "hello")

### number of items = 1 ( no parentheses ,ends with a comma )
single_tuple02 = "Hey ! ",
print('Tupple(6) = ', single_tuple02)  #  ( "Hey ! ", )

### tuple is immutable
try:
    t1[0] = 5
except TypeError as e:
    print('immutable test', e)  # 'tuple' object does not support item assignment

## Dictionary
d = {'key1': 1, 'key2': 2, 'key3': 3}
### delで削除が可能
del d["key1"]
###「キー = 新しい値」で辞書内容を変更できる
d["key2"] = 20
### 辞書にないキーを指定した場合は追加される
d["key4"] = 4
### キーを指定すると値を取り出すことができる
print(d["key3"])
### 空の辞書を生成
empty_dict = {}
print(empty_dict)

## Set : can't have the same value. The order of storage is undetermined.
sample_set1 = {"s", "w", "r", "t", "o", "a", "w","f", "o", "s"}
print('assebly(1) =', sample_set1)
sample_set2 = set("aaattttoooowwwwwffffffsssssssssssk") # The order of storage is undetermined
print('assebly(2) =', sample_set2)

## Arithmetic on sets
### union 
print('union :', sample_set1 | sample_set2) #  {'k', 'a', 'r', 'f', 'w', 'o', 't', 's'}
### Difference set
print('difference :', sample_set1 - sample_set2) # {'r'}
### intersection 
print('intersection :', sample_set1 & sample_set2) # {'a', 'f', 'w', 'o', 't', 's'}
### Symmetric difference set
print('Symmetric difference :', sample_set1 ^ sample_set2) # {'k', 'r'}

# Exception

## try-except , ZeroDivisionError
try:
    1/0
except ZeroDivisionError as e:
    print ('Exception(1):', e) # division by zero

## try-except-finally ( finally : runs all the time)
try:
    notDefineVal * 2
except Exception as e:
    print ('Exception(2):', e) #  name 'notDefineVal' is not defined
finally:
    print ('Exception(2): finally') 

## try-except-else(1)
try:
    notDefineVal * 2
except Exception as e:
    print ('Exception(3):', e) #  name 'notDefineVal' is not defined
else:
    print ('Exception(3): else') 

## try-except-else(1)
defineVal = 2
try:
    defineVal * 2
except Exception as e:
    print ('Exception(4):', e) #  name 'notDefineVal' is not defined
else:
    print ('Exception(4): else') 
    
## raise
defineVal = 2
try:
    defineVal * 2
    raise ZeroDivisionError('Throw an error(5)')
except Exception as e:
    print ('Exception(5):', e) #  name 'notDefineVal' is not defined


# class

## constructor , def
class Person:
    # メソッド
    # __init__に初期化処理を書く。第一引数はself
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

## private variable
class Person:
    def __init__(self, name):
        self.__name = name

p = Person("sato")
p.__name

class Person:
    def __init__(self, name):
        self.__name = name

p = Person("sato")
p._Person__name

## getter

## setter

## static variable

## static def

# class override
class Person:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print('Hello,', str(self.name))

p = Person("tanaka")
p.hello()

class Student(Person):
    def hello(self):
        print('Hello!!!', str(self.name))

s = Student("suzuki")
s.hello()