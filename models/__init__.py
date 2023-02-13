#!/usr/bin/python3
"""
Special magic file for the models package.
"""
# from models.engine.file_storage import FileStorage

# storage = FileStorage()
# storage.reload()
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
