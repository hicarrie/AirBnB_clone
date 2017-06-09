#!/usr/bin/python3
"""
Module for main console
"""


import cmd
from models.base_model import BaseModel
from models import storage


class_dict = {"BaseModel": BaseModel}
        #"User": User,
        #"State": State,
        #"City": City,
        #"Amenity": Amenity,
        #"Place": Place,
        #"Review": Review

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
            print("** class name missing **")
            print("** instance id missing **")
        object_dict = storage.all()
        if args[0] in class_dict:
            for full_key in object_dict:
                key = full_key.split(".")
                id_only = key[1]
                if key[1] == args[1]:
                    print(object_dict[full_key])
                    break
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        "Deletes instance based on class name/id"
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **")
            print("** instance id missing **")
        object_dict = storage.all()
        if args[0] in class_dict:
            for full_key in object_dict:
                key = full_key.split(".")
                id_only = key[1]
                if key[1] == args[1]:
                    remove = full_key
                    del object_dict[full_key]
                    storage.save()
                    break
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
            if args[0] in class_dict:
                for key, value in object_dict.items():
                    if value.__class__.__name__ == args[0]:
                        print(value)

    def do_update(self, arg):
        "Updates instance based on class name/id by adding/updating attribute"
        args = arg.split(" ", 3)
        object_dict = storage.all()
        #if id is missing
        print("** instance id missing **")
        #if class name is missing
        print("** class name missing **")
        #if attribute value is missing
        print("** value missing **")
        #if attribute name is missing
        print("** attribute name missing **")
        for full_key in object_dict.keys():
            key = full_key.split('.')
            print("KEY:", key)
            key_id = key[1]
            print("KEY_ID:", key_id)
            print("ARGS[0]:", args[0])
            if object_dict[key].__class__.__name__ == args[0]:
                if key[1] == args[1]:
                    setattr(object_dict[key], args[2], args[3])
                    storage.save()
                    return
            #if id doesn't exist
            print("** no instance found **")
       # else:
            #if class name doesn't exist
        #    print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
