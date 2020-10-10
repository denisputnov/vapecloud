import os

from django.test import TestCase

test =  os.path.dirname(os.path.abspath(__file__))
command = f"python {test}\manage.py search_index --rebuild"
os.system(command)
