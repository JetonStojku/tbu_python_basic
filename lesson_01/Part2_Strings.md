### String Literals
```python
# Single-quoted string
print('hello')

# Single-quoted string
print('This is also a string')

# Double-quoted string
print("String built with double quotes")

# Escaping Single Quotes
# The backslash (\) is used to escape a single quote within single quotes.
# This line will create an error if executed.
print(' I\'m using single quotes, but will create an error')

# Using Double Quotes Inside a String, 
# You can use double quotes within a single-quoted string, and vice versa.
print("Now I'm ready to use the single quotes inside a string!")

# Using Escape Sequences and Printing New Lines
print('Hello World 1')  # Print a string
print('Hello World 2')  # Print another string
print('Use \\n to print a new line')  # Use an escape sequence to print a new line
print('\n')  # Print an empty line
print('See what I mean?')  # Print another string
```

```python
# String Length
# The len() function calculates the length of a string.
print(len('Hello World'))
```

### String Slicing
```python
# String Variables
s = 'Hello World'  # Assign the string 'Hello World' to the variable 's'
print(s)  # Print the value of 's'
# String Indexing and Slicing
print(s[0])  # Print the first character ('H') of the string 's'
print(s[1])  # Print the second character ('e') of the string 's'
print(s[2])  # Print the third character ('l') of the string 's'
print(s[1:])  # Print the string from the second character ('e') to the end

# More String Slicing
print(s[:3])  # Print the string from the start to the fourth character ('Hel')
print(s[:])   # Print the entire string ('Hello World')
print(s[-1])  # Print the last character ('d')
print(s[:-1])  # Print the string from the start to the last character ('Hello Worl')

# String Slicing with Steps
print(s[::1])  # Print the entire string with a step of 1 (no change)
print(s[::2])  # Print the string with a step of 2 (skip every other character)
print(s[1:5:-1])  # Print the string in reverse order
# Concatenating Strings
# This line will create an error since strings are immutable (cannot be modified).
# You can't change the character at position 0 to 'x'.
# s[0] = 'x'
print(s)

# Concatenating Strings
s = s + ' concatenate me!'  # Concatenate 's' with ' concatenate me!'
print(s)  # Print the updated string

# String Repetition
letter = 'z'  # Create a string with the letter 'z'
print(letter * 10)  # Print 'z' repeated 10 times

# String Methods
# Converting the string to uppercase
print(s.upper())

# Converting the string to lowercase
print(s.lower())

# Splitting the string into words (using the default space delimiter)
print(s.split())

# Splitting the string at 'W'
print(s.split('W'))
```

### String Formatting
```python
# Using curly braces to insert another string
formatted_string = 'Insert another string with curly brackets: {}'.format('The inserted string')
print(formatted_string)

# Using string formatting to insert a value
formatted_string = 'This is a string with an {p}'.format(p='insert')
print(formatted_string)

# Using string formatting with multiple values
formatted_string = 'One: {p}, Two: {p}, Three: {p}'.format(p='Hi!')
print(formatted_string)

# Using string formatting with named placeholders and a dictionary
formatted_string = 'Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1, b='two', c=12.3)
print(formatted_string)
```