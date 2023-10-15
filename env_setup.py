import os
import json

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(ROOT_PATH, "credentials.json")

with open(path, 'r') as f:
    secret = json.load(f)

LOGIN = secret['login']
PASSWORD = secret['password']



