## Lesson: Reading and Writing Text Files in Python

### Introduction:
Manipulating text files is a fundamental aspect of programming, especially in data science and application development. In this lesson, we will explore how to read and write text files in Python, covering various methods and tips for efficient file handling.

### 1. Writing to Text Files:
To write to text files, you follow these basic steps:
- Open the text file for writing or appending using the **open()** function.
- Write to the text file using the **write()** or **writelines()** method.
- Close the file using the **close()** method.

Here are a few examples:
```python
# Example 1: Write a single line to a file
with open(r'data/readme.txt', 'w') as f:
    f.write('readme')

# Example 2: Write multiple lines to a file using a list
lines = ['Readme', 'How to write text files in Python']
with open('data/readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# Example 3: Append lines to an existing file
lines = ['Additional line 1', 'Additional line 2']
with open('data/readme.txt', 'a') as f:
    f.writelines(lines)

# Example 4: Write lines to a file using join
lines = ['Line 1', 'Line 2', 'Line 3']
with open('data/readme.txt', 'w') as f:
    f.write('\n'.join(lines))
```

### 2. Reading Text Files:
To read text files, you follow these steps:
- Open the text file for reading using **open()**.
- Read text from the text file using the **read()**, **readline()**, or **readlines()** method of the file object. 
- Close the file using the **close()** method.

Here are some examples:
```python
# Example 5: Read all lines into a list
with open('data/readme.txt') as f:
    lines = f.readlines()

# Example 6: Read the entire file content into a string
with open('data/readme.txt') as f:
    contents = f.read()
    print(contents)
```

### 3. Additional Reading Methods:
In addition to the above methods, you can use the **seek()** method to change the file cursor position and the **tell()** method to get the current cursor position.
```python
# Example 7: Using seek() and tell()
with open('data/readme.txt') as f:
    print(f.read(5))  # Reads the first 5 characters
    print(f.tell())   # Returns the current cursor position
    f.seek(0)         # Moves the cursor to the beginning
```

### 4. Tips for File Handling:
Use the **with** statement to ensure proper file closure.
Be mindful of file paths and use raw strings (**r''**) for Windows paths.
Consider specifying the file encoding, especially with non-ASCII characters.

### Conclusion:
Reading and writing text files are essential skills in Python. By understanding the open() function and different reading and writing methods, you gain flexibility and efficiency when working with files. Practice these concepts with various file structures to enhance your Python file handling proficiency.
