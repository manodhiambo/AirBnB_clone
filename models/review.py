#!/usr/bin/python3
""" review of user's when left the place """
from . base_model import BaseModel


class Review(BaseModel):
    """ review of the user (qualification)"""
    place_id = ''
    user_id = ''
    text = ''
