#!/usr/bin/python3
import json

class Base:
    """the base of class"""
    __nb_objects = 0


    def __init__(self, id=None):
        """this is the constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json strin representation of list"""
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = "{}.json".format(class_name)
        obj_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode="w") as f:
            f.write(cls.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            json_string = []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """another instance"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")
        dummy_instance.update(**dictionary)
        return dummy_instance
