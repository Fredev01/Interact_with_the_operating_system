""" 
This module is for count the extension of the files 
"""
import os
from collections import Counter
counts = Counter()
pwd: str = os.getcwd()
print(pwd)
for currentdir, dirnames, filenames in os.walk('.'):
    for filename in filenames:
        first_part, extension = os.path.splitext(filename)
        counts[extension] += 1

for extension, count in counts.items():
    print(f"{extension:8}{count}")
