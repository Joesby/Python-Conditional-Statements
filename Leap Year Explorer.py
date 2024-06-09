#Task 1: Leap Year Checker

#Ask for user to input a year and store it as an integer variable
year = int(input("Please enter a year: "))

#using confitional statements, check if the year meets requirements to be a leap year and print the result
#years that are divisible by 400 are leap years
if year % 400 == 0:
    print("True")
#years that are divisible by 4 but are also divisible by 100 are not leap years
elif year % 100 == 0 and year % 4 == 0:
    print("False")
#years that are divisible by 4 and not 100 are leap years
elif year % 100 != 0 and year % 4 ==0:
    print("True")
#all other years are not leap years
else:
    print("False")