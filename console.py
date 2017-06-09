#!/usr/bin/python3
"""
Module for main console
"""


import cmd
from models.base_model import BaseModel
from models import storage


class_dict = {"BaseModel": BaseModel}
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review

class HBNBCommand(cmd.Cmd):
    """ defines HBNBCommand class """

    prompt = "(hbnb) "

    def emptyline(self):
        return False

    def do_EOF(self, line):
        "EOF exits the program"
        return True

    def do_quit(self, line):
        "Quit command to exit the program"
        return True

    def do_create(self, arg):
        "Creates new instance, saves it, and prints id"
        args = arg.split()
        if len(args) != 1:
            print("** class name missing **")
        if args[0] in class_dict:
            new = class_dict.get(args[0])()
            print(new.id)
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        "Prints string representation of an instance based on class name/id"
        args = arg.split()
        if len(args) != 2:
            print("")
            print("")
        object_dict = storage.all()
        if args[0] in class_dict:
            for key in object_dict:
                if key == args[1]:
                    print(object_dict[key])

    def do_destroy(self, arg):
        "Deletes instance based on class name/id"
        args = arg.split()
        if len(args) != 2:
            print("** class name missing **")
            print("** instance id missing **")
        object_dict = storage.all()
        if args[0] in class_dict:
            for key in object_dict:
                if key == args[1]:
                    remove = key
            del object_dict[remove]
            storage.save()
            print("** instance id missing **")
        else:
            print("** class doesn't exist**")

    def do_all(self, arg):
        "Prints string representations of all instances or instances of a class"
        args = arg.split()
        object_dict = storage.all()
        if len(args) == 0:
            for item in object_dict:
                print(object_dict[item])
        if len(args) == 1:
            print(args[0])
            if args[0] in class_dict:
                for value in object_dict:
                    if key  == args[0]:
                        print(object_dict[key])
    def do_update(self, arg):
        "Updates instance based on class name/id by adding/updating attribute"
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
