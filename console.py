#!/usr/bin/python3
# console.py
# Author: @tonybnya
"""
This module implements the entry point of the command line interpreter.
"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(line):
    """
    Helper function to parse the arguments for the command line.
    """
    curly_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)

    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(line)]

        lexer = split(line[:brackets.span()[0]])
        args = [i.strip(",") for i in lexer]
        args.append(brackets.group())
        return args

    lexer = split(line[:curly_braces.span()[0]])
    args = [i.strip(",") for i in lexer]
    args.append(curly_braces.group())

    return args


class HBNBCommand(cmd.Cmd):
    """
    Class definition for the AirBnB Console.

    Attributes:
        prompt (str): A custom prompt defined for the Console.
        __classes (str): String representing different args corresponding to
        the classed defined.
    """

    # Interactive Mode
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_create(self, line):
        """
        Create a BaseModel object, saves to a JSON file, prints the id.

        Usage: create <class_name>
        """
        if not line:
            print("** class name missing **")
        else:
            args = parse(line)
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                storage.save()
                print(eval(args[0])().id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based of the class name
        and id.

        Usage: show <class_name> <id>
        """
        if not line:
            print("** class name missing **")
        else:
            args = parse(line)
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance = storage.all().get("{}.{}".format(args[0], args[1]))
                if instance is None:
                    print("** no instance found **")
                else:
                    print(instance)

    def emptyline(self):
        """
        Do not execute anything on empty arguments.
        """
        pass

    def do_EOF(self, line):
        """
        Quit the console on EOF signal.
        """
        print('')
        return True

    def do_quit(self, line):
        """
        Quit the console.
        """
        return True

    def help_EOF(self):
        """
        Documentation for the EOF signal.
        """
        print("Quit the console with the EOF signal")

    def help_quit(self):
        """
        Documentation for the quit command.
        """
        print("Quit command to exit the program")


# This module should not be executed when imported.
if __name__ == '__main__':
    HBNBCommand().cmdloop()
