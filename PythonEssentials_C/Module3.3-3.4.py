### 3.3 - Logic and bit operations in Python

###### 3.1 Computer logic 
# if we have some time AND the weather is good, we will go for a walk
# We´ve used the conjunction "and", which means that going for a walk depends of the simultaneous fulfilment of these two conditions. 
# ALSO CALLED A CONJUNCTION 

# if you are in the mall OR i am at the mall, one of us will buy a gift for mom. 
# the word OR means the purchase depends on at least one of these conditions. 
# ALSO CALLED DISJUNCTION. 

#these are Logical operators. 

####### The "and" operator
# a binary operator with a priority that is lower than the one expressed by the comparison operators. 
# the result provided by the "and" operator can be determined on the basis of the truth table. 
# | argument A  | argument  B   | A and B   |
# | false       | false         | false     |
# | false       | True          | False     |
# | True        | False         | False     |
# | True        | True          | True      |


####### The "or" operator
# a disjunction operator. Its a binary operator with a priority that is lower than "and". (just like in math, + compared to *).
# the result provided by the "or" operator can be determined on the basis of the truth table.
# | argument A  | argument  B   | A or B    |
# | false       | false         | False     |
# | false       | True          | True      |
# | True        | False         | True      |
# | True        | True          | True      |


####### The "not" operator
# Its a unary operator perfonrming a logical negation. 
# simple condition: it turns truth into falsehood and viceversa. 
# high priority, the same as the unary + and -. 

# | Argument    | not Argument|
# | False       | True        |
# | True        | False       |

####### Logical Expressions 
#The negation of a conjunction is the disjunction of the negations. 
#The negation of a disjunction is the conjunction of the negations. 
# not (p and q) == (not p) or (not q)
# not (p or q) == (not p) and (not q)

##### Logical values vs. Single bits
# logical operators take their arguments as a whole regardless of how many bits they contanin. 
# False when the value is 0, and True when at least one bit is set. 
i = 1 # i is a logical value, it is True.
j = not not i # j is True, because i is not 0.


##### Bitwise operators
# There are 4 operator that allow you to manipulate single bits of data. 
# & (ampersand) ‒ conjunción a nivel de bits;
# | (barra vertical) - disyunción a nivel de bits;
# ~ (tilde) - negación a nivel de bits;
# ^ (signo de intercalación) - o exclusivo a nivel de bits (xor).

# & requieres exactamente dos 1 s para proporcionar 1 como resultado;
# | requiere al menos un 1 para proporcionar 1 como resultado;
# ^ requiere exactamente un 1 para proporcionar 1 como resultado.

# Siempre tienen que ser numeros enteros, jamas flotantes.

###### Logical vs. bit operations 
 
i = 15
j = 22

#i: 00000000000000000000000000001111
#j: 00000000000000000000000000010110

#logical1:
log = i and j #True, because both i and j are not 0.

#bit operations1: 
bit = i & j #00000000000000000000000000000110

#logical2:
logneg = not 1 #False, because 1 is not 0.

#bit operations2:
bitneg = ~1 #11111111111111111111111111111110

#### Binary left shift and right shift
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

#17 >> 1 → 17 // 2 (17 floor-divided by 2 to the power of 1) → 8 (shifting to the right by one bit is the same as integer division by two)
#17 << 2 → 17 * 4 (17 multiplied by 2 to the power of 2) → 68 (shifting to the left by two bits is the same as integer multiplication by four)


#################### Notas del capitulo 3.3

# Logical operators: 
 # - and: conjunction (True and true is true)
 # - or: disjunction (True or False is True)
 # - not: negation (not True is False)

# Bitwise operators:
x = 15 #0000 1111
y = 16 #0001 0000
    # - & (ampersand): bitwise AND / x & y = 0 (0000 0000)
    # - | (pipe): bitwise OR / x | y = 31 (0001 1111)
    # - ^ (caret): bitwise XOR / x ^ y = 31 (0001 1111)
    # - ~ (tilde): bitwise NOT / ~x = -16 (1111 0000)
    # - << (left shift): y << 3 = 128 (1000 0000)
    # - >> (right shift): y >> 1 = 8 (0000 1000)

### Section quiz
# What is the output of the following snippet? 
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
# The output will be False.

# What is the output of the following snippet? 
x = 4
y = 1

a = x & y
b = x | y
c = ~x  # tricky!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)

# The output will be:
# 0 5 -5 1 1 16










################### 3.4 - lists 
# to store more than one value in a singe variable. 
# multi-value variables.
# the list starts with [ and ends with ].
# the numbers are separated by commas.
# single value are called scalars, and multi-value variables are called collections.
# the elements inside of a list may have different types. Integers, floats, and even other lists.


# write a program that sorts a sequence of numbers: 
numbers = [10, 5, 7, 2, 1]
# sort the list in ascending order
numbers.sort()  # This will sort the list in place
# print the sorted list
print(numbers)  # Output: [1, 2, 5, 7, 10]

# the variable numbers is a list consisting of five values, all of them numbers
# the first number is zero, so in this 5 number list, the fifth number is 4.

##### Indexing lists 
# Lets assing a new value of 111 to the first element of the list. 

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.

# and now we want the value of the fifth element to be copied to the second element. 
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("New list contents:", numbers)  # Printing current list contents.

##### Accesing list content

