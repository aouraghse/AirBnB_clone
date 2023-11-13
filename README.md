![HBNB](http://imgur.com/JBCMHDP.png)

## AirBnB Clone 

### Synopsis
The objective of the AirBnB Clone project is to learn the fundamental concepts to building a web application similar to AirBnB. AirBnB. AirBnB is an online marketplace and hospitality service, enabling people to lease or rent short-term lodging.

This portion of the project is the first step towards building the full web application; it includes a command interpreter (accessed through a console) for manipulating data and Holberton AirBnB (`HBNB`) objects.

This command interpreter is able to:
* [] - Create a new object
* [] - Retrieve an object from a file
* [] - Do operations on objects
* [] - Update attributes of an object
* [] - Destroy an object

### Environment
Our AirBnB Clone has been tested on `Ubuntu 14.04 LTS` using `python3` (`version 3.4.3`) and adheres to `PEP 8` style protocols. 

Tests done in VirtualBox on [Ubuntu](https://atlas.hashicorp.com/ubuntu/boxes/trusty64) via [Vagrant](https://www.vagrantup.com/)(1.9.1)

### Repository Contents
The repository contains the following files:

|   **File**    |  **Decription**                       |
|---------------|---------------------------------------|
| console.py   | entry point of the command interpreter           |
| init_test.sh      | executes all the test files from tests folder        |
| models/__init__.py | creates an instance of FileStorage |
| models/amenity.py | class Amenity, inherits from BaseModel |
| models/base_model.py | class BaseModel that defines all common attributes/methods for other classes |
| models/city.py | class City, inherits from BaseModel |
| models/place.py | class Place, inherits from BaseModel |
| models/review.py | class Review, inherits from BaseModel |
| models/state.py | class State, inherits from BaseModel |
| models/user.py | class User, inherits from BaseModel |
| models/engine/file_storage.py | class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances |
| tests/test_models/amenity_test.py | tests Amenity class |
| tests/test_models/basemodel_test.py | tests BaseModel class |
| tests/test_models/city_test.py | tests City class |
| tests/test_models/place_test.py | tests Place class |
| tests/test_models/review_test.py | tests Review class |
| tests/test_models/state_test.py | tests State class |
| tests/test_models/user_test.py | tests User class |

* When objects are saved and reloaded they will be saved and read from `file.json`. If the file does not exist, it will be created. If the file exists and is not empty, the contents will be overwritten.

### Description of Classes
1. [models/amenity.py](models/amenity.py) - Class Amenity, inherits from BaseModel
  * ``name`` - public class attribute
2. [models/base_model.py](models/base_model.py) - Class BaseModel that defines all common attributes/methods for other classes
  * ``dt_format`` - public class attribute that defines format of the date and time
  * ``id`` - public instance attribute, assigned with an uuid when an instance is created
  * ``created_at`` - public instance attribute, datetime - assigned with the current datetime when an instance is created
  * ``updated_at`` - public instance attribute, datetime - assigned with the current datetime when an instance is updated
  * ``save`` - public instance method that updates the public instance attribute updated_at with the current datetime
  * ``to_json`` - public instance method that returns a dictionary containing all keys/values of __dict__ of the instance + the class name in the key __class__
3. [models/city.py](models/city.py) - Class City, inherits from BaseModel
  * ``state_id`` - public class attribute: it will be the State.id
  * ``name`` - public class attribute
4. [models/place.py](models/place.py) - Class Place, inherits from BaseModel
  * ``city_id`` - public class attribute: it will be the City.id
  * ``user_id`` - public class attribute: it will be the User.id
  * ``name`` - public class attribute
  * ``description`` - public class attribute
  * ``number_rooms`` - public class attribute
  * ``number_bathrooms`` - public class attribute
  * ``max_guest`` - public class attribute
  * ``price_by_night`` - public class attribute
  * ``latitude`` - public class attribute
  * ``longitude`` - public class attribute
  * ``amenity_ids`` - public class attribute: it will be the list of Amenity.id
5. [models/review.py](models/review.py) - Class Review, inherits from BaseModel
  * ``place_id`` - public class attribute: it will be the Place.id
  * ``user_id`` - public class attribute: it will be the User.id
  * ``text`` - public class attribute
6. [models/state.py](models/state.py) - Class State, inherits from BaseModel
  * ``name`` - public class attribute
7. [models/user.py](models/user.py) - Class User, inherits from BaseModel
  * ``email`` - public class attribute
  * ``password`` - public class attribute
  * ``first_name`` - public class attribute
  * ``last_name`` - public class attribute
8. [models/engine/file_storage.py](models/engine/file_storage.py) - Class FileStorage, serializes instances to a JSON file and deserializes JSON file to instances
  * ``__file_path`` - private class attribute; path to the JSON file
  * ``__objects`` - private class attribute; empty but will store all objects by <class name>.id
  * ``all`` - public instance method; returns __objects
  * ``new`` - public instance method; sets in __objects the obj with key <obj class name>.id
  * ``save`` - public instance method; serializes __objects to the JSON file
  * ``reload`` - public instance method; deserializes the JSON file to __objects

### How to Use The Console
First, clone the repository into your directory.
```
$ git clone https://github.com/lisale0/AirBnB_clone

## Example of Use
Run the executable `./console.py`
```
Type `help` for a list of the commands available with `console.py`.

`help` is an action provided by default by `cmd`.

Enter `help` + `command` for information about respective command and usage.

```
vagrant@vagrant$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all     destroy  quit  update
BaseModel  EOF   Review  User   create  help     show

(hbnb) create City
4af7890c-007f-42ff-97d8-074214f1094f
(hbnb) show City 4af7890c-007f-42ff-97d8-074214f1094f
[City] (4af7890c-007f-42ff-97d8-074214f1094f) {'id': '4af7890c-007f-42ff-97d8-074214f1094f',
 'updated_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679386), '__class__': 'City',
 'created_at': datetime.datetime(2017, 6, 11, 1, 6, 39, 679362)}
(hbnb)$
```

### Primary console commands

* `create` -- creates a new instance of `BaseModel`, saves it to the `JSON` (`file.json`) and prints its `id`.
Ex. usage: `create Amenity`

```
(hbnb) create Amenity
ada6dd72-cd6b-4a5f-9c02-68f401dd7baa

(hbnb) all Amenity
[Amenity] (ada6dd72-cd6b-4a5f-9c02-68f401dd7baa) {'created_at': datetime.datetime(2017, 6, 15, 17, 12, 28, 631950), 'updated_at': datetime.datetime(2017, 6, 15, 17, 12, 28, 631967), 'id': 'ada6dd72-cd6b-4a5f-9c02-68f401dd7baa'}
```

* `show` -- prints the string representation of an instance based on its `class name` and `id`.
Ex. usage: `show BaseModel cfa037cb-78d1-478e-ae4d-f0ef3acd7173`

```
(hbnb) create BaseModel
cfa037cb-78d1-478e-ae4d-f0ef3acd7173
(hbnb) show BaseModel cfa037cb-78d1-478e-ae4d-f0ef3acd7173
[BaseModel] (cfa037cb-78d1-478e-ae4d-f0ef3acd7173) {'created_at': datetime.datetime(2017, 6, 15, 17, 16, 14, 463963), 'updated_at': datetime.datetime(2017, 6, 15, 17, 16, 14, 463994), 'id': 'cfa037cb-78d1-478e-ae4d-f0ef3acd7173'}
```

* `destroy` -- deletes an instance of an object based on the `class name` and `id` entered. Changes are saved into the `JSON` (`file.json`) file.
Ex. usage: `destroy BaseModel cfa037cb-78d1-478e-ae4d-f0ef3acd7173`

```
(hbnb) destroy BaseModel cfa037cb-78d1-478e-ae4d-f0ef3acd7173
(hbnb) show BaseModel cfa037cb-78d1-478e-ae4d-f0ef3acd7173
** no instance found **
```

* `all` -- prints all reprentations of specified instances or all instances if none specified
Ex usage: `all City` displays all city instances
`all` displays all instances

```
(hbnb) all
[City] (1f75d5b0-f3af-4104-8063-128dca5928f2) {'created_at': datetime.datetime(2017, 6, 15, 17, 30, 49, 887988), 'updated_at': datetime.datetime(2017, 6, 15, 17, 30, 49, 888034), 'id': '1f75d5b0-f3af-4104-8063-128dca5928f2'}
[State] (b11e9ba3-6201-4ff6-83f8-60b47343cb8d) {'created_at': datetime.datetime(2017, 6, 15, 17, 30, 57, 103554), 'updated_at': datetime.datetime(2017, 6, 15, 17, 30, 57, 103573), 'id': 'b11e9ba3-6201-4ff6-83f8-60b47343cb8d'}
[User] (4fef4387-88d8-465d-8878-fc55552f32a1) {'created_at': datetime.datetime(2017, 6, 15, 17, 20, 54, 223298), 'updated_at': datetime.datetime(2017, 6, 15, 17, 20, 54, 223314), 'id': '4fef4387-88d8-465d-8878-fc55552f32a1'}
```

* `update` -- updates an instance based on the `class name` and `id` supplied. Changes are saved into the `JSON` (`file.json`) file.
Ex usage: `update Amenity ada6dd72-cd6b-4a5f-9c02-68f401dd7baa housekeeping yes'

```
(hbnb) update Amenity ada6dd72-cd6b-4a5f-9c02-68f401dd7baa housekeeping yes
(hbnb) all
[Amenity] (ada6dd72-cd6b-4a5f-9c02-68f401dd7baa) {'updated_at': datetime.datetime(2017, 6, 15, 17, 13, 50, 31308), 'created_at': datetime.datetime(2017, 6, 15, 17, 12, 28, 631950), 'id': 'ada6dd72-cd6b-4a5f-9c02-68f401dd7baa', 'housekeeping': 'yes'}
```

* `quit` -- exits the program

* `EOF` -- exits the program 

### Notes
Other functionalities are currently in development.

### To do list
Console

* for `update`, for format `update <class name> <id> <attribute name> "<attribute value>"`, deal with case if <attribute value> is more than one word.

```
DESIRED OUTPUT:
```
[City] (1f75d5b0-f3af-4104-8063-128dca5928f2) {'id': '1f75d5b0-f3af-4104-8063-128dca5928f2', 'updated_at': datetime.datetime(2017, 6, 15, 20, 7, 9, 581835), 'created_at': datetime.datetime(2017, 6, 15, 17, 30, 49, 887988), 'name': 'San'}
```
GOT:
```
[City] (1f75d5b0-f3af-4104-8063-128dca5928f2) {'id': '1f75d5b0-f3af-4104-8063-128dca5928f2', 'updated_at': datetime.datetime(2017, 6, 15, 20, 7, 9, 581835), 'created_at': datetime.datetime(2017, 6, 15, 17, 30, 49, 887988), 'name': 'San Francisco'}
```

* `update BaseModel + existing ID`
GOT:
```
** attribute name missing **
** value missing **
```
DESIRED OUTPUT:
```
** attribute name missing **
```

* `update BaseModel`
GOT:
```
** instance id missing **
** attribute name missing **
** value missing **
```

DESIRED OUTPUT:
```
** instance id missing **
** attribute name missing **
** value missing **
```

Unittests for Console
* Test `quit` is present
* Test `EOF` is present
* Test `help` is present
* Test `empty line` is present
* Test `create BaseModel` is present
* Test `show BaseModel` is present
* Test `destroy BaseModel` is present
* Test `all BaseModel` is present
* Test `update BaseModel` is present
* Test `BaseModel.all()` is present
* Test `Review.all()` is present
* Test `User.all()` is present
* Test `State.all()` is present
* Test `City.all()` is present
* Test `Amenity.all()` is present
* Test `Place.all()` is present
* Test `BaseModel.count()` is present
* Test `User.count()` is present
* Test `State.count()` is present
* Test `Place.count()` is present
* Test `City.count()` is present
* Test `Amenity.count()` is present
* Test `Review.count()` is present
* Test `BaseModel.show("id")` is present
* Test `User.show("id")` is present
* Test `State.show("id")` is present
* Test `City.show("id")` is present
* Test `Amenity.show("id")` is present
* Test `Place.show("id")` is present
* Test `Review.show("id")` is present
* Test `BaseModel.destroy("id")` is present
* Test `User.destroy("id")` is present
* Test `City.destroy("id")` is present
* Test `State.destroy("id")` is present
* Test `Place.destroy("id")` is present
* Test `Amenity.destroy("id")` is present
* Test `Review.destroy("id")` is present
* Test `BaseModel.update("id", "attribute_name", "string_value")` is present
* Test `User.update("id", "attribute_name", "string_value")` is present
* Test `State.update("id", "attribute_name", "string_value")` is present
* Test `City.update("id", "attribute_name", "string_value")` is present
* Test `Place.update("id", "attribute_name", "string_value")` is present
* Test `Amenity.update("id", "attribute_name", "string_value")` is present
* Test `Review.update("id", "attribute_name", "string_value")` is present
* Test `BaseModel.update("id", { "attribute_name": "string_value" })` is present
* Test `User.update("id", { "attribute_name": "string_value" })` is present
* Test `State.update("id", { "attribute_name": "string_value" })` is present
* Test `Amenity.update("id", { "attribute_name": "string_value" })` is present
* Test `City.update("id", { "attribute_name": "string_value" })` is present
* Test `Place.update("id", { "attribute_name": "string_value" })` is present
* Test `Review.update("id", { "attribute_name": "string_value" })` is present

### Authors
*Lisa Leung* - [Github](https://github.com/lisale0) || [Twitter](https://twitter.com/lisale01) || [email](lisa.leung@holbertonschool.com)

*Spencer Cheng* - [Github](https://github.com/spencerhcheng) || [Twitter](https://twitter.com/spencerhcheng) || [email](spencer.cheng@gmail.com)

*Julija Lee* - [Github](https://github.com/FreeJules) || [Twitter](https://twitter.com/LeeJulija) || [email](julijalee@gmail.com)

#### Feedback and contributors welcomed. Please reach out to either authors.
