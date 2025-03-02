"COPY AND DEEP COPY"
"""Lesson: Copy and Deepcopy in Python

Introduction:
In Python, when working with mutable objects like lists, dictionaries, or user-defined classes, understanding the concepts of copying and deep copying is crucial. Copying allows you to create duplicates of objects, but the behavior varies based on whether you perform a shallow copy or a deep copy. This lesson will cover the basics of copying and deep copying in Python.

1. Shallow Copy:
A shallow copy creates a new object but does not create copies of nested objects. Instead, it copies references to the original nested objects. The `copy` module in Python provides the `copy()` method for creating shallow copies.
"""

import copy

original_list = [1, 2, [3, 4]]

shallow_copied_list = copy.copy(original_list)

# Modify the nested list in the shallow copy
shallow_copied_list[2][0] = 99

# Changes will be reflected in the original list as well
print(original_list)  # Output: [1, 2, [99, 4]]

"""2. Deep Copy:
A deep copy creates a new object and recursively creates copies of all nested objects. The `copy` module also provides the `deepcopy()` method for deep copying."""

import copy

original_list = [1, 2, [3, 4]]

deep_copied_list = copy.deepcopy(original_list)

# Modify the nested list in the deep copy
deep_copied_list[2][0] = 99

# Changes won't affect the original list
print(original_list)  # Output: [1, 2, [3, 4]]


"""3. When to Use Copy and Deepcopy:
- Use shallow copy when you want a new object with copies of the top-level elements, but shared references to nested objects.
- Use deep copy when you want a completely independent copy of the original object, including all nested objects.

4. Performance Considerations:
- Shallow copy is generally faster than deep copy since it doesn't need to recursively copy all nested objects.
- Deep copy may be slower but ensures complete independence of the copied object.

Conclusion:
Understanding the differences between shallow copy and deep copy is essential for avoiding unexpected behavior when working with mutable objects in Python. Choose the appropriate method based on the desired level of independence between the original and copied objects.
"""