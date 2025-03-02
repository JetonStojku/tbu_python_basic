**Exercise 1: Abstract Class**
Create an abstract class called `Shape` with an abstract method `area()`. Create two subclasses, `Circle` and `Rectangle`, that inherit from the `Shape` class. Implement the `area()` method in each subclass.

**Exercise 2: Polymorphic Function**
Write a function `calculate_area(shape)` that takes an object of type `Shape` and calculates its area using the `area()` method. Test the function with instances of both `Circle` and `Rectangle`.

**Exercise 3: Abstract Method Implementation**
Create an abstract class `Animal` with an abstract method `make_sound()`. Implement two subclasses, `Dog` and `Cat`, and provide different implementations for the `make_sound()` method in each.

**Exercise 4: Polymorphic List**
Create a list of `Animal` objects containing instances of both `Dog` and `Cat`. Iterate through the list and call the `make_sound()` method for each object.

**Exercise 5: Abstract Class Inheritance**
Create an abstract class `Vehicle` with abstract methods `start()` and `stop()`. Implement two subclasses, `Car` and `Motorcycle`, inheriting from `Vehicle`. Provide implementations for the abstract methods.

**Exercise 6: Polymorphic Function with Vehicles**
Write a function `operate_vehicle(vehicle)` that takes an object of type `Vehicle` and calls its `start()` and `stop()` methods. Test the function with instances of both `Car` and `Motorcycle`.

**Exercise 7: Abstract Property**
Extend the `Shape` class from Exercise 1 by adding an abstract property `name`. Each subclass (`Circle` and `Rectangle`) should provide a unique name for the shape.

**Exercise 8: Polymorphic Property Access**
Write a function `get_shape_name(shape)` that takes an object of type `Shape` and prints its name using the `name` property. Test the function with instances of both `Circle` and `Rectangle`.

**Exercise 9: Multiple Inheritance**
Create a class `FlyingObject` with an abstract method `fly()`. Modify the `Bird` class from Exercise 3 to inherit from both `Animal` and `FlyingObject`. Provide an implementation for the `fly()` method in the `Bird` class.

**Exercise 10: Using isinstance()**
Write a function `print_type(obj)` that takes an object and prints its type. Use `isinstance()` to check if the object is an instance of the `Shape`, `Animal`, or `Vehicle` classes and print the corresponding information.