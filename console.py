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


def check_arg(arg2, msg):
    try:
        command, new_id = arg2.split('(')
    except Exception:
        print("** commande invalide **")
        return None
    if command != msg:
        print("** commande invalide **")
        return None
    return new_id.replace(')', '')


class HBNBCommand(cmd.Cmd):
    """Interface en ligne de commande pour le clone AirBnB"""
    prompt = '(hbnb) '
    file = None
    classes = ['BaseModel', 'Place', 'State', 'City', 'Amenity', 'Review', 'User']

    def do_EOF(self, line):
        """Gère la fin de fichier (Ctrl + D)"""
        print("")
        return True

    def do_quit(self, arg):
        """Commande Quitter pour quitter le programme"""
        quit()

    def do_create(self, args):
        """Crée une nouvelle instance d'une classe"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** nom de classe manquant **")
            return
        if arg2[0] not in self.classes:
            print("** la classe n'existe pas **")
            return
        model = eval(arg2[0])()
        model.save()
        print(model.id)

    def do_show(self, args):
        """Affiche la représentation en chaîne d'une instance"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** nom de classe manquant **")
            return
        if arg2[0] not in self.classes:
            print("** la classe n'existe pas **")
            return
        if len(arg2) < 2:
            print("** identifiant d'instance manquant **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(arg2[0], arg2[1])
        if y in tempD.keys():
            obj = tempD.get(y)
            print(obj)
        else:
            print("** aucune instance trouvée **")

    def do_destroy(self, args):
        """Supprime une instance en fonction du nom de la classe et de l'identifiant"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** nom de classe manquant **")
            return
        if arg2[0] not in self.classes:
            print("** la classe n'existe pas **")
            return
        if len(arg2) < 2:
            print("** identifiant d'instance manquant **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(arg2[0], arg2[1])
        if y in tempD.keys():
            del tempD[y]
            storage.save()
        else:
            print("** aucune instance trouvée **")

    def do_all(self, args):
        """Crée une nouvelle instance d'une classe"""
        arg2 = shlex.split(args)
        if len(arg2) >= 1 and arg2[0] not in self.classes:
            print("** la classe n'existe pas **")
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
        """Met à jour une instance en fonction du nom de la classe et de l'identifiant en ajoutant
        ou en mettant à jour l'attribut"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** nom de classe manquant **")
            return
        if arg2[0] not in self.classes:
            print("** la classe n'existe pas **")
            return
        if len(arg2) < 2:
            print("** identifiant d'instance manquant **")
            return
        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        y = "{}.{}".format(arg2[0], arg2[1])
        if y not in tempD.keys():
            print("** aucune instance trouvée **")
            return
        if len(arg2) < 3:
            print("** nom d'attribut manquant **")
            return
        if len(arg2) < 4:
            print("** valeur manquante **")
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
        """Gère les autres commandes"""
        args = shlex.split(args)
        try:
            arg1, arg2 = args[0].split('.')
            if len(args) > 1:
                for i in range(1, len(args)):
                    arg2 += args[i]
        except Exception:
            print("** commande invalide **")
            return
        if arg1 not in self.classes:
            print("** la classe n'existe pas ")
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
            Récupère toutes les instances
            Utilisation: <nom de la classe>.all()
            """
            print(new_list)

        elif arg2 == "count()":
            """
            Récupère le nombre d'instances de la classe
            Utilisation: <nom de la classe>.count()
            """
            print(len(new_list))

        elif "show" in arg2:
            """
            Récupère une instance en fonction de l'id
            Utilisation: <nom de la classe>.show(<id>)
            """
            new_id = check_arg(arg2, "show")
            if not new_id:
                return
            for items in new_list:
                if new_id in items:
                    print(items)
                    return
            print("** aucune instance trouvée **")

        elif "destroy" in arg2:
            """
            Détruit une instance en fonction de son id
            Utilisation: <nom de la classe>.destroy(<id>)
            """
            new_id = check_arg(arg2, "destroy")
            if not new_id:
                return
            y = f"{arg1}.{new_id}"
            if y in tempD.keys():
                del tempD[y]
                storage.save()
            else:
                print("** aucune instance trouvée **")

        elif "update" in arg2:
            """
            Met à jour une instance en fonction de l'id
            Utilisation: <nom de la classe>.update(<id>, <nom>, <valeur>)
            """
            new_arg = check_arg(arg2, "update")
            if not new_arg:
                return
            if '{' in new_arg:
                try:
                    new_list = list(new_arg.split('{'))
                except Exception:
                    print("** arguments invalides **")
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
                            print("** nom d'attribut manquant **")
                            return
                        setattr(tempD[y], valx[0], valx[1])
                    tempD[y].save()
                    storage.save()

                else:
                    print("** aucune instance trouvée **")

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
                    print("** aucune instance trouvée **")
            else:
                print("** attribut manquant **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

