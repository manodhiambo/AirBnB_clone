#!/usr/bin/python3
""" First User in ABNB project """
from . base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
