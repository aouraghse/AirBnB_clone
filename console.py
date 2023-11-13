#!/usr/bin/python3
"""
Ce module active l'interface en ligne de commande Python
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
    """convertit les arguments appropriés en entier ou en décimal"""
    for i in val:
        try:
            yield json.loads(i)
        except Exception:
            yield i


def check_arg(argument, message):
    try:
        command, nouveau_ID = argument.split('(')
    except Exception:
        print("** invalid command **")
        return None
    if command != message:
        print("** invalid command **")
        return None
    return nouveau_ID.replace(')', '')


class HBNBCommand(cmd.Cmd):
    """Interface en ligne de commande pour le clone AirBnB"""
    prompt = '(hbnb) '
    file = None
    classes = ['BaseModel', 'Place', 'State',
               'City', 'Amenity', 'Review', 'User']

    def do_EOF(self, line):
        """EOF(Ctrl + D)"""
        print("")
        return True

    def do_quit(self, argument_0):
        """Commande Quitter pour quitter le programme"""
        quit()

    def do_create(self, args):
        """Crée une nouvelle instance d'une classe"""
        argument = shlex.split(args)
        if len(argument) < 1:
            print("** class name missing **")
            return
        if argument[0] not in self.classes:
            print("** class doesn't exist **")
            return
        model = eval(argument[0])()
        model.save()
        print(model.id)

    def do_show(self, args):
        """Affiche la représentation en chaîne d'une instance"""
        argument = shlex.split(args)
        if len(argument) < 1:
            print("** class name missing **")
            return
        if argument[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(argument) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(argument[0], argument[1])
        if y in tempD.keys():
            obj = tempD.get(y)
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Supprime une instance en fonction du nom de la classe et de l'identifiant"""
        argument = shlex.split(args)
        if len(argument) < 1:
            print("** class name missing **")
            return
        if argument[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(argument) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(argument[0], argument[1])
        if y in tempD.keys():
            del tempD[y]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Crée une nouvelle instance d'une classe"""
        argument = shlex.split(args)
        if len(argument) >= 1 and argument[0] not in self.classes:
            print("** class doesn't exist **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        alList = []

        for key, obj in tempD.items():
            if len(argument) >= 1:
                if args[0] in key:
                    alList.append(str(obj))
            else:
                alList.append(str(obj))
        print(alList)

    def do_update(self, args):
        """Met à jour une instance en fonction du nom de la classe et de
        l'identifiant en ajoutant ou en mettant à jour l'attribut"""
        argument = shlex.split(args)
        if len(argument) < 1:
            print("** class name missing **")
            return
        if argument[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(argument) < 2:
            print("** instance id missing **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(argument[0], argument[1])
        if y not in tempD.keys():
            print("** no instance found **")
            return
        if len(argument) < 3:
            print("** attribute name missing **")
            return
        if len(argument) < 4:
            print("** value missing **")
            return
        argument = list(ev(argument))
        obj = tempD.get(y)
        dict2 = obj.to_dict()
        dict2.update({argument[2]: argument[3]})
        obj2 = eval(argument[0])(**dict2)
        obj2.save()
        tempD.update({y: obj2})
        storage.save()

    def emptyline(self):
        pass

        return

    def default(self, args):
        """Gère les autres commandes"""
        args = shlex.split(args)
        try:
            arg1, argument = args[0].split('.')
            if len(args) > 1:
                for i in range(1, len(args)):
                    argument += args[i]
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

        if argument == "all()":
            print(new_list)

        elif argument == "count()":
            print(len(new_list))

        elif "show" in argument:
            nouveau_ID = check_arg(argument, "show")
            if not nouveau_ID:
                return
            for items in new_list:
                if nouveau_ID in items:
                    print(items)
                    return
            print("** no instance found **")

        elif "destroy" in argument:
            nouveau_ID = check_arg(argument, "destroy")
            if not nouveau_ID:
                return
            y = f"{arg1}.{nouveau_ID}"
            if y in tempD.keys():
                del tempD[y]
                storage.save()
            else:
                print("** no instance found **")

        elif "update" in argument:
            new_arg = check_arg(argument, "update")
            if not new_arg:
                return
            if '{' in new_arg:
                try:
                    new_list = list(new_arg.split('{'))
                except Exception:
                    print("** invalid arguments **")
                    return
                nouveau_ID = new_list[0].replace(',', '')
                new_dict = new_list[1].replace('}', '')
                new_list = list(new_dict.split(','))
                y = f"{arg1}.{nouveau_ID}"

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
                nouveau_ID, new_key, new_value = new_arg.split(',')
                new_list = []
                new_list.append(new_value)
                new_list = list(ev(new_list))
                new_value = new_list[0]
                y = f"{arg1}.{nouveau_ID}"
                if y in tempD.keys():
                    setattr(tempD[y], new_key, new_value)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** attribute missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()