# AirBnB Clone Project
The project is a command-line application inspired by the popular online platform Airbnb.

## Description
 * The Airbnb Clone project is a command-line application inspired by the popular online platform Airbnb. The app offers users a simplified yet interactive way to simulate various aspects of the Airbnb experience directly from the command line. By providing a command-line environment, the app offers users an opportunity to explore the core processes of Airbnb without the need for a graphical user interface.
 * **Please note** that the Airbnb Clone Project is an educational exercise and not a fully featured replacement for the actual Airbnb platform. It showcases the use of programming concepts to simulate the functionality of the popular online service in a text-based environment.


## Installation
```
git clone https://github.com/Basi-Letsholo/AirBnB_clone
cd AirBnB_clone
```
## How to Use Command Interpreter
```
---
| Commands  | Usage                                         | Functionality                              |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help`    | `help`                                        | displays all commands available            |
| `create`  | `create <class>`                              | creates new object (ex. a new User, Place) |
| `update`  | `User.update('123', {'name' : 'Sakhile'})`    | updates attribute of an object             |
| `destroy` | `User.destroy('123')`                         | destroys specified object                  |
| `show`    | `User.show('123')`                            | retrieve an object from a file, a database |
| `all`     | `User.all()`                                  | display all objects in class               |
| `quit`    | `quit`                                        | exits                                      |

```
## Usage
Interactive Mode
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Environment
* Language: Python3 (version 3.8.5)
* Editors: vi, vim
* OS: Ubuntu 20.04 LTS
* Style guidelines: [PEP 8](https://peps.python.org/pep-0008/) || [Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) || [Pycodestyle](https://pycodestyle.pycqa.org/en/latest/)

## Authors
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
 * Basi Letsholo
