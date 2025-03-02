# Lesson 1: Creating Dictionaries
# Dictionaries are collections of key-value pairs enclosed in curly braces.
my_dict = {
    'key1': 'value1',
    'key2': 'value2'
}

# Access values by their keys
print(my_dict['key2'])  # Access the value associated with 'key2'

# Additional Example: Creating a Dictionary with Various Data Types
my_dict = {
    'key1': 123,
    'key2': [12, 23, 33],
    'key3': ['item0', 'item1', 'item2'],
    'key4': {
        'k1': 5.2,
        'k2': '5'
    }
}

# Access values and nested values in the dictionary
my_dict['key3']  # Access the value associated with 'key3' (a list)
my_dict['key3'][0]  # Access the first item in the list associated with 'key3'

# Lesson 2: Modifying Dictionary Values
# You can modify dictionary values by accessing them through their keys.
my_dict['key3'][0] = my_dict['key3'][0].upper()  # Convert the string to uppercase

# Additional Example: Modifying Values and Reassignment
my_dict['key1']  # Access the value associated with 'key1'
my_dict['key1'] = my_dict['key1'] - 123  # Subtract 123 from the value associated with 'key1'
my_dict['key1']  # Access the updated value

# You can also use shorthand for modifying values.
my_dict['key1'] -= 123  # Subtract 123 from the value and update it
my_dict['key1']  # Access the updated value

# Lesson 3: Creating a Dictionary and Adding Key-Value Pairs
# Create an empty dictionary and add key-value pairs through assignment.
d = {}
d['animal'] = 'Dog'  # Add 'animal' as a key with the value 'Dog'
d['answer'] = 42  # Add 'answer' as a key with the value 42

# Additional Example: Show the Dictionary
d  # Result: {'animal': 'Dog', 'answer': 42}

# Lesson 4: Nested Dictionaries
# Dictionaries can be nested inside other dictionaries.
d = {
    'key1': {
        'nestkey': {
            'subnestkey': 'value'
        }
    }
}

# Access nested dictionary values by chaining keys.
d['key1']['nestkey']['subnestkey']

# Lesson 5: Dictionary Methods
d = {'key1': 1, 'key2': 2, 'key3': 3}

# Method to return a list of all keys
d.keys()

# Method to return a list of all values
d.values()

# Method to return a list of tuples containing key-value pairs
d.items()
