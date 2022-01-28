<<<<<<< HEAD
#!/usr/bin/python
""" holds class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Representation of Place """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
=======
#!/usr/bin/python3
""" Places where host the user's """
from . base_model import BaseModel


class Place(BaseModel):
    """ Places where we offer our services """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
<<<<<<< HEAD

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
=======
>>>>>>> 5d10a342d89ab5775900c4d6b39a51e8a13a1f1b
