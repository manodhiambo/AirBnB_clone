#!/usr/bin/env python3
""" AirBnB Console - Program that contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage


class HBNBCommand(cmd.Cmd):
    """ init Command Prompt """
    prompt = "(hbnb) "
    level = ["BaseModel", "City", "State",
             "User", "Place", "Review", "Amenity"]

    def do_EOF(self, args):
        """CTRl-D to exit\n"""
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """ENTER shouldn’t execute anything"""
        pass

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return None
        elif (line not in self.level):
            print("** class doesn't exist **")
            return None
        else:
            my_inst = eval(line + "()")
            my_inst.save()
            print(my_inst.id)

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id"""
        # First, separate in a list the commands by white space
        n = line.split()
        if not line:
            print("** class name missing **")
            return None
        elif (n[0] not in self.level):
            print("** class doesn't exist **")
            return None
        elif len(n) == 1:
            print("** instance id missing **")
            return None
        else:
            # concatenate class_name and id with a dot
            key = "{}.{}".format(n[0], n[1])
            # search in file json the key saved in key
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                obj = storage.all()
                # string representation of the instance with class name and id
                print(obj[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        n = line.split()
        if not line:
            print("** class name missing **")
            return None
        elif (n[0] not in self.level):
            print("** class doesn't exist **")
            return None
        elif len(n) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(n[0], n[1])
            if key not in storage.all().keys():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of
        all instances based or not on the class name"""
        n = line.split()
        obj_list = []
        if len(n) == 0:
            for value in storage.all().values():
                obj_list.append(value.__str__())
            print(obj_list)
        elif (n[0] not in self.level):
            print("** class dioesn't exist **")
        else:
            for key, value in storage.all().items():
                if n[0] in key:
                    obj_list.append(storage.all()[key].__str__())
                else:
                    return
            print(obj_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        n = line.split()
        if len(n) == 0:
            print("** class name missing **")
        elif (n[0] not in self.level):
            print("** class doesn't exist **")
        elif len(n) == 1:
            print("** instance id missing **")
        else:
            obj = storage.all()
            key = "{}.{}".format(n[0], n[1])
            if (key not in obj):
                print("** no instance found **")
            elif len(n) == 2:
                print("** attribute name missing **")
            elif len(n) == 3:
                print("** value missing **")
            else:
                # cast to the attribute type
                # arg_type = type(eval(n[3]))
                # attr = n[3].strip('\'\"')
                setattr(obj[key], n[2], n[3])
                storage.save()

    def do_count(self, line):
        """ retrieve the number of instances of a class """
        count = 0
        for key in storage.all().keys():
            if line in key:
                count += 1
        print(count)

    def default(self, line):
        """ Retrieve instances based on methods, i.e. <class name>.all() """
        n = line.split('.')
        inst = n[0]
        if n[1] == "all()":
            self.do_all(inst)
        elif n[1] == "count()":
            self.do_count(inst)
        elif n[1].startswith('show'):
            idsp = n[1].split('"')
            # BaseModel valid_id, idsp[1] to get the id
            line = inst + ' ' + idsp[1]
            self.do_show(line)
        elif n[1].startswith('destroy'):
            idsp = n[1].split('"')
            line = inst + ' ' + idsp[1]
            self.do_destroy(line)
        elif n[1].startswith('update'):
            sp = n[1].split('"')
            line = inst + ' ' + sp[1] + ' ' + sp[3] + ' ' + sp[5]
            self.do_update(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    # import sys
    # non-interactive mode
    # if len(sys.argv) > 1:
    # Since onecmd () takes a single string as input
    # the arguments of the program must be joined before passing them
    # HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    # HBNBCommand().cmdloop()
