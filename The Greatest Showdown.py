#Task 1: Identify the Greatest

#Ask for user input
number1 = int(input("Please enter your first number: "))
number2 = int(input("Please enter your second number: "))
number3 = int(input("Please enter your third number: "))

#using conditional statements, check the user inputs for the largest number and print it
if number1 > number2 and number1 > number3:
    print("The largest number is: " + str(number1))
elif number2 > number1 and number2 > number3:
    print("The largest number is: " + str(number2))
else:
    print("The largest number is: " + str(number3))

#Task 2: Identify the smallest

#using conditional statements, check the user inputs for the smalest number and print it
if number1 < number2 and number1 < number3:
    print("The smallest number is: " + str(number1))
elif number2 < number1 and number2 < number3:
    print("The smallest number is: " + str(number2))
else:
    print("The smallest number is: " + str(number3))

#Task 3: Equality Check

#using conditional statements, check if any of the user inputs are equal to one another and print the outcome
if number1 == number2 and number1 == number3:
    print("All numbers are equal")

#checks for two equal inputs and determines if they are greater
elif number1 == number2 and number1 > number3:
    print("Two numbers are equal and the largest")
elif number2 == number3 and number2 > number1:
    print("Two numbers are equal and the largest")
elif number3 == number1 and number3 > number2:
    print("Two numbers are equal and the largest")

#checks for two equal inputs and determines if they are smaller
elif number1 == number2 and number1 < number3:
    print("Two numbers are equal and the smallest")
elif number2 == number3 and number2 < number1:
    print("Two numbers are equal and the smallest")
elif number3 == number1 and number3 < number2:
    print("Two numbers are equal and the smallest")

#if none of the inputs are equal to each other
else:
    print("No numbers are equal")