#!/usr/bin/python3
# console.py
# Author: @tonybnya
"""
This module implements the entry point of the command line interpreter.
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """Class definition for the AirBnB Console.

    Attributes:
        prompt (str): A custom prompt defined for the Console.
        __classes (str): String representing different args corresponding to
        the classed defined.
    """

    # Interactive Mode
    prompt = "(hbnb) "
    # __classes = {
    #     "BaseModel",
    #     "User",
    #     "State",
    #     "City",
    #     "Place",
    #     "Amenity",
    #     "Review"
    # }

    # def do_create(self, args):
    #     """Create a BaseModel object, saves to a JSON file, prints the id."""
    #     if not args:
    #         print("** class name missing **")
    #     else:
    #         class_name = args.strip()
    #         if class_name not in HBNBCommand.__classes:
    #             print("** class doesn't exist **")
    #         else:
    #             storage.save()
    #             print(eval(class_name[0])().id)

    def emptyline(self):
        """Do not execute anything on empty arguments."""
        pass

    def do_EOF(self, args):
        """Quit the console on EOF signal."""
        print('')
        return True

    def do_quit(self, args):
        """Quit the console."""
        return True

    def help_EOF(self):
        """Documentation for the EOF signal."""
        print("Quit the console with the EOF signal")

    def help_quit(self):
        """Documentation for the quit command."""
        print("Quit command to exit the program")


# This module should not be executed when imported.
if __name__ == '__main__':
    # Non-Interactive Mode
    if not sys.stdin.isatty():
        pass

    HBNBCommand().cmdloop()
