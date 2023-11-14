#!/usr/bin/python3
"""crée une instance FileStorage unique pour votre application"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
