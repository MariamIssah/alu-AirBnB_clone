
# AirBnB clone - The console

# Description of the project

This project is a basic replica of the Airbnb website. The initial phase focuses on developing a backend interface or console for managing application data, similar to a shell. Through console commands, users can create, update, delete objects, and handle file storage. 

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

