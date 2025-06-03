print()
print("Modulo 3")
######## 3.1 Making decisions in Python. 

# A programmer writes a program and the program asks questions. 
# Only two possible answers: Yes, this is true or No, this is false.
# to ask questions, Python uses a set of very special operators. 

#Comparison: equality operator
# Are two values equal?
# = is an assignment operator. ej. a = b / a with the value of b
# == is the question "Are these two values equal?" ej. a == b / compares a and b
# Binary operator with left side binding. 

2 == 2 # True
2 == 2. # True (python automaticamente cambia de float a int)
2 == 3 # False
# note* True and False are Python keywords. 

#Operators

# Equality: te equal operator ==
#Compares two values of two operands. If they are equal, the result is True, otherwise False. 
print()
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)
print()

#Inequality: the not equal operator !=
# the != (not equal to) compares 2 values o 2 operands.
# If they are not equal the result is True, otherwise False.
print()
var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)
print()

#Comparison: greater than operator >
# the > (greater than) compares 2 values or 2 operands.
mini = 13
maxi = 20
print(mini > maxi) #False xq maxi tiene valor de 20
print()

#Comparison: greater thar or equal to >=
# The greater than operator has another non-strict variant; >= 
# Binary operators with left-sided binding. 
#With greater priority than == and !=
climita = 24
print (climita >= 22)
print()

#Comparison: less than/ less than or equal to <=
current_velocity_mph = 84
current_velocity_mph < 85  # Less than
current_velocity_mph <= 85  # Less than or equal to
print()


### Making use of the answers
# 2 possibilities:
#   1. Memorize it (store it in a variable)
#       ej. answer = number_of_lions >= number_of_lionesses
#   2. Make a decision about the future of the program. 
#       *special instructions needed... ahead ? 

# Note - UPDATE PRIORITY TABLE
# 1. + , - (unary)
# 2. **
# 3. * , / , // , %
# 4. + , - (binary)
# 5. < , <= , > , >=
# 6. == , !=

######## LAB - Questions and answers
#Using one of the comparison operators in Python, write a simple two-line program 
# that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

n = int(input("Introduce un numero:"))
print ("el numero es mayor a 100?",n >= 100)
print()

#Conditions and conditional execution 
# Do something if a condition is met, and not do it if it isn´t
# It´s called Conditional instruction (or conditional statement)
#       Ej
#          if true_or_not:
#             do_this_if_true
#   *elementos de la conditional statement
#       - if keyword
#       - one or more white spaces
#       - an expression whose value will be interpeted in terms of True and False
#       - a colon(:) followed by a newline
#       - an indented instruction or instructions (at least 1)
#       - take at least 4 spaces or a tab
# Como funciona? 
#   - Si la expresión true_or_not representa la verdad (su valor no es cero), las sentencias con sangria se ejecutaran 
#   - Si la expresion no representa la verdad (igual a cero) las sentencias se omitiran. 
# No condicionales: 
#            if the_weather_is_good:
#                    go_for_a_walk()
#            have_lunch()

#Conditional execution: the if statement
# if sheep_counter >= 120: # Evaluate a test expression
#     sleep_and_dream() # Execute if test expression is True
# if the sheeps are more or 120 go to sleep and dream
# conditionally executed statements havet to be intented:
# if sheep_counter >= 120:
#     make_a_bed()
#     take_a_shower()
#     sleep_and_dream()
# feed_the_sheepdogs()
# feed the dogs isnt intended, it happens anyway.

# Conditional execution: the if-else statement
# if the conditions are met perform the statement, if not it wiltt perform the second statement.
#   ej. 
#    if true_or_false_condition:
#       perform_if_condition_true
#    else:
#        perform_if_condition_false
# *note else is also a Keyword in python

#The if-else statement: more conditional execution 
# we can describe the plan as follows: 
    # if the_weather_is_good:
    #     go_for_a_walk()
    # else:
    #     go_to_a_theater()
    # have_lunch()
# If the weather is good, we´ll go to a walk, otherwie, we´ll go to the theater. 
# No matter the weather, we´ll have lunch afterwards

#Nested if-else statement 
# Case where the instruction after if is another if
    # if the_weather_is_good:
    #     if nice_restaurant_is_found:
    #         have_lunch()
    #     else:
    #         eat_a_sandwich()
    # else:
    #     if tickets_are_available:
    #         go_to_the_theater()
    #     else:
    #         go_shopping()
# This use of the if statement is known as nesting.
# Very important to remember the identation. 

#The elif statement 
# elif is used to check more than just one condition, and to stop when the first statement which is true is found. 
    # if the_weather_is_good:
    #     go_for_a_walk()
    # elif tickets_are_available:
    #     go_to_the_theater()
    # elif table_is_available:
    #     go_for_lunch()
    # else:
    #     play_chess_at_home()
 # If the weather is fine, go for a walk, otherwise if we get tickets, go to the theater, otherwise if there are free tables, go to lunch, if all else fails, stay home and play chess. 
 # elif is like saying otherwise
