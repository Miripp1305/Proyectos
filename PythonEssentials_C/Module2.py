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

#Notas del capitulo 
#Literals are notations for fixed values in code. Ej. a literal can be a number(123) or a string ("im a literal")
#The binary system is a base-2 numeral system that uses only two symbols: 0 and 1.
#The octal system is a base-8 numeral system that uses the digits 0 to 7.
#The hexadecimal system is a base-16 numeral system that uses the digits 0 to 9 and the letters A to F.
#Integers (Ints) Are numerical types . ej (256) o (-1)
#Floating point numbers (Floats) Are  numerical types. ej (3.14) o (-0.5)
#Boolean values (Booleans) Are logical types. ej (True) o (False)
#The None literal. Used to represent the absence of a value or a null value.

