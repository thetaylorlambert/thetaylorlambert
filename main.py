# Taylor Lambert
# This project is going to be about what I've learned this semester.
print("Welcome to my project! \nIn this project I am going to show you what I've learned in my COP1500 class.")
print("First I am going to do addition and input 3+4 with and without quotation marks.")
print("With:", "3+4")
print("Without:", 3+4)
print("The quotation marks make it a string and prints exactly what I wrote, while without them, it actually does the math.")
print("Now we can also pick our own numbers and the computer will calculate it for us.")
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
answer = num1 + num2
print("The answer is ", answer)
print("We can also do this with subtraction.")
print("With quotation marks:", "10-6")
print("No quotatoin marks:", 10-6)
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
answer = num1 - num2
print("The answer is ", answer)
print("Multiplication: ")
print("With quotation marks: ", "5 * 6")
print("No quotation marks:", 5 * 6)
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
answer = num1 * num2
print("The answer is ", answer)
print("Division: ")
print("With quotation marks: ", "10 / 3")
print("No quotation marks:", 10 / 3)
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
answer = num1 / num2
print("The answer is ", answer)
print("Exponent: ")
print("With quotation marks: ", "3 ** 2")
print("No quotation marks:", 3 ** 2)
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
answer = num1 ** num2
print("The answer is ", answer)
print("Floor division: ")
print("With quotation marks: ", "20 // 3")
print("No quotation marks:", 20 // 3)
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
answer = num1 // num2
print("The answer is ", answer)
print("Remainder: ")
print("With quotation marks: ", "20 % 3")
print("No quotation marks:", 20 % 3)
first_number = input("Enter first number: ")
second_number = input("Enter second number: ")
num1 = int(firstNumber)
num2 = int(secondNumber)
answer = num1 % num2
print("The answer is ", answer)
print("Now that I've shown you all of the numeric operators, ", end = '')
print("here are the string operators.")
print("Using addition: you can put two seperate string together.")
print("Hello! " + "How are you?")
print("You can also put together strings and variables.")
name1 = input("Enter a name: ")
verb1 = input ("Enter a past-tense verb: ")
name2 = input("Enter another name: ")
noun = input("Enter a noun: ")
emotion = input("Enter an emotion: ")
verb2 = input("Enter another past tense verb: ")
place = input("Enter a place: ")
print(name1 + " " + verb1 + " " + name2 + "'s " + noun + " so " + name2 + " got " + emotion + " and " + verb2 + " to " + place + ".")
print("Using multiplication: you can print a string or variable or both multiple times.")
print("Example:")
word = input("Enter a word: ")
print(word * 100)
print("This project's due date: ", end = '')
print('09','18','2021', sep='-')
#sources: stackoverflow.com, course website, geeksforgeeks.org
