import time
import logging
import datetime
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="a")
def time_decorator(func):
    curtime = datetime.datetime.now()
    logging.info(f"time_decorator is started with {func.__name__}. Current time: {curtime}")
    def inner(*args, **kargs):
        tok = time.time()
        func(*args, **kargs)
        tik = time.time()
        print(f"{func.__name__}'s executing time is {tik - tok}")
    return inner
def time_decorator_with_return(func):
    curtime = datetime.datetime.now()
    logging.info(f"time_decorator_with_return is started with {func.__name__}. Current time: {curtime}")
    def inner(*args, **kargs):
        tok = time.time()
        ans = func(*args, **kargs)
        tik = time.time()
        print(f"{func.__name__}'s executing time is {tik - tok}")
        return ans
    return inner
