#!/usr/bin/python3
"""
Ce module active l'interface en ligne de commande Python
"""
import json
import cmd
import sys
import shlex
from models.engine.file_storage import FileStorage

# Use a dictionary to map class names to class objects
CLASSES = {
    'BaseModel': BaseModel,
    'Place': Place,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Review': Review,
    'User': User,
}

def load_instance(arg2):
    """Load instance from storage based on class name and id"""
    storage = FileStorage()
    storage.reload()
    tempD = storage.all()
    y = f"{arg2[0]}.{arg2[1]}"
    return tempD.get(y)

def print_error(message):
    """Print error message"""
    print(f"** {message} **")

class HBNBCommand(cmd.Cmd):
    """Interface en ligne de commande pour le clone AirBnB"""
    prompt = '(hbnb) '

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
        if not arg2:
            print_error("nom de classe manquant")
            return
        class_name = arg2[0]
        if class_name not in CLASSES:
            print_error("la classe n'existe pas")
            return

        model = CLASSES[class_name]()
        model.save()
        print(model.id)

    def do_show(self, args):
        """Affiche la représentation en chaîne d'une instance"""
        arg2 = shlex.split(args)
        if len(arg2) < 2:
            print_error("nom de classe ou identifiant d'instance manquant")
            return
        class_name, instance_id = arg2[0], arg2[1]
        if class_name not in CLASSES:
            print_error("la classe n'existe pas")
            return

        instance = load_instance(arg2)
        if instance:
            print(instance)
        else:
            print_error("aucune instance trouvée")

    def do_destroy(self, args):
        """Supprime une instance en fonction du nom de la classe et de l'identifiant"""
        arg2 = shlex.split(args)
        if len(arg2) < 2:
            print_error("nom de classe ou identifiant d'instance manquant")
            return
        class_name, instance_id = arg2[0], arg2[1]
        if class_name not in CLASSES:
            print_error("la classe n'existe pas")
            return

        instance = load_instance(arg2)
        if instance:
            del storage.all()[f"{class_name}.{instance_id}"]
            storage.save()
        else:
            print_error("aucune instance trouvée")

    def do_all(self, args):
        """Crée une nouvelle instance d'une classe"""
        arg2 = shlex.split(args)
        if arg2 and arg2[0] not in CLASSES:
            print_error("la classe n'existe pas")
            return

        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        instances = [str(obj) for obj in tempD.values() if not arg2 or arg2[0] in str(obj)]
        print(instances)

    def do_update(self, args):
        """Met à jour une instance en fonction du nom de la classe et de l'identifiant en ajoutant
        ou en mettant à jour l'attribut"""
        arg2 = shlex.split(args)
        if len(arg2) < 4:
            print_error("arguments insuffisants")
            return
        class_name, instance_id, attribute_name, value = arg2[0], arg2[1], arg2[2], arg2[3]
        if class_name not in CLASSES:
            print_error("la classe n'existe pas")
            return

        instance = load_instance(arg2)
        if not instance:
            print_error("aucune instance trouvée")
            return

        setattr(instance, attribute_name, json.loads(value))
        instance.save()
        storage.save()

    def emptyline(self):
        pass
        return

    def default(self, args):
        """Gère les autres commandes"""
        args = shlex.split(args)
        try:
            class_name, command = args[0].split('.')
            if len(args) > 1:
                command += ''.join(args[1:])
        except Exception:
            print_error("commande invalide")
            return

        if class_name not in CLASSES:
            print_error("la classe n'existe pas")
            return

        storage = FileStorage()
        storage.reload()
        tempD = storage.all()
        new_list = [str(value) for key, value in tempD.items() if class_name in key]

        if command == "all()":
            print(new_list)
        elif command == "count()":
            print(len(new_list))
        elif "show" in command:
            new_id = check_arg(command, "show")
            if not new_id:
                return
            for items in new_list:
                if new_id in items:
                    print(items)
                    return
            print_error("aucune instance trouvée")
        elif "destroy" in command:
            new_id = check_arg(command, "destroy")
            if not new_id:
                return
            y = f"{class_name}.{new_id}"
            if y in tempD.keys():
                del tempD[y]
                storage.save()
            else:
                print_error("aucune instance trouvée")
        elif "update" in command:
            new_arg = check_arg(command, "update")
            if not new_arg:
                return
            if '{' in new_arg:
                try:
                    new_list = list(new_arg.split('{'))
                except Exception:
                    print_error("arguments invalides")
                    return
                new_id = new_list[0].replace(',', '')
                new_dict = new_list[1].replace('}', '')
                new_list = list(new_dict.split(','))
                y = f"{class_name}.{new_id}"

                if y in tempD.keys():
                    for item in new_list:
                        try:
                            attribute, val = item.split(':')
                            setattr(tempD[y], attribute, json.loads(val))
                        except Exception:
                            print_error("nom d'attribut manquant")
                            return
                    tempD[y].save()
                    storage.save()
                else:
                    print_error("aucune instance trouvée")
            elif len(args) == 3:
                new_id, new_key, new_value = new_arg.split(',')
                y = f"{class_name}.{new_id}"
                if y in tempD.keys():
                    setattr(tempD[y], new_key, json.loads(new_value))
                    storage.save()
                else:
                    print_error("aucune instance trouvée")
            else:
                print_error("attribut manquant")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

