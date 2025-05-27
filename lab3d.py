#!/usr/bin/env python3
#AuthorID: salakoozi

import os

def free_space():
    result = os.popen("df -h | grep '/$' | awk '{print $4}'").read()
    return result.strip()

print(free_space())