# if-elif-else is sometimes called a cascade. 
#notes* 
#   1- You musn´t use else without a preceding if; 
#   2- else is always the last branch of the cascade. 
#   3- If there isn´t a else branch, its possible that none of the branches is executed. 

#Analazing code samples 
# Read two numbers
number1 = int(input("Ingresa el primer numero:"))
number2 = int(input("Ingresa el segundo numero:"))

if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

print("El numero mas grande es:", larger_number)
print()

# Largest of 3 numbers

num1 = int(input("Introduce el primer numero:"))
num2 = int(input("Introduce el segundo numero:"))
num3 = int(input("Introduce el tercer numero:"))

largest_num = num1

if num2 > num1:
    largest_num = num2 
if num3 > largest_num:
    largest_num = num3

print("El numero mas grande es:", largest_num)
print()

# Pseudocode and instruction to loop
# Writing the algorithm, not necesseraly real programming.
# formalized, concise and readable. Its called Pseudocode
    # largest_number = -999999999
    # number = int(input())
    # if number == -1:
    #     print(largest_number)
    #     exit()
    # if number > largest_number:
    #     largest_number = number
# We assgn the variable largest_number to the smallest number = -99999999999
# When the value -1 is enteed, it will be a sign that there are no more data, and the program ends.
# Otherwise, if the value is different from -1, the program will read another number, and so on. 
# Performing a certain part of the code more than once is called a loop. 

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
largest_number = max(number1, number2, number3)
# Print the result.
print("The largest number is:", largest_number)
print()
#note* you can also use the min() function to find the smallest number. 

######LAB - Comparison operators and conditional execution.
#Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

# Write a program that utilizes the concept of conditional execution, takes a string as input, and:

# prints the sentence "Yes - Spathiphyllum is the best 
# plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
# prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
# Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

plant = input("Ingresa el nombre de la mejor planta ever! :")

if plant == "spathiphyllum":
    print("No, quiero la big Spathiphyllum! No olvides la mayuscula")
elif plant == "Spathiphyllum":
    print("GRACIAS!!  SIII Spathiphyllum es la mejor planta ever <3")
else: 
    print ("Te prometo que", plant, "no es :(")
print()


####lAB eesentials of the if-else statement
# Once upon a time there was a land – a land of milk and honey, inhabited by happy and prosperous people. The people paid taxes, of course – their happiness had limits. The most important tax, called the Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:

# if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was what they called tax relief)
# if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
# Your task is to write a tax calculator.

income = float(input("Cual es tu ingreso anual de thalers?: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + ((income - 85528) * .32 ) 

if tax < 0:
    tax = 0.0

tax = round(tax, 0)
print("Tu impuesto a pagar son:", tax, "thalers")
print()

######LAB - Essentials of the if-elif-else statement
# As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.

# Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

# if the year number isn't divisible by four, it's a common year;
# otherwise, if the year number isn't divisible by 100, it's a leap year;
# otherwise, if the year number isn't divisible by 400, it's a common year;
# otherwise, it's a leap year.

# The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
# It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

year = int(input("Ingresa un año:"))

if year < 1582:
    print("No esta dentro del calendario gregoriano")
else: 
    if year % 4 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    elif year % 400 != 0:
        print("Common year")
    else:
        print("Leap year")
print()

################# Notas del capitulo 
# The comparison (relational) operators are used to compare values. The table below illustrates how the comparison operators works:
# x = 0 , y = 1 , z = 0:
# ( == ) (Arroja True si los valores son iguales, False si no) (x == y #False) (x == z #True)
# ( != ) (Arroja True si los valores NO son iguales, True si si son) (x != y #True) (x != z #False)
# ( > ) (Mayor  que) (x > y #False)
# ( < ) (Menor que) (x < y #True)
# (>=) Mayor o igual a (<=) menor o igual a
#
#When you want to execute some code only if a certain condition is met. Use CONDITIONAL STATEMENT
#a single if statement:
x = 10
if x == 10: # condition
    print("x is equal to 10")  # Executed if the condition is True.
#a series of if statements:
x = 10
if x > 5: # condition one
    print("x is greater than 5")  # Executed if condition one is True.
if x < 10: # condition two
    print("x is less than 10")  # Executed if condition two is True.
if x == 10: # condition three
    print("x is equal to 10")  # Executed if condition three is True.
    # Each statement is tested separately
# An if-else statement:
x = 10
if x < 10: # condition
    print("x is less than 10")  # Executed if the condition is True.
else:
    print("x is greater than or equal to 10")  # Executed if the condition is False.
# A series of "if" statements followed by an "else":
x = 10 
if x > 5:
    print("x is greater than 5")
if x < 10:
    print("x is less than 10")
if x == 10:
    print("x is equal to 10")
    #The body "else" is executed if the last "if" is False
# The if- elif - else statement
x = 10
if x == 10: # True
    print("x == 10")
if x > 15: # False
    print("x > 15")
elif x > 10: # False
    print("x > 10")
elif x > 5: # True
    print("x > 5")
else:
    print("else will not be executed")
    # If the condition for "if" is False, the program checks the conditions of the subsequent "elif" blocks - the first "elif" block that is True is executed.
    #If all the conditions are False, the "else" block will be executed
#Nested conditional statements: 
x = 10
if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")








############# 3.2 - Loops in Python 

# Looping your code with "while":
    # while there is something to do (while)
        #do it (instruction)
# Pretty similar to the if instruction. "if" performs its statement only once. "while" REPEATS the execution as long as the condition evaluates to True.
# Algorithm ej: 
 # while conditional_expression:
 #     instruction_one
 #     instruction_two
 #     instruction_three
 #     :
 #     :
 #     instruction_n
# If you want to execute more than one statement inside one "while" loop, you must (as with if) indent all the instructions in the same way. 
# The instruction(s) executed inside the "while" loop is called loop´s body.
# if the condition is False as early as when it is tested for the first time, the body is not executed even once.
# The body should be able to change the condition´s value, because if the condition is True at the beginning, the body might run continuosly to infinity. 

#An infinite loop 
# Also called endless loop. Sequence of instructions in a program which repeat indefinitely. 
    # while True:
    #     print("Im stuck in a loop")
 #Lo va a correr infinatemente en tu pantalla hasta que lo interrumpas con Ctrl + c

#Loop to find the largest number from a large set of entered data. 
# Store the current largest number here.
largest_number = -999999999
# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))
# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))
# Print the largest number.
print("The largest number is:", largest_number)
print()

# More examples: the "while" loop

# A program that reads a sequence of numbers and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
odd_numbers = 0
even_numbers = 0
# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))
# 0 terminates execution.
while number != 0: #Se puede poner omitir el "!= 0" ya que python 0 es False, y cualquier otro numero es True
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))
# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

