#!/usr/bin/python3
"""
Ce module active l'interface de ligne de commande Python (CLI)
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
    """Convertit les arguments appropriés en entier ou en nombre à virgule flottante"""
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
    return new_id.rstrip(')')


class HBNBCommand(cmd.Cmd):
    """Interface en ligne de commande (CLI) pour le clone d'AirBnB"""
    prompt = '(hbnb) '
    file_storage = FileStorage()
    file_storage.reload()
    classes = ['BaseModel', 'Place', 'State', 'City', 'Amenity', 'Review', 'User']

    def do_EOF(self, line):
        """Gère la fin de fichier (Ctrl + D)"""
        print("")
        return True

    def do_quit(self, arg):
        """Commande Quit pour quitter le programme"""
        quit()

    def do_create(self, args):
        """Crée une nouvelle instance d'une classe"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** nom de classe manquant **")
            return
        if arg2[0] not in self.classes:
            print("** classe inexistante **")
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
            print("** classe inexistante **")
            return
        if len(arg2) < 2:
            print("** identifiant d'instance manquant **")
            return
        temp_d = self.file_storage.all()
        instance_key = "{}.{}".format(arg2[0], arg2[1])
        if instance_key in temp_d.keys():
            obj = temp_d.get(instance_key)
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
            print("** classe inexistante **")
            return
        if len(arg2) < 2:
            print("** identifiant d'instance manquant **")
            return
        temp_d = self.file_storage.all()
        instance_key = "{}.{}".format(arg2[0], arg2[1])
        if instance_key in temp_d.keys():
            del temp_d[instance_key]
            self.file_storage.save()
        else:
            print("** aucune instance trouvée **")

    def do_all(self, args):
        """Récupère toutes les instances d'une classe ou celles qui correspondent à un filtre"""
        arg2 = shlex.split(args)
        if len(arg2) >= 1 and arg2[0] not in self.classes:
            print("** classe inexistante **")
            return
        temp_d = self.file_storage.all()
        instances_list = []

        for key, obj in temp_d.items():
            if len(arg2) >= 1:
                if arg2[0] in key:
                    instances_list.append(str(obj))
            else:
                instances_list.append(str(obj))
        print(instances_list)

    def do_update(self, args):
        """Met à jour une instance en fonction du nom de la classe et de l'identifiant en ajoutant
        ou en mettant à jour un attribut"""
        arg2 = shlex.split(args)
        if len(arg2) < 1:
            print("** nom de classe manquant **")
            return
        if arg2[0] not in self.classes:
            print("** classe inexistante **")
            return
        if len(arg2) < 2:
            print("** identifiant d'instance manquant **")
            return
        temp_d = self.file_storage.all()
        instance_key = "{}.{}".format(arg2[0], arg2[1])
        if instance_key not in temp_d.keys():
            print("** aucune instance trouvée **")
            return
        if len(arg2) < 3:
            print("** nom d'attribut manquant **")
            return
        if len(arg2) < 4:
            print("** valeur manquante **")
            return
        arg2 = list(ev(arg2))
        obj = temp_d.get(instance_key)
        dict2 = obj.to_dict()
        dict2.update({arg2[2]: arg2[3]})
        obj2 = eval(arg2[0])(**dict2)
        obj2.save()
        temp_d.update({instance_key: obj2})
        self.file_storage.save()

    def emptyline(self):
        pass

    def default(self, args):
        """Gère les autres commandes"""
        args = shlex.split(args)
        try:
            arg1, arg2 = args[0].split('.')
            if len(args) > 1:
                arg2 += ''.join(args[1:])
        except Exception:
            print("** commande invalide **")
            return
        if arg1 not in self.classes:
            print("** classe inexistante ")
            return
        temp_d = self.file_storage.all()
        new_list = [str(value) for key, value in temp_d.items() if arg1 in key]

        if arg2 == "all()":
            print(new_list)
        elif arg2 == "count()":
            print(len(new_list))
        elif "show" in arg2:
            new_id = check_arg(arg2, "show")
            if not new_id:
                return
            for items in new_list:
                if new_id in items:
                    print(items)
                    return
            print("** aucune instance trouvée **")
        elif "destroy" in arg2:
            new_id = check_arg(arg2, "destroy")
            if not new_id:
                return
            instance_key = f"{arg1}.{new_id}"
            if instance_key in temp_d.keys():
                del temp_d[instance_key]
                self.file_storage.save()
            else:
                print("** aucune instance trouvée **")
        elif "update" in arg2:
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
                instance_key = f"{arg1}.{new_id}"
                if instance_key in temp_d.keys():
                    for item in new_list:
                        try:
                            attr_name, attr_value = list(item.split(':'))
                            attr_value = next(ev([attr_value]))
                        except Exception:
                            print("** nom d'attribut manquant **")
                            return
                        setattr(temp_d[instance_key], attr_name, attr_value)
                    temp_d[instance_key].save()
                    self.file_storage.save()
                else:
                    print("** aucune instance trouvée **")
            elif len(args) == 3:
                new_id, new_key, new_value = new_arg.split(',')
                new_value = next(ev([new_value]))
                instance_key = f"{arg1}.{new_id}"
                if instance_key in temp_d.keys():
                    setattr(temp_d[instance_key], new_key, new_value)
                    self.file_storage.save()
                else:
                    print("** aucune instance trouvée **")
            else:
                print("** attribut manquant **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
