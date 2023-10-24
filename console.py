#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}
    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            if key == "password":
                json_objects[key].decode()
            json_objects[key] = self.__objects[key].to_dict(save_fs=1)
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
    def delete(self, obj=None):
        """delete obj from __objects if it's inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value
        return None
    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()
        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())
        return count







Courtney Alvarado
  10:27 PM
#!/usr/bin/python3
"""New class inherit from cmd"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Consol for safe database."""

    prompt = '(hbnb)'

    __list_class = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    ]

    def do_create(self, line):
        """Create classes"""
        if self.check_class_name(line):
            try:
                new = eval(line + "()")
                new.save()
                print(new.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Show instances"""
        key = self.found_class_name(line)
        if key is not None:
            all_objs = storage.all()
            try:
                obj = all_objs[key]
                print(obj)
            except Exception:
                print("** no instance found **")

    def do_destroy(self, line):
        """Destroy instances"""
        key = self.found_class_name(line)
        if key is not None:
            all_objs = storage.all()
            try:
                all_objs.pop(key)
                storage.save()
            except Exception:
                print("** no instance found **")

    def do_all(self, line):
        """Show all instnaces"""
        new_list = []
        match = True
        args = shlex.split(line)
        all_objs = storage.all()
        if len(line) != 0:
            if args[0] in HBNBCommand.__list_class:
                for key, value in all_objs.items():
                    if line == key.split('.')[0]:
                        obj = all_objs[key]
                        new_list.append(obj.__str__())
            else:
                print("** class doesn't exist **")
                match = False

        else:
            for key, value in all_objs.items():
                obj = all_objs[key]
                new_list.append(obj.__str__())
        if match:
            print(new_list)

    def do_update(self, line):
        """Update console"""
        key = self.found_class_name(line)
        if key is not None:
            args = shlex.split(line)
            all_objs = storage.all()
            if key in all_objs.keys():
                if len(args) == 2:
                    print("** attribute name missing **")
                elif len(args) == 3:
                    print("** value missing **")
                else:
                    if args[3][0] and args[3][-1] != '"':
                        try:
                            args[3] = int(args[3])
                        except ValueError:
                            try:
                                args[3] = float(args[3])
                            except ValueError:
                                pass

                    obj = all_objs[key]
                    obj.__dict__.update({args[2]: args[3]})
                    setattr(obj, args[2], type(
                        getattr(obj, args[2], args[3]))(args[3]))
                    obj.save()
            else:
                print("** no instance found **")

    def do_EOF(self, line):
        """Signal C+d for exit."""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """Overwrite method emptyline."""
        pass

    def check_class_name(self, name=""):
        """Check if stdin user typed class name and id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Check class id"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__list_class:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
            else:
                print("** class doesn't exist **")
        return None

    def precmd(self, line):
        args = line.split('.')
        if len(args) >= 2:
            if args[1].count('()') == 1:
                clas_name = args[0]
                a = args[1].replace('(', '.')
                b = a.replace(')', '.')
                c = b.split('.')
                comand = c[0]
            # print(clas_name)
            # print(comand)
            # print(argvs)
                line = str(comand + ' ' + clas_name)
            elif args[1].count('(') == 1 and args[1].count(')') == 1:
                arguments = ""
                clas_name = args[0]
                a = args[1].replace('(', '.')
                b = a.replace(')', '.')
                c = b.split('.')
                comand = c[0]
                argvs = shlex.split(c[1], '"')
                for wrd in argvs:
                    arguments = arguments + wrd

                d = str(comand + ' ' + clas_name + ' ' + arguments)
                line = d.replace(',', ' ')
                print(line)

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
