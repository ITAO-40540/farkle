from db.base import *
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy import event


class Player:

    # __init__() gets executed when Player() is called
    # not necessary to include but very useful in most cases
    def __init__(self, first_name, age=None):
        # self is a hook into the object created. It's how you add attributes
        self.first_name = first_name
        # the `_` signifies that the attribute should be treated as private
        self._age = age

    # these are functions that are hooked into the object but their structure is a plain old function
    def age(self):
        return self._age

    def full_name(self):
        return self.first_name

