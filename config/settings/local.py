from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='y^_#cy-aikn0_idwz&a+!9dyerjbt#wu-t(=qui+%7gq3ts8mx')
DEBUG = env.bool('DJANGO_DEBUG', True)
