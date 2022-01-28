<<<<<<< HEAD
#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """Representation of city """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
=======
#!/user/bin/python3
""" City where user's come from """
from . base_model import BaseModel


class City(BaseModel):
    """ city of the user """
    state_id = ''
    name = ''
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
