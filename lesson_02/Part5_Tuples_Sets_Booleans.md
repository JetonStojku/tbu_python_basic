### Lesson 1: Tuples
```python
# Tuples are ordered collections of elements that are immutable, meaning they cannot be changed after creation.
t = (1, 2, 3)  # A tuple with integer elements

# Length of a tuple
len(t)  # Result: 3

# Tuples can contain different types of elements
t = ('one', 2)  # A tuple with mixed data types
t[0]  # Access the first element: 'one'
t[-1]  # Access the last element: 2

# Lesson 2: Basic Tuple Methods
# Tuples support some basic methods.
t.index('one')  # Find the index of 'one' in the tuple
t.count('one')  # Count the number of times 'one' appears in the tuple

# Tuples are immutable; you cannot change their values.
# t[0] = 'change'  # Uncomment this line to see an error

# You also cannot add elements to a tuple.
# t.append('nope')  # Uncomment this line to see an error
```

### Sets are unordered collections of unique elements.
```python
# You can create a set using the set() function.
x = {1, 2, 3}  # Create a set with three unique elements

x = set()  # Create an empty set
x.add(1)  # Add an element (1) to the set
x  # Result: {1}

x.add(2)  # Add a different element (2) to the set
x  # Result: {1, 2}

# Try to add the same element (1) again
x.add(1)  # The set remains unchanged (no duplicates)
x  # Result: {1, 2}

# Additional Example: Removing Duplicates Using Sets
l = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
unique_values = set(l)  # Casting a list to a set removes duplicates
unique_values  # Result: {1, 2, 3, 4, 5, 6}
```

### Lesson 4: Booleans
```python
# Booleans represent two values: True and False.
a = True
a  # Result: True

# Booleans can also be the result of comparisons.
1 > 2  # Result: False
```

### None
```python
b = None  # None represents the absence of a value or a null value
b
```