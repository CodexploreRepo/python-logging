import logging

import module_a
from utils import MyLogger

logger = MyLogger(name=__name__)
logger.setLevel(logging.DEBUG)
logger.debug("This is debug from main")
logger.info("This is info from main")

def divide_func(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception(f"Cannot divide x={x} with y={y}")
    else:
        return result
divide_func(10,0)