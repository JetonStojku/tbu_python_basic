**Exercise 1: Shopping List (Lists)**

```python
# Create a shopping list
shopping_list = ['apples', 'bread', 'milk', 'eggs', 'cereal']
```

**Exercise 2: User Information (Dictionaries)**

```python
# Create a user information dictionary
user_info = {
    'username': 'john_doe',
    'email': 'john@example.com',
    'age': 30
}
```

**Exercise 3: Days of the Week (Tuples)**

```python
# Create a tuple of days of the week
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# Attempting to modify the tuple will result in an error, as tuples are immutable.
# Example:
# days_of_week[0] = 'NewDay'  # This will raise a TypeError
```

**Exercise 4: Unique Numbers (Sets)**

```python
# Create a set of unique numbers
unique_numbers = {1, 2, 3, 4, 5}
```

**Exercise 5: Boolean Logic (Booleans)**

```python
# Create boolean variables
is_student = True
is_teacher = False

# Use the variables to answer questions
print("Is the person a student?", is_student)
print("Is the person a teacher?", is_teacher)
```

**Exercise 6: Grocery List (Lists and Dictionaries)**

```python
# Create a grocery list
grocery_items = [
    {'name': 'apples', 'quantity': 5, 'price': 1.99},
    {'name': 'milk', 'quantity': 2, 'price': 2.49},
    {'name': 'bread', 'quantity': 1, 'price': 2.99},
    # Add more grocery items as needed
]
```

**Exercise 7: Weather Forecast (Dictionaries and Nested Data)**

```python
# Create a weather forecast dictionary
weather_forecast = {
    'current_weather': {
        'temperature': 72,
        'conditions': 'Sunny',
        'wind_speed': 5
    },
    'next_days': {
        'day1': {
            'temperature': 75,
            'conditions': 'Partly Cloudy',
            'wind_speed': 8
        },
        'day2': {
            'temperature': 68,
            'conditions': 'Rainy',
            'wind_speed': 10
        }
    }
}
```

**Exercise 8: Favorite Colors (Sets)**

```python
# Create two sets of favorite colors
set1 = {'red', 'blue', 'green'}
set2 = {'blue', 'yellow', 'green'}

# Find the intersection of the two sets (shared favorites)
shared_favorites = set1.intersection(set2)
```

**Exercise 9: User Preferences (Dictionaries)**

```python
# Create a user preferences dictionary
user_preferences = {
    'theme_color': 'dark',
    'notifications': True,
    'font_size': 'medium'
}

# Modify user preferences
user_preferences['notifications'] = False  # Turn off notifications
user_preferences['theme_color'] = 'light'  # Change theme color
```

**Exercise 10: User Status (Booleans)**

```python
# Simulate user online status
is_online = False  # User is offline

# When the user logs in or out, update the boolean accordingly
is_online = True  # User logs in
# User is online
is_online = False  # User logs out
# User is offline
```