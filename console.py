#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime

"""module: console.py"""


class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class"""

    prompt = '(hbnb) '
    file = None

    @classmethod
    def get_instanceCount(self, clsname=""):
        obj = storage.all()
        count = 0
        for k in obj.keys():
            obj_cls = (obj[k].__class__.__name__)
            if (obj_cls == clsname):
                count += 1
        return count

    def do_EOF(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        raise SystemExit

    def do_create(self, args):
        """Creates a new instance: format - create <classname>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if s[0] is None:
                print("** class name missing **")
            else:
                cls_chk = check_class(s[0])
                if cls_chk is not None:
                    inst = cls_chk()
                    inst.save()
                    print(inst.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, args):
        """Show information of an instance: format - show <classname> <id>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()

            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except Exception:
                print("** instance id missing **")
            else:
                cls_chk = check_class(s[0])
                if cls_chk is not None:
                    obj = storage.all()
                    key = str(s[0]) + '.' + str(s[1])
                    try:
                        print(obj[key])
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_destroy(self, args):
        """Destroys an instance: format - destroy <classname> <id>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if not s[0]:
                print("** class name missing **")

            try:
                s[1]
            except:
                print("** instance id missing **")
            else:
                cls_chk = check_class(s[0])
                if cls_chk is not None:
                    obj = storage.all()
                    key = str(s[0]) + '.' + str(s[1])
                    try:
                        del obj[key]
                        storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all instances in str format based on
        classname or not:\nformat(1) - all\nformat(2) all <classname>\n"""
        s = args.split()
        obj = storage.all()
        count = 0
        try:
            s[0]
            cls_chk = check_class(s[0])
            if cls_chk is None:
                print("** class doesn't exist **")
            for k in obj.keys():
                obj_cls = (obj[k].__class__.__name__)
                if (obj_cls == s[0]):
                    print(obj[k])
                    count = count + 1
            if count == 0 and cls_chk is not None:
                print([])
        except:
            for k in obj.keys():
                print(obj[k])
                count = count + 1
            if count == 0:
                print([])

    def do_update(self, args):
        """Updates the key/value pair of an instance\nformat
        - update <class> <id> <key> <value>\n"""
        if not args:
            print("** class name missing **")
        else:
            s = args.split()
            if not s[0]:
                print("** class name missing **")
            try:
                s[1]
            except:
                print("** instance id missing **")
            try:
                s[2]
            except:
                print("** attribute name missing **")
            try:
                s[3]
            except:
                print("** value missing **")
            else:
                cls_chk = check_class(s[0])
                if cls_chk is not None:
                    obj = storage.all()
                    key = str(s[0]) + '.' + str(s[1])
                    try:
                        if s[3].isdigit():
                            s[3] = int(s[3])
                        else:
                            s[3] = s[3].replace('"', '')
                        setattr(obj[key], s[2], s[3])
                        setattr(obj[key], "updated_at", datetime.now())
                        storage.save()
                    except:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")

    def do_BaseModel(self, args):
        """(1): BaseModel.all()\n(2): BaseModel.count()\n
        (3): BaseModel.show(<id>)\n(4): BaseModel.destroy(<id>)\n"""
        if args == '.all()':
            self.do_all("BaseModel")
        elif args == '.count()':
            print(self.get_instanceCount("BaseModel"))
        elif args[0:5] == '.show':
            arg = 'BaseModel' + ' ' + args[7:-2]
            self.do_show(arg)
        elif args[0:8] == '.destroy':
            arg = "BaseModel" + ' ' + args[10:-2]
            self.do_destroy(arg)
        elif args[0:7] == '.update':
            ret = build_updatearg(args[8:-1])
            arg = "BaseModel" + ' ' + ret
            self.do_update(arg)

    def do_User(self, args):
        """(1): User.all()\n(2): User.count()\n(3): User.show(<id>)\n
        (4): User.destroy(<id>)\n"""
        if args == '.all()':
            self.do_all("User")
        elif args == '.count()':
            print(self.get_instanceCount("User"))
        elif args[0:5] == '.show':
            arg = 'User' + ' ' + args[7:-2]
            self.do_show(arg)
        elif args[0:8] == '.destroy':
            arg = "User" + ' ' + args[10:-2]
            self.do_destroy(arg)
        elif args[0:7] == '.update':
            ret = build_updatearg(args[8:-1])
            arg = "User" + ' ' + ret
            self.do_update(arg)

    def do_State(self, args):
        """(1): State.all()\n(2): State.count()\n(3): State.show(<id>)\n
        (4): State.destroy(<id>)\n"""
        if args == '.all()':
            self.do_all("State")
        elif args == '.count()':
            print(self.get_instanceCount("State"))
        elif args[0:5] == '.show':
            arg = 'State' + ' ' + args[7:-2]
            self.do_show(arg)
        elif args[0:8] == '.destroy':
            arg = "State" + ' ' + args[10:-2]
            self.do_destroy(arg)
        elif args[0:7] == '.update':
            ret = build_updatearg(args[8:-1])
            arg = "State" + ' ' + ret
            self.do_update(arg)

    def do_City(self, args):
        """(1): City.all()\n(2): City.count()\n(3): City.show(<id>)\n
        (4): City.destroy(<id>)\n"""
        if args == '.all()':
            self.do_all("City")
        elif args == '.count()':
            print(self.get_instanceCount("City"))
        elif args[0:5] == '.show':
            arg = 'City' + ' ' + args[7:-2]
            self.do_show(arg)
        elif args[0:8] == '.destroy':
            arg = "City" + ' ' + args[10:-2]
            self.do_destroy(arg)
        elif args[0:7] == '.update':
            ret = build_updatearg(args[8:-1])
            arg = "City" + ' ' + ret
            self.do_update(arg)

    def do_Place(self, args):
        """(1): Place.all()\n(2): Place.count()\n(3): Place.show(<id>)\n
        (4): Place.destroy(<id>)\n"""
        if args == '.all()':
            self.do_all("Place")
        elif args == '.count()':
            print(self.get_instanceCount("Place"))
        elif args[0:5] == '.show':
            arg = 'Place' + ' ' + args[7:-2]
            self.do_show(arg)
        elif args[0:8] == '.destroy':
            arg = "Place" + ' ' + args[10:-2]
            self.do_destroy(arg)
        elif args[0:7] == '.update':
            ret = build_updatearg(args[8:-1])
            arg = "Place" + ' ' + ret
            self.do_update(arg)

    def do_Amenity(self, args):
        """(1): Amenity.all()\n(2): Amenity.count()\n
        (3): Amenity.show(<id>)\n(4): Amenity.destroy(<id>)\n"""
        if args == '.all()':
            self.do_all("Amenity")
        elif args == '.count()':
            print(self.get_instanceCount("Amenity"))
        elif args[0:5] == '.show':
            arg = 'Amenity' + ' ' + args[7:-2]
            self.do_show(arg)
        elif args[0:8] == '.destroy':
            arg = "Amenity" + ' ' + args[10:-2]
            self.do_destroy(arg)
        elif args[0:7] == '.update':
            ret = build_updatearg(args[8:-1])
            arg = "Amenity" + ' ' + ret
            self.do_update(arg)

    def do_Review(self, args):
        """(1): Review.all()\n(2): Review.count()\n(3): Review.show(<id>)\n
        (4): Review.destroy(<id>)\n"""
        if args == '.all()':
            self.do_all("Review")
        elif args == '.count()':
            print(self.get_instanceCount("Review"))
        elif args[0:5] == '.show':
            arg = 'Review' + ' ' + args[7:-2]
            self.do_show(arg)
        elif args[0:8] == '.destroy':
            arg = "Review" + ' ' + args[10:-2]
            self.do_destroy(arg)
        elif args[0:7] == '.update':
            ret = build_updatearg(args[8:-1])
            arg = "Review" + ' ' + ret
            self.do_update(arg)

    def emptyline(self):
        pass


def build_updatearg(arg):
    """builds out the string for Classname.update"""
    s = arg.split()
    s01 = s[0].replace('"', "")
    a = s01.replace(',', "")
    atr = s[1].replace('"', '')
    atr = atr.replace(',', '')
    val = s[2].replace('"', '')
    val = val.replace(',', '')
    retval = a + ' ' + atr + ' ' + val
    return retval


def check_class(classname):
    """checks is user's class input is valid"""
    classes = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'User': User, 'Amenity': Amenity, 'Review': Review,
               'Place': Place}
    for k, v in classes.items():
        if classname == k:
            return v
    else:
        return None

if __name__ == '__main__':
    HBNBCommand().cmdloop()
