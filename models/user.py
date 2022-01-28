<<<<<<< HEAD
#!/usr/bin/python
""" holds class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
""" First User in ABNB project """
from . base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
