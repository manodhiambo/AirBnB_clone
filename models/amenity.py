<<<<<<< HEAD
#!/usr/bin/python
""" holds class Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Representation of Amenity """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
""" The amenities of place """
from . base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity (Comodidades) """
    name = ''
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
