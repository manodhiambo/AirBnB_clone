<<<<<<< HEAD
#!/usr/bin/python
""" holds class State"""
from models.base_model import BaseModel


class State(BaseModel):
    """Representation of state """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
""" State where user's come from """
from . base_model import BaseModel


class State(BaseModel):
    """ Define the state of the user """
    name = ''
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
