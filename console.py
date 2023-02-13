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

    Args:
        line (str): the input text to be parsed.
    """
    curly_braces = re.search(r"\{(.*?)\}", line)
    brackets = re.search(r"\[(.*?)\]", line)

    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(line)]

        lexer = split(line[: brackets.span()[0]])
        args = [i.strip(",") for i in lexer]
        args.append(brackets.group())
        return args

    lexer = split(line[: curly_braces.span()[0]])
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
        "BaseModel", "User", "State", "City", "Place", "Amenity", "Review"
    }

    def emptyline(self):
        """
        Do not execute anything on empty arguments.
        """
        pass

    def do_EOF(self, line):
        """
        Quit the console on EOF signal.

        Args:
            line (str): input command.
        """
        print("")
        return True

    def do_quit(self, line):
        """
        Quit the console.

        Args:
            line (str): input command.
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

    def do_create(self, line):
        """
        Create a BaseModel object, saves to a JSON file, prints the id.

        Args:
            line (str): input command.

        Usage: create <class name>
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

        Args:
            line (str): input command.

        Usage: show <class name> <id>
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

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id and saves the change
        into the JSON file.

        Args:
            line (str): input command.

        Usage: destroy <class name> <id>
        """
        if not line:
            print("** class name missing **")
            return

        args = parse(line)
        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        elif len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def all(self, line):
        """
        Prints all string representation of all instances based or not on the
        class name.

        Args:
            line (str): input command.

        Usage: all or all <class name>
        """
        args = parse(line)

        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            list_objects = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    list_objects.append(obj.__str__())
                elif len(args) == 0:
                    list_objects.append(obj.__str__())

            print(list_objects)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute, and saves the change into JSON file.

        Args:
            line (str): input command.

        Usage: <class name> <id> <attribute name> "<attribute value>"
        """
        args = parse(line)

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all().keys:
            print("** no instance found **")
            return

        if len(args) == 2:
            print("** attribute name missing **")
            return

        if len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return

        if len(args) == 4:
            obj = storage.all()[key]
            if args[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = value_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = storage.all()[key]
            for key, value in eval(args[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in (str, int,
                                                              float)):
                    value_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = value_type
                else:
                    obj.__dict__[key] = value

        storage.save()


# This module should not be executed when imported.
if __name__ == "__main__":
    HBNBCommand().cmdloop()
