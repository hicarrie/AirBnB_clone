#!/usr/bin/python3
"""
Module for init
"""


from models.engine.file_storage import FileStorage


""" creates storage and reloads """
storage = FileStorage()
FileStorage.reload(storage)
