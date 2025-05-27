####################2.1 The "Hello wolrd" program

#Ejercicio 1 Instructions
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")

#Python escpae and newline characters
print("The itsy bitsy spider\nclimbed up the waterspout.") #\n the escape character n viene de newline
print()
print("Down came the rain\nand washed the spider out.")

#using multiple arguments
print() 
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

#Positional arguments * positional way - the argument is dictated by the position
print()
print("My name is", "Python.")
print("Monty Python.")

#Keyword arguments 
print()
print("My name is", "Python.", end=" ")
print("Monty Python.")
#keyword argument end=" " is used to avoid the new line
#RULES - 1. 3 elements. A keyword, an equal sign, and a value 
#       2. The keyword has to be put after de last positional argument

print("My", "name", "is", "Monty", "Python.", sep="-")
#sep = "-" is used to separate the arguments with a "-"

print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
#mixed invocations




############LAB FORMATTING THE OUTPUT #############
#Original
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")



#Todo en una sola linea
print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#duplicar la flecha, nota- se añadio el espacio que estaba antes de los asteriscos al final
print("    *     " *2)
print("   * *    " *2)
print("  *   *   " *2)
print(" *     *  " *2)
print("***   *** " *2)
print("  *   *   " *2)
print("  *   *   " *2)
print("  *****   " *2)

####### notas del capitulo 

# print is a built-in function, always available.
# To call a function, use the function name followed by parentheses. 
# Computer programs are collections of instructions. 
# the backslahes (\) announces that the charachter that follows has a different meaning. ej.\n (newline)
# positional arguments are dictated by their position.
# keyword arguments are dictated by the keyword not by their location. 
# The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments, e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.








######################2.2 Pythons Literals 

#literals 
print(
)
print("2")
print(2)
#ambos se imprimen igual, pero el primero es un string de texto y el segundo un entero tomado como literal.

#Integers 
#enteros, son numeros sin decimales with a fractional part. 

#Floating-point numbers 
#números de punto flotante, son números con decimales. 

#The Type. Characteristics of numeric value which determines its kind, range, and application. 
#You can writte large numbers 11111111 o 11_111_111

#Octal and Hexadecimal numbers
#If an integer number is preceded by an 0O or 0o prefix (zero-o), it will be treated as an octal value. This means that the number must contain digits taken from the [0..7] range only.
print()
print(0o123) 
# es igual a 83 en decimal

#if an integer is preceded by 0x is a hexadecimal value. This means that the number must contain digits taken from the [0..9] only 
print(0x123)
#es igual a 291 en decimal

#Floats 
#Non empty decimal fraction ej. 2.5 y -0.4
#Note - Siempre utilizar el punto (.) como separador decimal, no la coma (,)

#Ints VS. Floats
4
4.0 
#4.0 is a float, 4 is an int. Asi los recconoce Python
#*tmb se puede usar la "e" para utilizar la notacion cientifica
# 300000000 = 3 x 10^8
# en python se puede escribir como 3e8 
print()
print(3e8)
print(300000000)

#Coding floats  
#To record numbers very small, es decir, close to zero. 

#Planck´s constant (h) = 6.62607015 x 10^-34
#Planck´s constant (h) = 6.62607015e-34 
print()
print(6.62607015E-34)

#python uses a different notation for very small numbers.
print(0.0000000000000000000001) 
#este es el resultado = 1e-22


#Strings
#To process text not numbers. 
#Rules: -Strings need quotes. 

# How to encode a quote in a string?
#1. Use backslash (\) to escape the quote.
print()
print("I like \"Monty Python\"")
#2. Use an apostrophe (') instead of a quote (") to enclose the string.
print('I like "Monty Python"')
print()

#For abbreviations, use a backslash (\) to escape the apostrophe.
print('I\'m Monty Python.')
print("I'm Monty Python.")

#Boolean Values
#True and False - 1 Y 0 
#Gorge Boole (1815-1864) - matematico ingles que invento el algebra booleana.
print()
print(True > False)
print(True < False)

###########LAB - LITERALS - Strings ###########

#Write a one-line piece of code, using the print() function, as well as the newline and escape characters, to match the expected result outputted on three lines.

#Expected output: 
# "I'm"
# "learning"
# "Python"
print("\"I´m\"\n\"\"learning\"\"\n\"\"\"Python\"\"\"")

