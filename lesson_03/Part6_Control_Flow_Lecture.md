### COMPARISON OPERATORS
```python
# Greater than
1 > 2   # False
# Less than
1 < 2   # True
# Greater than or Equal to
1 >= 1  # True
# Less than or Equal to
4 < 4  # False
# Equality
1 == 1  # True
1 == "1"    # False
'hi' == 'bye'   # False
# Inequality
1 != 2  # True
'hi' != 'bye'   # True
```

### LOGICAL OPERATORS
**AND**
```python
(1 > 2) and (2 < 3)  # True
```

```
and T   F
T   T   F
F   F   F

or  T   F
T   T   T
F   T   F
```


**OR**
```python
(1 > 2) or (2 < 3)  # True
```

**Multiple logical operators**
```python
(1 == 2) or (2 == 3) or (4 == 4)  # True
```

### if,elif, else Statements

**Now let's show some examples of if, elif, and else statements:**
```python
if 1 < 2:
    a = 0
    b = 1
    c = 2


if 1 < 2:
    print('Yep!')

if 1 < 2:
    print('yep!')
```

**If Else - Make sure to line up the else with the if statement to "connect" them**
```python
if 1 < 2:
    print('first')
else:
    print('last')

if 1 > 2:
    print('first')
else:
    print('last')
```


**To add more conditions (like else if) you just use a single phrase "elif"**
```python
if 1 == 2:
    print('first')
elif 3 == 3:
    print('middle')
else:
    print('Last')
```

### FOR LOOPS

```python
# Perform an action with each element
seq = [1, 2, 3, 4, 5]

for item in seq:
    print(item)

# Perform an action for every element but doesn't actually involve the elements
for item in seq:
    print('Yep')

# You can call the loop variable whatever you want:
for jelly in seq:
    print(jelly+jelly)
```

**For Loop with a Dictionary**
```python
ages = {"Sam": 3, "Frank": 4, "Dan": 29}

for key in ages:
    print("This is the key")
    print(key)
    print("This is the value")
    print(ages[key])
    print("\n")
```

**A list of tuple pairs is a very common format for functions to return data in Because it is so common we can use tuple un-packing to deal with this, example:**
```python
mypairs = [(1, 10), (3, 30), (5, 50)]

# Normal
for tup in mypairs:
    print(tup)

# Tuple un-packing
for item1, item2 in mypairs:
    print(item1)
    print(item2)
```

### WHILE LOOPS
**While loops allow us to continually perform and action until a condition becomes true. For example:**
```python
i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1
```

### RANGE FUNCTION
**range() can quickly generate integers for you, based on a starting and ending point Note that its a generator:**
```python
range(5)

a = list(range(5))

for i in range(5):
    print(i)

# Start and ending
range(1, 10)

# Third argument for step-size
range(0, 10, 2)
```

**Starting with:**
```python
x = [1, 2, 3, 4]

# We could do this:
out = []
for item in x:
    out.append(item**2)
print(out)

# Written in List Comprehension Form
[item**2 for item in x]

# Traditional way to create a dictionary
square_dict = {}
for num in range(1, 6):
    square_dict[num] = num ** 2

# Using dictionary comprehension
square_dict_comp = {num: num**2 for num in range(1, 6)}

# Display the dictionaries
print("Traditional Dictionary:", square_dict)
print("Dictionary Comprehension:", square_dict_comp)
```