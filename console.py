#!/usr/bin/python3
"""Module for the console application
"""
from cmd import Cmd


class HBNBCommand(Cmd):
    """Console-based interpreter for different commands"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Quit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
