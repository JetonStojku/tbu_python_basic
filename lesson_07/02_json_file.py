"""
Reading and Writing JSON to a File in Python
The full-form of JSON is JavaScript Object Notation. It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. Python supports JSON through a built-in package called json. To use this feature, we import the json package in Python script. The text in JSON is done through quoted string which contains the value in key-value mapping within { }. It is similar to the dictionary in Python.

Writing JSON to a file in python
Serializing JSON refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network. To handle the data flow in a file, the JSON library in Python uses dump() or dumps() function to convert the Python objects into their respective JSON object, so it makes easy to write data to files. See the following table given below.

PYTHON OBJECT	    JSON OBJECT
dict	            object
list, tuple	        array
str	                string
int, long, float	numbers
True	            true
False	            false
None	            null

Using json.dumps()

The JSON package in python has a function called json.dumps() that helps in converting a dictionary to a JSON object.

It takes two parameters:

dictionary – name of dictionary which should be converted to JSON object.
1. indent – defines the number of units for indentation
2. After converting dictionary to a JSON object, simply write it to a file using the “write” function.
"""

# 1
# Python program to write JSON
# to a file


import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

"""
Using json.dump()

Another way of writing JSON to a file is by using json.dump() method

The JSON package has the “dump” function which directly writes the dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object.

It takes 2 parameters:

1. dictionary – name of dictionary which should be converted to JSON object.
2. file pointer – pointer of the file opened in write or append mode.
"""

# 2
# Python program to write JSON
# to a file


import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)

"""
Reading JSON from a file using python
Deserialization is the opposite of Serialization, i.e. conversion of JSON object into their respective Python objects. The load() method is used for it. If you have used JSON data from another program or obtained as a string format of JSON, then it can easily be deserialized with load(), which is usually used to load from string, otherwise, the root object is in list or dict.

Using json.load()

The JSON package has json.load() function that loads the json content from a json file into a dictionary.

It takes one parameter:

File pointer: A file pointer that points to a JSON file.
"""

# Python program to read JSON
# from a file


import json

# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))
