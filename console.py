#!/usr/bin/python3


import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