# Using a "counter" variable to exit a loop
counter = 5
while counter != 0:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)
# The code is intented to print the string "Inside the loop" and the value stored in the variable during a given loop exactly five times. 
# Once the condition has not been met (counter = 0) the loop is exited, and the message "Outside the loop" as well as the value stored in counter is printed. 

####### LAB - Guess the secret number 
secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
num = int(input("Prueba tu suerte... :"))
while num != secret_number:
    print("Ese no es!!! jajaj try again :)")
    num = int(input("Prueba tu suerte... :"))
print ("Siiii! Como supiste?")
print()

# Looping your code with "for"
# Sometimes it´s more important to count the "turns" of the loop than check the conditions.
# ej. Imagine a loop´s body that needs to be executed exactly 100 times. Using the while may look like this:
    # i = 0
    # while i < 100:
    #     # do_something()
    #     i += 1
# We use "for" para que el lo cuente por nosotros. 
    # for i in range(100):
    #     # do_something()
    #     pass
 #new elements: 
 # the "for" keyword opens the "for" loop; note - there is no condition after it; you dont have to think about conditions, as they´re checked internally, whithout any intervention. 
 # any variable after the for keyword is the control variable of the loop; it counts the loop´s turns, automatically.
 # the "in" keyword introduces a syntax element describing the range of possible values being assigned to the control variable. 
 # the range() function is responsible for generating all the desired values of the control variable; in our example, the function will create (feed the loop) subsequent values form the following set: 0,1,2...,97,98,99. The range() starts from 0 and finishes 1 number before the value of its argument.
 # the pass keyword inside the loop body - it does nothing, its an empty instruction. We put it because the for loop´s syntax demands at least one instruction inside the body. 

# ej:
for i in range(10):
    print("The value of i is currently", i)
print()
# the loop is executed ten times (range)
# the last variable is 9 NOT 10 (its starts from 0, not from 1)

# ej with 2 arguments: 
for i in range(2, 8):
    print("The value of i is currently", i)
print()
# The first argument determines the initial value of the control variable. 
# The last argument shows the first value the control variable will not be assigned. 
# note* range() only accepts integers as its arguments. 
# cuenta del 2 al 7

# More about the "for" loop and the range() function with 3 arguments. 
for i in range(2, 8, 3):
    print("The value of i is currently", i)
print()
# The third argument is an increment - it´s a value added to control the variable at every loop turn (the default value of the increment is 1) 
# The first argument tells us what the starting number of the sequence. The second number tells us when to stop the sequence. and the third number indicates the step (difference between each number)
# 2 + 3 = 5 + 3 = 8 ya no se incluye el 8 porque es hasta un numero antes. 

#If the range() function is empty, the loop wont execute its body at all. 
# ej:
for i in range(1, 1):
    print("The value of i is currently", i)
# note* the set generated by range has to be sorted in ASCENDING ORDER. 
# ej 2: 
for i in range(2, 1):
    print("The value of i is currently", i)

# Program whose task is to write some of the first powers of two: 
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 2
# The expo variable is used as a control variable for the loop, and indicates the current value of the exponent. 
# The exponentiation itself is replaced by multiplying by 2.

############ LAB - Essentials of the "for" loop - counting mississippily





