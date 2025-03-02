**Exercise 1: Enhancing the Txt Class**
- **Add a Method to Clear the File:**
  * Add a method named **clear_file** to the **Txt** class. 
  * The method should clear the contents of the 'data/readme.txt' file.
- **Modify undo_f Method:**
  * Modify the **undo_f** method to reset the **self.undo** attribute to an empty string after writing its value to the file.

- **Create a New Instance and Test:**
  * Create a new instance of the **Txt** class.
  * Use the **write** method to write a string to the file.
  * Use the **undo_f** method to undo the last write operation.
  * Check if the file's contents match the state before the last writing.

**Exercise 2**
* Build a class of type **Billionaire** that will store the following data: name, rank, year, gender, location, worth, citizenship.
* Build a class of type Location that will store the following data: country, region, billionaires (a list with objects of type **Billionaire**).
* Read the data from the **billionaires.json** file and create a list with objects of type **Billionaire**.
* Read the data from the **billionaires.json** file and create a list with objects of type **Location**.
* Find the country with the highest wealth from billionaires using the data obtained from the **billionaires.json** file.


**Exercise 4: Analyzing Airport Flight Data**

Consider the provided JSON file ("airlines.json") containing flight data for a specific airport.

- Load and Access Data:

  - Load the data from the "airlines.json" file into a Python script.
  - Access and print the airport code, name, and the time label from the loaded data.

- Statistics Analysis:
  - Calculate and print the total number of delayed flights for each delay type (Carrier, Late Aircraft, National Aviation System, Security, Weather).
  - Determine and print the carriers with the highest number of delays.
  - Calculate and print the percentage of delayed, canceled, and on-time flights.
- Flight Analysis:
  - Calculate and print the percentage of canceled, delayed, and on-time flights.
  - Identify and print the total number of flights for each status (Canceled, Delayed, Diverted, On Time).
  - Determine the month with the highest number of delayed flights.
- Minutes Delayed Analysis:
  - Calculate and print the total minutes delayed for each delay type.
  - Identify the delay type with the highest total minutes.
- Carrier Names Analysis:
  - Extract and print the names of carriers from the provided data.
  - Calculate and print the total number of carriers.
- Additional Analysis:
  - Identify and print the carrier with the highest total minutes of delay.
  - Determine and print the overall percentage of delayed minutes compared to the total minutes.
- Create Visualizations:
  - Using a visualization library (e.g., Matplotlib), create a bar chart to represent the number of delayed flights for each delay type.
- Data Modification:
  - Update the JSON data to include information about a new month and its corresponding flight statistics.
  - Save the modified data back to the "airlines.json" file.


**Exercise 4: Analyzing Car Specifications**

Consider the provided JSON file ("cars.json") containing information about cars.

- **Load and Access Data:**
   - Load the data from the "cars.json" file into a Python script.
   - Access and print the Make, Model Year, and Fuel Type of the car.

- **Dimensions Analysis:**
   - Calculate and print the total volume of the car by multiplying Height, Length, and Width.
   - Determine and print whether the car is classified as a compact, mid-size, or full-size based on the total volume.

- **Engine Information Analysis:**
   - Print the Engine Type and the number of forward gears.
   - Determine and print whether the car has a hybrid engine.
   - Calculate and print the power-to-weight ratio by dividing Horsepower by the total weight (you can assume weight is a constant value).

- **Fuel Information Analysis:**
   - Calculate and print the average fuel efficiency (average of City mpg and Highway mpg).
   - Determine and print whether the car is more fuel-efficient in the city or on the highway.

- **Identification Analysis:**
   - Print the Transmission type (Automatic or Manual) of the car.
   - Determine and print whether the car has an automatic or manual transmission.

- **Advanced Analysis:**
   - Implement a function that receives a fuel type as a parameter and returns a list of cars with that fuel type.
   - Implement a function that receives a classification as a parameter and returns the average Horsepower for cars in that classification.

- **Create Visualizations:**
   - Using a visualization library (e.g., Matplotlib), create a bar chart to represent the Horsepower and Torque of the car.

- **Data Modification:**
   - Update the JSON data to include information about a new car and its specifications.
   - Save the modified data back to the "cars.json" file.
