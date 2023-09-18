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
