#Everyday Test
import sys

def open_file(file_name, mode):
    """Open file"""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
        