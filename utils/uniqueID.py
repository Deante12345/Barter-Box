import string
import random

def make_ID():
    made_id = ""
    for i in range (12):
        if (random.random() >= .5):
            made_id += str(random.randint(0,9))
        else:
            made_id += random.choice(string.ascii_letters)
    return made_id

def add_ID():
    temp_id = make_ID()
    while (temp_id in id_Dictionary.keys()):
        temp_id = make_ID()
    id_Dictionary.update({temp_id:"1"})

id_Dictionary = {}