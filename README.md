
# AirBnB clone - The console

# Description of the project

This project aims to create a fundamental replica of the Airbnb website, focusing on building the core backend infrastructure that powers the application. In this initial phase, we are developing a command-line interface (CLI) or console as the backend interface for managing various application data aspects.
Shell or terminal, this console allows users to interact with the system through text-based commands. It is designed to handle essential operations such as creating, reading, updating, and deleting instances of various objects, including users, places, amenities, and reviews.
Moreover, the console includes functionality for persisting data across sessions through file storage. This means that all created objects can be saved to a file and reloaded later, ensuring that the application's state is maintained even after the program exits. This console serves as the foundation upon which more complex features and interfaces, such as the web front-end and database integration, will be built in later phases of the project.
In all, this project shows the groundwork for a fully functional web application by providing a robust backend system capable of managing the core data and operations that will be essential to the eventual Airbnb clone.


# The console - tasks
-  Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of  future instances <br>
-  Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
-  Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
-  Create the first abstracted storage engine of the project: File storage.
-  Create all unittests to validate all our classes and storage engine


# Description of the command interpreter

The command interpreter helps us to manage the objects of our project by:

- Creating a new object (ex: a new User or a new Place)
- Retrieving an object from a file, a database etc…
- Doing operations on objects (count, compute stats, etc…)
- Updating attributes of an object
- Destroying an object

## How to start the interpreter

```bash
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  delete  destroy  exit  help  q  quit  show  update

(hbnb) 
(hbnb) 
(hbnb) quit

```

## How to use the interpreter

## Tests
To run all the tests execute the following command:

```bash
$ python3 -m unittest discover tests
```
You can also run a single test by specifying the test file:

```bash
$ python3 -m unittest tests/test_models/test_city.py

```


# Authors

## [`Nmesoma Solomon Peter`]
## [`Mariam Issah`]
## [`Nicole Ange Mukundwa`]

