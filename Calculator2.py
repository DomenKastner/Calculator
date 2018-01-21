# -*- coding: utf-8 -*-

x = int(raw_input("vpisi število x:"))
y = int(raw_input("vpisi število y:"))
znak = raw_input("vnesi operacijo:")

if znak == "+": # + Addition
    print"vsota je:", x + y
elif znak == "-": # - Subtraction
    print"razlika je:", x - y
elif znak == "*": # * Multiplication
    print"produkt je:", x * y
elif znak == "/": # / Division
    print"kvocient je:", x / y
elif znak == "**": # ** Exponent
    print"potenca je:", x ** y
elif znak == "%": # % Modulus
    print"ostanek je:", x % y
else:
    print("TYPO...ne poznam te operacije")




#print"vpisal si",x
#print"vpisal si",y
#print"vsota je:",x+y
#print"razlika je:", x-y
#print str(x)+ ".po vrsti."

