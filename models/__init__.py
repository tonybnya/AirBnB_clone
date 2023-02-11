#!/usr/bin/python3
"""
Special magic file for the models package.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
