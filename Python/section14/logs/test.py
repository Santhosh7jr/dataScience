from logger import logging

def add(a, b):
    logging.debug("adding two numbers")
    return a + b

print(add(5, 3))

