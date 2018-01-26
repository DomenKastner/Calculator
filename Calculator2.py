# -*- coding: utf-8 -*-

while True:

    x = int(raw_input("vpisi število x:"))
    print "-----------"
    y = int(raw_input("vpisi število y:"))
    znak = raw_input("Izberi eno od naslednjih operacij:\n --------- \n Odštevanje - \n Seštevanje + \n Množenje * \n"
                     " Deljenje / \n Potenciranje ** \n Razlika % \n ------- \n ")

    if znak == "+":  # + Addition
        print"vsota je:", x + y
        print"........."
    elif znak == "-":  # - Subtraction
        print"razlika je:", x - y
        print"........."
    elif znak == "*":  # * Multiplication
        print"produkt je:", x * y
        print"........."
    elif znak == "/":  # / Division
        print"kvocient je:", x / y
        print"........."
    elif znak == "**":  # ** Exponent
        print"potenca je:", x ** y
        print"........."
    elif znak == "%":  # % Modulus (Ostanek pri deljenju)
        print"ostanek je:", x % y
        print"........."
    else:
        print("Ne poznam te operacije")
        print "----------"

    ponovi = raw_input("Želiš ponovno računati? y/n")
    if ponovi == "n":
        break
