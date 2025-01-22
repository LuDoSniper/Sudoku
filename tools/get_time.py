import time

def get_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    
    execution_time = end_time - start_time
    return result, execution_time