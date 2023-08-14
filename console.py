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
    """Command interpreter for HBNB."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)."""
        return True

    def do_help(self, arg):
        """Display help message."""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing on an empty line."""
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

    def precmd(self, line):
        """Prints newline after prompt if non-interactive."""
        if not sys.stdin.isatty():
            print("")
        return line

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        input_create = arg.split()

        if len(input_create) == 0:
            print("** class name missing **")
        elif input_create[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_base_model = BaseModel()
            new_base_model.save()
            print(new_base_model.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        input_show = arg.split()

        if len(input_show) == 0:
            print("** class name missing **")
        else:
            if input_show[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(input_show) < 2:
                print("** instance id missing **")
            else:
                instance_id = input_show[1]
                key = "{}.{}".format(BaseModel, instance_id)
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        input_destroy = arg.split()

        if len(input_destroy) == 0:
            print("** class name missing **")
        else:
            if input_destroy[0] != "BaseModel":
                print("** class doesn't exist **")
            elif len(input_destroy) < 2:
                print("** instance id missing **")
            else:
                instance_id = input_destroy[1]
                key = "{}.{}".format(input_destroy[0], instance_id)
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Print all string representation of instances."""
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            instances = []
            for key, obj in storage.all().items():
                if not arg or key.startswith("BaseModel"):
                    instances.append(str(obj))
            print(instances)

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        input_update = arg.split()

        if len(input_update) == 0:
            print("** class name missing **")
        else:
            class_name = input_update[0]
            if class_name != "BaseModel":
                print("** class doesn't exist **")
            elif len(input_update) < 2:
                print("** instance id missing **")
            else:
                instance_id = input_update[1]
                key = "{}.{}".format(class_name, instance_id)
                if key not in storage.all():
                    print("** no instance found **")
                elif len(input_update) < 3:
                    print("** attribute name missing **")
                else:
                    attr_name = input_update[2]
                    if len(input_update) < 4:
                        print("** value missing **")
                    else:
                        attr_value = input_update[3]
                        obj = storage.all()[key]
                        setattr(obj, attr_name, attr_value)
                        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
