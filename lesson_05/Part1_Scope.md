### Nested Statements and Scope
```python
x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())
print(x)
```

### Quick examples of LEGB
Enclosing function locals
This occurs when we have a function inside a function (nested functions)
```python
name = 'This is a global name'

def greet():
    # Enclosing function
    name = 'Sammy'

    def hello():
        print('Hello '+name)

    hello()

greet()
print(name)
```

```python
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)
```

### The Global Statement
```python
x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)
```
