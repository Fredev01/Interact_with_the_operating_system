""" 
The module is for get the OS encironment
"""
import os
print(os.getcwd())
print(os.getenv("PATH"))
print(os.environ)
for environ in os.environ:
    print(environ)
for key, value in os.environ.items():
    print(key, value)
