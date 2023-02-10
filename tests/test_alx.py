#!/usr/bin/python3
# alx_test_base_model.py
# Author: @ALX
"""
This test function has been given by ALX.
The first lines have been modified due to path changing of the testing folder.
"""
from .. import models

BaseModel = __import__('models.base_model').BaseModel


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(
        key, type(my_model_json[key]), my_model_json[key]))
