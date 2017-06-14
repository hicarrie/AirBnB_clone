#!/usr/bin/python3
"""
Module for main console
"""


import cmd
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ defines HBNBCommand class """

    class_dict = {"BaseModel": BaseModel, "User": User, "State": State, "City":
                  City, "Amenity": Amenity, "Place": Place, "Review": Review}

    prompt = "(hbnb) "

    def emptyline(self):
        """Handles empty lines"""
        return False

    def do_EOF(self, line):
        """EOF exits the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates new instance, saves it, and prints id
        Usage: $ create <class name>"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.class_dict:
            new = self.class_dict.get(args[0])()
            storage.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints string representation of an instance based on class name/id
        Usage: $ show <class name> <id>"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) < 2 and args[0] in self.class_dict:
            print("** instance id missing **")
            return

        object_dict = storage.all()
        if args[0] in self.class_dict:
            for full_key in object_dict:
                key = full_key.split(".")
                if key[1] == args[1]:
                    print(object_dict[full_key])
                    return
            print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes instance based on class name/id
        Usage: $ destroy <class name> <id>"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) < 2 and args[0] in self.class_dict:
            print("** instance id missing **")
            return
        elif len(args) < 2:
            print("** class name missing **")
            return

        object_dict = storage.all()
        if args[0] in self.class_dict:
            for full_key in object_dict:
                key = full_key.split(".")
                if key[1] == args[1]:
                    del object_dict[full_key]
                    storage.save()
                    return
            print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representation of all instances of a class
        Usage: $ all <class name> or $ all"""
        args = arg.split()
        object_dict = storage.all()
        if len(args) == 0:
            for item in object_dict:
                print(object_dict[item])
        if len(args) == 1:
            if args[0] in self.class_dict:
                for key, value in object_dict.items():
                    if value.__class__.__name__ == args[0]:
                        print(value)
            else:
                print("** class doesn't exist **")
                return
            if not object_dict:
                print("[]")

    def do_update(self, arg):
        """Updates instance based on class name/id by adding/updating attribute
        Usage: $ update <class name> <id> <attribute name> <attribute value>"""
        args = arg.split()
        object_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in self.class_dict:
            if len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** attribute value missing **")
                return
        else:
            print("** class doesn't exist **")
            return

        for i in range(len(args)):
            if args[i].startswith('"') and args[i].endswith('"'):
                args[i] = args[i][1:-1]

        for full_key in object_dict.keys():
            key = full_key.split('.')
            key_id = key[1]
            if args[0] in self.class_dict:
                if args[1] == object_dict[full_key].id:
                    setattr(object_dict[full_key], args[2], args[3])
                    setattr(object_dict[full_key], "updated_at",
                            datetime.now())
                    storage.save()
                    return
            else:
                print("** class doesn't exist **")
                return
        print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
