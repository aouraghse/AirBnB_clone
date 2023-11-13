#!/usr/bin/python3
"""
This module activates python cli
"""
import json
import cmd
import sys
from models.base_model import BaseModel
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.city import City
from models.engine.file_storage import FileStorage
import shlex


def ev(val):
    """converts suitable arguments to int or float"""
    for i in val:
        try:
            yield json.loads(i)
        except Exception:
            yield i


def check_arg(arg2, msg):
    try:
        command, new_id = arg2.split('(')
    except Exception:
        print("** invalid command **")
        return None
    if command != msg:
        print("** invalid command **")
        return None
    return new_id.replace(')', '')


class HBNBCommand(cmd.Cmd):
    """CLI for AirBnB clone"""
    prompt = '(hbnb) '
    file = None
    classes = ['BaseModel', 'Place', 'State',
               'City', 'Amenity', 'Review', 'User']

    def do_EOF(self, line):
        """Handles EOF(Ctrl + D)"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()

    def do_create(self, args):
        """Creates a new instance of a class"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** class name missing **")
            return
        if arg2[0] not in self.classes:
            print("** class doesn't exist **")
            return
        model = eval(arg2[0])()
        model.save()
        print(model.id)

    def do_show(self, args):
        """Prints the string representation of an instance """
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** class name missing **")
            return
        if arg2[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg2) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(arg2[0], arg2[1])
        if y in tempD.keys():
            obj = tempD.get(y)
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** class name missing **")
            return
        if arg2[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg2) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(arg2[0], arg2[1])
        if y in tempD.keys():
            del tempD[y]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Creates a new instance of a class"""
        arg2 = shlex.split(args)
        if len(arg2) >= 1 and arg2[0] not in self.classes:
            print("** class doesn't exist **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        alList = []

        for key, obj in tempD.items():
            if len(arg2) >= 1:
                if args[0] in key:
                    alList.append(str(obj))
            else:
                alList.append(str(obj))
        print(alList)

    def do_update(self, args):
        """Updates an instance based on the class name and id by adding
        or updating attribute"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** class name missing **")
            return
        if arg2[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg2) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(arg2[0], arg2[1])
        if y not in tempD.keys():
            print("** no instance found **")
            return
        if len(arg2) < 3:
            print("** attribute name missing **")
            return
        if len(arg2) < 4:
            print("** value missing **")
            return
        arg2 = list(ev(arg2))
        obj = tempD.get(y)
        dict2 = obj.to_dict()
        dict2.update({arg2[2]: arg2[3]})
        obj2 = eval(arg2[0])(**dict2)
        obj2.save()
        tempD.update({y: obj2})
        storage.save()

    def emptyline(self):
        pass

        return

    def default(self, args):
        """Handles other commands"""
        args = shlex.split(args)
        try:
            arg1, arg2 = args[0].split('.')
            if len(args) > 1:
                for i in range(1, len(args)):
                    arg2 += args[i]
        except Exception:
            print("** invalid command **")
            return
        if arg1 not in self.classes:
            print("** class doesn't exist ")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        new_list = []
        for key, value in tempD.items():
            if arg1 in key:
                new_list.append(str(value))

        if arg2 == "all()":
            """
            Retrives all instances
            Usage: <class name>.all()
            """
            print(new_list)

        elif arg2 == "count()":
            """
            Retrieves number of instances of class
            Usage: <class name>.count()
            """
            print(len(new_list))

        elif "show" in arg2:
            """
            Retrieves instance based on id
            Usage: <class name>.show(<id>)
            """
            new_id = check_arg(arg2, "show")
            if not new_id:
                return
            for items in new_list:
                if new_id in items:
                    print(items)
                    return
            print("** no instance found **")

        elif "destroy" in arg2:
            """
            Destroys instance based on its id
            Usage: <class name>.destroy(<id>)
            """
            new_id = check_arg(arg2, "destroy")
            if not new_id:
                return
            y = f"{arg1}.{new_id}"
            if y in tempD.keys():
                del tempD[y]
                storage.save()
            else:
                print("** no instance found **")

        elif "update" in arg2:
            """
            Updates instance based on id
            Usage: <class name>.update(<id>, <name>, <value>)
            """
            new_arg = check_arg(arg2, "update")
            if not new_arg:
                return
            if '{' in new_arg:
                try:
                    new_list = list(new_arg.split('{'))
                except Exception:
                    print("** invalid arguments **")
                    return
                new_id = new_list[0].replace(',', '')
                new_dict = new_list[1].replace('}', '')
                new_list = list(new_dict.split(','))
                y = f"{arg1}.{new_id}"

                if y in tempD.keys():
                    for item in new_list:
                        try:
                            valx = list(item.split(':'))
                            valx = list(ev(valx))
                        except Exception:
                            print("** attribute name missing **")
                            return
                        setattr(tempD[y], valx[0], valx[1])
                    tempD[y].save()
                    storage.save()

                else:
                    print("** no instance found **")

            elif len(args) == 3:
                new_id, new_key, new_value = new_arg.split(',')
                new_list = []
                new_list.append(new_value)
                new_list = list(ev(new_list))
                new_value = new_list[0]
                y = f"{arg1}.{new_id}"
                if y in tempD.keys():
                    setattr(tempD[y], new_key, new_value)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** attribute missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()