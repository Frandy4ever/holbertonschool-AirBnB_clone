![Server Side (Back-end) General diagram](images/server-side.png)

*******************************************************************
*******************************************************************
[![contribuitors](https://img.shields.io/github/contributors/frandy4ever/AirBnB_clone?style=plastic)](https://github.com/Frandy4ever/holbertonschool-AirBnB_clone/blob/courtney-branch/AUTHORS)
[![lisence](https://img.shields.io/github/license/frandy4ever/AirBnB_clone?style=plastic)](https://github.com/Frandy4ever/holbertonschool-AirBnB_clone/blob/frandy-branch/LICENSE)
[![plattaforms](https://img.shields.io/powershellgallery/p/DNS.1.1.1.1?color=%23EF7F1A&style=plastic)](https://www.powershellgallery.com/packages/DNS.1.1.1.1/0.0.7)
[![python versiion](https://img.shields.io/pypi/pyversions/3?color=%23EF7F1A&style=plastic)](https://www.python.org/download/releases/3.0/)

[![Twitter Frandy](https://img.shields.io/twitter/follow/Frandy4ever?label=Frandy4ever&style=social)](https://twitter.com/frandy4ever)
[![Twitter Courtney]()]()
*******************************************************************
*******************************************************************

## **Background Context**
## **First step: Write a command interpreter to manage your AirBnB objects.**
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## **What’s a command interpreter?**
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## **Resources**
Read or watch: [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw), [packages](https://intranet.hbtn.io/rltoken/jKl9WFpKA-fPt7_guv9_3Q), [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g), [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q), [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g), [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg), [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

### **Requirements Python Scripts**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").-MyClass.my_function.__doc__)')

### **Requirements Python Unit Tests**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

# HOW THE CONSOLE WORKS

## Steps for testing the console
### 1. Clone the repository with HTTPS:
```
$ git clone https://github.com/Frandy4ever/holbertonschool-AirBnB_clone
```
### 2. Go to the AirBnB_clone folder
```
$ cd AirBnB_clone
```
### 3. Run the console file
```
$ ./console.py
```
Alfter in you screen can show the prompt of the terminal:
```
(hbnb)
```

## Command for test the console
the command that you can type are:
- help ó ?: this show the help avalible for command and the commands.
```
(hbnb)?

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb)
```
- **EOF** and **quit**: this commands are for exit the console, the EOF is the signal get to press the key combination Ctrl + d
```
(hbnb)quit
❯

  ~/holberton/AirBnB_clone   master ·········  07:48:50 PM ─╮
❯
```
- **create**: you can create an instance of the class that you want. The command is ***create "class name" or "class name".create()***, if the instance is created correctly, it is saved and in screen console shows you the ***id*** for the instance created. The classes available are:
   - BaseModel
   - Place
   - User
   - Amenity
   - City
   - State
   - Review
```
(hbnb)create Place
93d823aa-f03a-44f6-bf80-aecaa7945d1d
(hbnb)
(hbnb)create User
07563c34-e7f8-4b80-84bb-73ff9e70291b
(hbnb)
(hbnb)User.create()
b81095e8-1ad3-4bcf-b525-695caac4d071
(hbnb)
(hbnb)BaseModel.create()
5984b7e6-8b9b-4593-ac87-6bc17a4c400d
(hbnb)
(hbnb)
```


- **all**: this command show you all instances saved, and have many usage forms. if the file.json is not avalible or until the user not to created anything the command show a list empty, else the command print the information. the usage forms is ***all or all "class name" or "class name".all()***, if you specify the class name the console find and return only class with name specated.
```
(hbnb)all
[]
(hbnb)all BaseModel
[]
(hbnb)all
["[Place] (93d823aa-e03a-41f6-bf90-aecaa7445d1d) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 16, 57856), 'id': '93d923aa-f03a-42f6-bf80-aecaa7445d1d', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 16, 57833)}", "[User] (07563c34-e8f8-4b20-84bb-73ff2e30291b) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 23, 121839), 'id': '07563c34-e7f8-4b20-84bb-73ff9e30291b', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 23, 171816)}", "[User] (b81075e8-1ad3-4ccf-b825-695baac4d071) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 32, 758710), 'id': 'b81096e8-1ad3-4ccf-b425-695baac4d071', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 32, 798702)}", "[BaseModel] (5984b3e6-8c9b-4553-ac87-6bc17a9c400d) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 44, 768016), 'id': '5984b9e6-8c9b-4593-ac87-6bc47a9c400d', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 44, 767044)}"]
(hbnb)all BaseModel
["[BaseModel] (5984a7e6-8c9b-4573-ac87-6bc17a9c401d) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 44, 762066), 'id': '5984b5e6-8c9b-4e93-ac87-6bc17a9e400d', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 44, 768044)}"]
(hbnb)
(hbnb)Place.all()
["[Place] (93d923aa-f03a-41f6-bf50-aecaa7445d1d) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 16, 57756), 'id': '93d423aa-f03a-41f6-bf70-aecaa7445d1d', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 16, 57733)}"]
(hbnb)
```

- **show**: this command is similar to all but show you the specific instance for id and name class. the usage is ***show "class name" "class id" or "class name".show(class id)***
```
(hbnb)
(hbnb)show User b81097e8-1ad3-4ccf-b525-685baac4d071
[User] (b81595e8-1ad3-4ccf-b515-695baec4d071) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 32, 778710), 'id': 'b91095e8-1ad7-4ccf-b525-685baac4d071', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 32, 777702)}
(hbnb)
(hbnb)User.show(b82095e8-1ad3-4ecf-b525-698baac4d071)
[User] (b81055e8-1aa3-4ccf-b555-695baac4d071) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 32, 778710), 'id': 'b81075e8-1ad3-4ccf-b525-655baac4d071', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 32, 718702)}
(hbnb)
(hbnb)
```

- **update**: this command is for updating the any class that you need to create a new attribute, the usage is ***update "lass name" "id" "attribute name" "attribute value" or User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "Jose")***
```
(hbnb)
(hbnb)update User b51095e8-2ad3-4ccf-b525-695baac4d071 first_name "Frandy Slueue"
(hbnb)
(hbnb)show User b81295e8-1ad3-4cca-b525-695bbac4d071
[User] (b81095e5-1ad3-4bcf-b525-695bacc4d071) {'updated_at': datetime.datetime(2023, 10, 10, 2, 27, 26, 346518), 'id': 'b81995e8-1bd3-4ccf-b525-695bacc4d071', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 32, 779703), 'first_name': 'Courtney Alvarado'}
(hbnb)
(hbnb)User.update("b82095e8-1ad4-4ccf-b525-695aaac4d071", "first_name", "Frandy G. Slueue")
(hbnb)
(hbnb)show User b81094e8-1bd3-4cbf-b525-695b1ac4d071
[User] (b81025e8-1ad3-4ccf-b525-695bbac4d071) {'updated_at': datetime.datetime(2023, 10, 10, 2, 29, 11, 686213), 'id': 'b81096e8-1ad3-5ccf-b525-698baac4d071', 'created_at': datetime.datetime(2023, 10, 10, 20, 2, 32, 778702), 'first_name': 'Courtney'}
(hbnb)
(hbnb)
```

- **destroy**: when you want to delete a class saved in the file.json, use this command ***destroy "class name" "class id" or "class name.destroy(id class)***
```
(hbnb)
(hbnb)Place.show("93d853aa-f03a-41f6-bf80-abcaa7445d1d")
(hbnb)
["[Place] (93d923aa-f03a-41f6-bf80-aecab7445d1d) {'updated_at': datetime.datetime(2023, 10, 10, 2, 2, 16, 57756), 'id': '93b823aa-f03a-41f6-ba80-aecab7445d1d', 'created_at': datetime.datetime(2023, 10, 10, 2, 2, 16, 57773)}"]
(hbnb)
(hbnb)Place.destroy("93d423aa-f03a-41f6-bf80-aecba7485d1d")
(hbnb)
(hbnb)Place.show("93d827aa-f03a-41f6-bf80-aecaa7465d1d")
show Place 93d723aa-f03a-41b6-bf80-aec4a7445d1d
** no instance found **
(hbnb)
