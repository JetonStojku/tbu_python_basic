## Lesson: Reading and Writing Text Files in Python

### Introduction:
JSON (JavaScript Object Notation) is a widely used data interchange format. In Python, the built-in json package facilitates working with JSON data. This lesson will cover the basics of reading and writing JSON files in Python, including serialization and deserialization.

### 1. Writing JSON to a File:
When working with JSON, we often need to serialize Python objects into JSON format and write them to a file.
Using **json.dumps()**:
The **json.dumps()** function is used to convert a Python dictionary to a JSON object.

```python
import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Serializing to JSON
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
```

**Using** **json.dump()**:
The **json.dump()** function directly writes the dictionary to a file in JSON format.
```python
import json

# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

# Writing to sample.json
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
```

### 2. Reading JSON from a File:
Deserialization involves converting a JSON object into Python objects.

**Using json.load()**:
The **json.load()** function reads JSON content from a file into a Python dictionary.
```python
import json

# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))
```

### 3. Serialization Mapping:

* **dict**: JSON object
* **list**, **tuple**: JSON array
* **str**: JSON string
* **int**, **float**: JSON numbers
* **True**: JSON true
* **False**: JSON false
* **None**: JSON null

### 4. Tips:
Use **json.dumps()** for serialization and **json.loads()** for deserialization when working with JSON strings.
Be mindful of file paths and ensure proper file closure using the **with** statement.
Consider specifying the file encoding, especially for non-ASCII characters.

### Conclusion:
Understanding how to read and write JSON in Python is essential for working with web APIs, configuration files, and data exchange. The json package provides convenient methods for serialization and deserialization, making it a powerful tool for handling JSON data in Python. Practice using these functions with different datasets to enhance your JSON handling skills.