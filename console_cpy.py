#!/usr/bin/python3
"""This module is the entry point of the command interpreter"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    __myClasses = {"BaseModel": BaseModel}

    def do_EOF(self, line):
        """Exits the program"""

        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        
        return True
    

    @staticmethod
    def __cmd_validation(usage, obj=None):
        for k, v in usage.items():
            if v == "" and k == "class_name":
                print("** class name missing **")
                return 0
            
            if v not in HBNBCommand.__myClasses and k == "class_name":
                print("** class doesn't exist **")
                return 0

            if v == "" and k == "obj_id":
                print("** instance id missing **")
                return 0
            
        if obj is not None:
          for v in obj.values():
            if v.id == usage["obj_id"]:
              break
          else:
            print("** no instance found **")
            return 0
                    

        if "attributes" in usage:
          pass
                
        
                    
    @staticmethod
    def handle_usage(line, usage):
        args = line.split()

        # let the length of args == the length of usage
        if len(args) > len(usage):
            args = args[:len(usage)]

        if len(args) < len(usage):
            for _ in range(len(usage) - len(args)):
                args.append("")

        i = 0
        for k in usage.keys():
            usage[k] = args[i]
            i += 1

    def do_create(self, line):
        """Description: Creates a new instance of BaseModel, saves it (to the JSON file) 
and prints the id

        Usage: create class_name
        """

        usage_create = {"class_name": ""}

        HBNBCommand.handle_usage(line, usage_create)
        is_validated = HBNBCommand.__cmd_validation(usage_create)
        if is_validated == 0:
            return
        

        my_model = BaseModel()
        my_model.save()
        print(my_model.id)

    
    def do_show(self, line):
        """Description: Prints the string representation of an instance based
         on the class name and id

        Usage: show class_name object_id
        """

        usage_show = {"class_name": "", "obj_id": ""}

        HBNBCommand.handle_usage(line, usage_show)
        
        all_objects = models.storage.all()

        is_validated = HBNBCommand.__cmd_validation(usage_show, all_objects)
        if is_validated == 0:
            return
        
        for v in all_objects.values():
            if v.id == usage_show["obj_id"]:
              print(v)

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
