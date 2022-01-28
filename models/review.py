<<<<<<< HEAD
#!/usr/bin/python
""" holds class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of Review """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
=======
#!/usr/bin/python3
""" review of user's when left the place """
from . base_model import BaseModel


class Review(BaseModel):
    """ review of the user (qualification)"""
    place_id = ''
    user_id = ''
    text = ''
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
