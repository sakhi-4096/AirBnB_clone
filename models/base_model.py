#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    """
    Added a docstring for demo purposes
    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dict_instances = self.__dict__.copy()
        dict_instances['__class__'] = self.__class__.__name__
        dict_instances['created_at'] = self.created_at.isoformat()
        dict_instances['updated_at'] = self.updated_at.isoformat()

        return dict_instances
