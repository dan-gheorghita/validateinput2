# validateInput.py

**Program Description**

This Python script is designed to continuously prompt users to input their age and a new password until a valid input is provided. A valid input for age is a decimal number (0-9), while a valid password is a string containing only alphanumeric characters (letters and numbers).

**Breakdown of the Script**

The script consists of two main loops, each responsible for collecting a specific type of user input.

### Age Input Loop

1. The loop starts with a `while True` statement, indicating that it will continue to execute indefinitely until a valid condition is met (i.e., a valid age is entered).
2. The user is prompted to enter their age with the message "Enter your age:".
3. The user's input is stored in the `age` variable using the `input()` function.
4. The script checks if the entered value is a decimal number using the `isdecimal()` method. If it is, the loop exits using the `break` statement