######### Notas del capitulo 
#Literals are notations for fixed values in code. Ej. a literal can be a number(123) or a string ("im a literal")
#The binary system is a base-2 numeral system that uses only two symbols: 0 and 1.
#The octal system is a base-8 numeral system that uses the digits 0 to 7.
#The hexadecimal system is a base-16 numeral system that uses the digits 0 to 9 and the letters A to F.
#Integers (Ints) Are numerical types . ej (256) o (-1)
#Floating point numbers (Floats) Are  numerical types. ej (3.14) o (-0.5)
#Boolean values (Booleans) Are logical types. ej (True) o (False)
#The None literal. Used to represent the absence of a value or a null value.









##########################2.3 Operators - Data manipulation tools

#Python as a calculator
print(2+2)

#Basic operators 
# +
# - 
# * 
# / 
# // 
# % 
# **  

#Exponentiation 
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#When both ** arguments are integers, the result is an integer.
#When at least one ** argument is a float, the result is a float.

#Multpilication 
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#Division 
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
#Exception for the rule. 
#The result by the division is always a float. 

#Integer division (Floor division)
print()
print(5 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
#It differs from the normal division in 2 things:
#1. The result is rounded down to the nearest integer. 
#2. It conforms to the integer vs. float rule. 
print()

print(6 // 4)
print(6. // 4)
print()
print(-6 // 4)
print(6. // -4)
#Rounding always goes to the lesser integer. 

#Remainder (modulo)
print()
print(14 % 4)
#remainder left after the integer division

#Addiition 
print()
print(-4 + 4)
print(-4. + 8)

#Substraction 
print()
print(-4 - 4)
print(4. - 8)
print(-1.1)
#It can also change the sign of a number.
# the minus operator expects two arguments: 
# the left (a minuend in arithmetical terms) and right (a subtrahend).

#Operators and their priorities
#Hierarchy of priorities. 
#Bindings (enlaces). Determines the order of computation performed by some operators with equal priority.
print()
print(9 % 6 % 2)
#Se tiene un enlace de izq a der. 

print(2 ** 2 ** 3)
#eL enlace es de der a izq. Por la exponenciacion.

print(-3 ** 2) # -9
print(-2 ** 3) # -8
print(-(3 ** 2)) # -9

print(2 * 3 % 5) # 1
    
#Operators and parentheses
#Subexpressions in parentheses are always calculated first.
print()
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
    
########### Notas del capitulo
#An expression is a combination of values. (1+2)
#Operators are special symbols or keywords whom perfor mathematical operations. (x * y)
#Arithmetic operators in python: + addition, - substraction, * multiplication, / division, // integer division(rounded down to the nearest number), % modulo(remanente de division), ** exponentiation
#An unary operator (-1) 
#A binary operator (1+2)
#Hierarchy of priorities. ** highest. 
#Subexpression in parentheses are always calculated first.
#The exponentiation operator (**) is right sided binding. From right to left.







######################## 2.4 - Variables 
#The contect of these containers can be varied (almost) any way.
#What does a variable has? A name; and a value.

#Variable names #Rules:
#1. A variable name can contain letters, digits, and underscores (_).
#2. A variable name cannot start with a digit.  
#3. A variable name cannot contain spaces.
#4. A variable name cannot be a Python keyword.

#How to create a variable
#A variable comes into existence as a result of assigning a value to it. 
#Will be automatically created when you assign a value to it.
print()
var = 1
print(var)
#Just name de desired varibale, then the equal sign, and then the value you want to put into the variable.

#How to use a variable
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

var = "3.8.5"
print("Python version: " + var)
#You can combine text and variables using the + operator.

#How to assign a new value to an already existing variable
#With the equal sign. Its an assignment operator. 
#It assigns the value of its right to the left. 
print()
var = 1
print(var)
var = var + 1
print(var)

#Solving simple mathematical problems.
#Pythagorean theorem
#The square of the hypotenuse (c) is equal to the sum of the suares of the other two sides (a and b).
print()
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

#LAB - Variables
#Once upon a time in Appleland, John had three apples, Mary had five apples, and Adam had six apples. They were all very happy and lived for a long time. End of story.
john = 3
mary = 5
adam = 6

print (john, mary, adam, sep=",")

total_apples = (john + mary + adam)
print("Total number of apples:", total_apples)

#Shortcut operators 
#Use one and the same variable both to the right and left of the = operator.
print()

x= 5

x = x * 2
#sheep = sheep + 1

x *= 2
#sheep += 1
#The above code is equivalent to the previous one, but it is shorter and easier to read.
#Variable = variable op expression (x = x * 2)
#variable op= expression (x *= 2)

# i = i + 2 * j / i += 2 * j
#var = var / 2   -  var /= 2
#rem = rem % 10  / rem %= 10

#### LAB VARIABLES - a simple converter

#Bearing in mind that 1 mile is equal to approximately 1.61 kilometers, complete the program in the editor so that it converts:
#miles to kilometers;
#kilometers to miles.
print()

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
#round() is used to round the result to 2 decimal places.


###### LAB Operators and expressions 
#Complete the code in order to evaluate the following expression:
#3x^3 - 2x^2 + 3x - 1
print()
x =  0
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1 
print("y =", y)

x = 1 
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
print("y =", y)
print()

########## NOTAS DEL CAPITULO
#A variable is a named location reserved to store values in the memory. Its created automatically when you assign a value to it.
#Each variable must have a unique name (identifier). Beginning with a _ or a letter. And it cannot be a Python keyword.
#Python is a dinaamically-typed language. Meaning you dont need to declare variables in it. Just =
#Compound assignment operators (shortcut operators) ej. var += 1 o var /= 5 * 2
#You can assign new values to already existing variables. for ej: 
var = 2
print(var)
var = 3
print(var)
var += 1
print(var)
# You can combine text and variables using the + operator with the print() function. ej:
print()
var = "007"
print("Agent " + var)









######################### 2.5 - Comments
#A remark inserted into the program, which is ommited at runtime.
# This program evaluates the hypotenuse c.
# a and b are the lengths of the legs.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5  # We use ** instead of a square root.
print("c =", c)
print()

#Marking fragments of code 
#Select the lines to modify into comments and press (Command + / )

####LAB - Comments
#this program computes the number of seconds in n number of hours
hrs = 2 # number of hours
s = 3600 # number of seconds in 1 hour
print("Hours: ", hrs) 
print("Seconds in hours: ", hrs * s) 
print("Thanks for using! Goodbye :)")
print()
#this is the end of the program that computes the number of seconds in 2 hour

################### NOTAS DEL CAPITULO
#Comments can be used to leave additional information in code. Ommited at runtime. 
#Piece of text that begins with a hash (#) symbol. 
#You can use comments to mark a piece of code taht is not needed at the moment. 
#Whenever possuble, give self-commenting names to variables. 
#Comments make the program easier to read and understand.







######################### 2.6 - Interaction with the user

#The input() function.
#The meaning of the function is to return a very usable result. 
#The input() function is able to read data entered by the user and return the same data to the running program. 
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")
print()
#The program prompts the user to imput some data. 
#You need to assign the result to a variable; CRUCIAL. 

#The input() function with an argument. 
print()
anything = input("Tell me anything...")
print("Hmm...", anything, "...Really?")
print()
#The input function is invoked with one argument, its a string containing a message.

#The result of the input() function.
#is always a string. 
#You mustn´t use it as and argument of any arithmetic operation.
#    anything = input("Enter a number: ")
#    something = anything ** 2
#    print(anything, "to the power of 2 is", something)
#IT WONT WORK.
#The input() function - prohibited operations. 
#You tried to apply the ** operator to str accompaniend with a float.

#Type casting (type convesion)
#Python offers 2 simple functions to sepcify data types. int() and float().
#int() takes one argument and tries to convert it to an integer. ej. int(string) - int("123") = 123
#float() takes one argument too but converts it to a float. ej. float(string) - float("123.45") = 123.45
#You can invoke any of these by passing the input() results directly to them. 
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)
print()

#More about input() and type casting 
#Having a team consistinf of the trio - input(), int(), and float().
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)
print()
#If you put negative values, la compu no se da cuenta del error. lo arreglamos mas adelante. 
#la variable hypo solo se usa con la finalidad de save the result. 
#Asi la podemos eliminar: 
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)
print()

#String operators
#Regresamos a: + y *. They have a second function other than just arithmetic operations.
#the plus sign (+), when applied to two strings, becomes a concetenation operator; 
#Glues two strings into one. 
#To use it correctly, both arguments must be strings. 
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")
print()
#Replication operator (*)
#The asterisk (*) when applied to a string and number becomes a replication operator. 
"james" * 3 # "jamesjamesjames"
3 * "miri" #"mirimirimiri"
5 * "2" #"22222"
#a number less than 0 prduces an empty string. 

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


