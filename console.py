#!/usr/bin/python3
"""Command interperter"""

import cmd
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for HBNB
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D).
        """
        return True

    def do_help(self, arg):
        """
        Display help message.
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def preloop(self):
        """Initialize the classes dictionary."""
        self.classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }


if __name__ == '__main__':
    HBNBCommand().cmdloop()
