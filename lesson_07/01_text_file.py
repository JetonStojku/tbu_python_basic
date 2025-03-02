"""
The following illustrates how to write a string to a text file:

Steps for writing to text files
To write to a text file in Python, you follow these steps:

First, open the text file for writing (or appending) using the open() function.
Second, write to the text file using the write() or writelines() method.
Third, close the file using the close() method.
The following shows the basic syntax of the open() function:
"""

# 1
with open(r'data/readme.txt', 'w') as f:
    f.write('readme')

# 2
lines = ['Readme', 'How to write text files in Python']
with open('data/readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

# 3
lines = ['Readme', 'How to write text files in Python']
with open('data/readme.txt', 'a') as f:
    f.writelines(lines)
# 4
lines = ['Readme', 'How to write text files in Python']
with open('data/readme.txt', 'w') as f:
    f.write('\n'.join(lines))

"""
The following shows how to read all texts from the readme.txt file into a string:

Steps for reading a text file in Python
To read a text file in Python, you follow these steps:

First, open a text file for reading by using the open() function.
Second, read text from the text file using the file read(), readline(), or readlines() method of the file object.
Third, close the file using the file close() method.
"""
# 5
with open('data/readme.txt') as f:
    lines = f.readlines()

# 6
with open('data/readme.txt') as f:
    contents = f.read()
    print(contents)
