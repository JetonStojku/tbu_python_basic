### Creating Lists
**Lists are collections of elements. Elements can be of different types.**
```python
my_list = [1, 2, 3]  # A list of integers
my_list = ['A string', 23, 100.232, 'o']  # A mixed-type list
```

```python
# Lesson 2: Accessing List Elements
my_list = ['one', 'two', 'three', 4, 5]

print(my_list[0])  # Access the first element: 'one'
print(my_list[1:])  # Access from the second element to the end: ['two', 'three', 4, '5']
print(my_list[:3])  # Access from the start to the fourth element: ['one', 'two', 'three']

# Additional Example: Accessing Elements by Index
print(my_list[3])  # Access the fourth element: 4
print(my_list[-1])  # Access the last element: 5

# Lesson 3: Modifying Lists
my_list = my_list + ['add new item permanently']  # Add a new item permanently to the list

# Additional Example: Removing an Item from the List
my_list.remove('two')  # Remove the element 'two' from the list
# Result: ['one', 'three', 4, 5, 'add new item permanently']

# Lesson 4: List Repetition (Optional)
# Lists can be repeated using the '*' operator.
repeated_list = my_list * 3
# Result: ['one', 'three', 4, 5, 'add new item permanently', 'one', 'three', 4, 5, 'add new item permanently', 'one', 'three', 4, 5, 'add new item permanently']
```

```python
# Lesson 5: List Methods (Append and Pop)
l = [1, 2, 3]

# Append: Add an element to the end of the list
l.append('append me!')
# Result: [1, 2, 3, 'append me!']

# Pop: Remove and return an element from the list by its index
popped_item = l.pop(0)  # Remove the element at index 0 ('1') and store it
# Result: '1'
# List after popping: [2, 3, 'append me!']

# Lesson 6: Accessing an Index Out of Range (Optional)
# Accessing an index that is out of range will result in an error.
# Example: l[100]  # Uncomment this line to see an index out of range error
```

```python
# Lesson 7: List Methods (Reverse and Sort)
new_list = ['a', 'e', 'x', 'b', 'c']

# Reverse: Reverse the order of elements in the list (permanently)
new_list.reverse()
# Result: ['c', 'b', 'x', 'e', 'a']

# Sort: Sort the list elements (ascending for numbers, alphabetical for strings)
new_list.sort()
# Result: ['a', 'b', 'c', 'e', 'x']
```

```python
# Lesson 8: Nested Lists (Matrix)
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

# Create a matrix by nesting lists
matrix = [lst_1, lst_2, lst_3]
# Result: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access the first item in the matrix
first_row = matrix[0]
# Result: [1, 2, 3]

# Access the first item of the first item in the matrix
first_element = matrix[0][0]
# Result: 1

# Lesson 9: List Comprehension
# Builds a list by deconstructing a for loop within square brackets []
first_col = [row[0] for row in matrix]
# Result: [1, 4, 7]
```