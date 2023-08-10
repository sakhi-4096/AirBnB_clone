#!/usr/bin/python3

import uuid
import datetime

class BaseModel:
    """
    Added a docstring for demo purposes
    """

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid.uuid4())
        self.created_at = 
        self.updated_at = updated_at