print(numbers[0]) # Accessing the list's first element.

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing previous list contents.

numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
print("Previous list contents:", numbers)  # Printing previous list contents.

print("\nList length:", len(numbers))  # Printing the list's length.
# The len() function returns the number of elements in the list.
print()

###### Removing elements from a list
# its done with an instruction named del. Its an instruction, not a function. 
# Point the element to be removed, it will vanish from the list, and the length will be reduced by one. 
numbers = [10, 5, 7, 2, 1]
del numbers[1]
print(len(numbers))
print(numbers)
print()

##### Negative indices are legal 
# An element with an index equal to -1 is the last one in the list.
numbers = [111, 7, 2, 5]
print(numbers[-1]) #5 
# the last accesible element is -4 (the first one)
print(numbers[-4]) # 111

####### LAB - the basics of lists.
# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

#Your task is to:
#write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
#write a line of code that removes the last element from the list (Step 2)
#write a line of code that prints the length of the existing list (Step 3).

hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
hat_list[2] = int(input("Ingresa un nuevo numero al sombrero :) :"))
# Step 2: write a line of code that removes the last element from the list.
del hat_list[-1]
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)

##### Function vs. methods 
# a METHOD is a specific kind of function. it behaves and looks like a function, but differs in the way it is called.
# a FUNCTION doesnt belong to any data. It gets data, may create new data, and returns it.
# a METHOD does all of these things, but it is also able to change the state of a selected entity. 
# a METHOD is owned by the data it works for, while a function is owned by the whole code. 
 
# Function: 
# result = function(argument)

# Method:
# result = data.method(argument)

# # The name method is preceded by the name of the data which owns the metod. 
# Next, you add a dot, followed by the method name, and a pair of () enclosing the arguments. 

##### Adding elements to a list: append() and insert()

# A new element can be added to the END of a list using the append() method.
list.append(value)

# A new element can be added to a SPECIFIC position in a list using the insert() method.
list.insert(location, value)

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)
#
numbers.append(4) # Adding 4 to the end of the list
print(len(numbers))
print(numbers)
#
numbers.insert(0, 222) # Adding 222 to the beginning of the list
print(len(numbers))
print(numbers)

# Start an empty list. (with a pair of square brackets).
## with append() method.
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.append(i + 1)

print(my_list)
# The list now contains five elements: 1, 2, 3, 4, and 5.

# WITH insert() method.
my_list = []  # Creating an empty list.

for i in range(5):
    my_list.insert(0, i + 1)

print(my_list)
# The list now contains five elements: 5, 4, 3, 2, and 1. In reverse order. 

#### Making use of lists. 
# The for loop has a special variant that can process lists effectively.

my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total) # Output: 27


### Segundo aspecto del bucle for:
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total) # Output: 27


#### listas en acción 
# Intercambiar los valores de dos variables.

variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2
# This will not work, because variable_2 is now equal to variable_1, so both variables are equal to 1.

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
# This will work, because we are using an auxiliary variable to store the value of variable_1 before we change it.

#Python ofrece una forma mas conveniente: 
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1

#ej.
my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list) # Output: [5, 3, 8, 1, 10]

########### LAB - Fundamentos de listas los beatles. 
# Paso 1: crear una lista vacía llamada beatles
beatles = []
print("Step 1:", beatles)

# Paso 2: agregar con append() a John Lennon, Paul McCartney y George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Paso 3: usar un ciclo for para pedir al usuario que agregue 2 miembros
# Vamos a usar una lista con los nombres esperados
nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]

for nombre in nuevos_miembros:
    entrada = input(f"Escribe el nombre para agregar ({nombre}): ").strip()
    # Si el usuario no escribe nada, usamos el nombre por defecto
    if entrada == "":
        beatles.append(nombre)
    else:
        beatles.append(entrada)

print("Step 3:", beatles)

# Paso 4: eliminar a Stu Sutcliffe y Pete Best
# Como son los dos últimos, se pueden eliminar así:
del beatles[-2:]  # borra los últimos dos elementos
print("Step 4:", beatles)

# Paso 5: agregar a Ringo Starr al inicio de la lista usando insert()
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Verificar longitud final
print("The Fab", len(beatles))

############ Notas del capitulo 3.4
# A list is a type of data used to store multiple objects. 
my_list = [1, None, True, "I am a string", 256, 0]

# lists can be indexed and updated.
my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list[3])  # outputs: I am a string
print(my_list[-1])  # outputs: 0

my_list[1] = '?'
print(my_list)  # outputs: [1, '?', True, 'I am a string', 256, 0]

my_list.insert(0, "first")
my_list.append("last")
print(my_list)  # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

#Lists can be nested. 
my_list = [1, 'a', ["list", 64, [0, 1], False]]

#Lists elements and lists can be deleted. 
my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)  # outputs: [1, 2, 4]

del my_list  # deletes the whole list

#lists can be iterated over using a for loop.
my_list = ["white", "purple", "blue", "yellow", "green"]

for color in my_list:
    print(color)

# The len() function checks the list length.
my_list = ["white", "purple", "blue", "yellow", "green"]
print(len(my_list))  # outputs 5

del my_list[2]
print(len(my_list))  # outputs 4

# A typical funcition invocation looks as follows: result = function(arg)
# A typical method invocation looks as follows: result = data.method(arg)


