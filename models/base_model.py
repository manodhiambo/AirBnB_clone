#!/usr/bin/python3
<<<<<<< HEAD
"""
Contains class BaseModel
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
=======


""" Base module """
import uuid
from datetime import datetime
# import the variable storage
import models


class BaseModel:
    """ class for all other classes to inherit from """
    def __init__(self, *args, **kwargs):
        """ Constructor and re-create an instance with
        this dictionary representation"""
        if len(kwargs) > 0:
            # each key of this dictionary is an attribute name
            # each value of this dictionary is the value of this attribute name
            for key, value in kwargs.items():
                if key == "updated_at":
                    # Convert string date to datetime object
                    # strptime (string parse time): Parse a string into a -
                    # datetime object given a corresponding format
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    # This happens because __class__ is not mandatory in output
                    continue

                setattr(self, key, value)
        else:
            # Generate a random UUID
            self.id = str(uuid.uuid4())
            # assign with the current datetime when an instance is created
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # if it’s a new instance add a call to the method new(self) on stge
            models.storage.new(self)

    def __str__(self):
        """ overriding the __str__ method that returns a custom
        string object """
        # Old-style: self.__class__.__name__
        class_name = type(self).__name__
        mssg = "[{0}] ({1}) {2}".format(class_name, self.id, self.__dict__)
        return (mssg)

    # Public instance methods
    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime """
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
=======
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        # Define a dictionary and key __class__ that add to this dictionary
        # with the class name of the object
        tdic = {}
        tdic["__class__"] = type(self).__name__
        # loop over dict items and validate created_at and updated_at to
        # convert in ISO format
        for n, i in self.__dict__.items():
            if isinstance(i, datetime):
                tdic[n] = i.isoformat()
            else:
                tdic[n] = i
        return (tdic)
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
