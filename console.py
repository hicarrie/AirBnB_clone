#!/usr/bin/python3
"""
Module for main console
"""


import cmd


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
