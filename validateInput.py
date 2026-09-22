```python
# Continuously ask the user for their age until a valid number is entered
while True:
    # Prompt the user to enter their age
    print('Enter your age:')
    # Get the user's input
    age = input()
    # Check if the entered value is a decimal number (i.e., not a float)
    if age.isdecimal():
        # If it's a valid number, exit the loop
        break
    # If it's not a valid number, print an error message and continue to the next iteration
    print('Please enter a number for your age.')

# Continuously ask the user for a new password until a valid one is entered
while True:
    # Prompt the user to select a new password
    print('Select a new password (letters and numbers only):')
    # Get the user's input
    password = input()
    # Check if the entered password contains only alphanumeric characters (letters and numbers)
    if password.isalnum():
        # If it's a valid password, exit the loop
        break
    # If it's not a valid password, print an error message and continue to the next iteration
    print('Passwords can only have letters and numbers.')
```