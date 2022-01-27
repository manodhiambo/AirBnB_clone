#!/user/bin/python3
""" City where user's come from """
from . base_model import BaseModel


class City(BaseModel):
    """ city of the user """
    state_id = ''
    name = ''
