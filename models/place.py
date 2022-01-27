#!/usr/bin/python3
""" Places where host the user's """
from . base_model import BaseModel


class Place(BaseModel):
    """ Places where we offer our services """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
