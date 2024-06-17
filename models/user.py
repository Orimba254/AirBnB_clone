#!/usr/bin/python3
"""Module that defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """A User class having various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
