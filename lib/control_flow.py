#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

   

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"  # Ensure exclamation mark is included
    elif temperature <= 55:
        return "It's a little chilly out there!"
    elif temperature >= 90:
        return "It's too dang hot out there!"
    elif temperature == 75:
        return "It's perfect out there!"
    else:
        return "Enjoy the weather!"




def fizzbuzz(num):
    # Divisibility check for Fizz, Buzz, and FizzBuzz
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    # Check for valid operations
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        print("Invalid operation!")
        return None
