import timeit

def time(func: callable, *args: any, **kwargs: any) -> float:
    sum = 0
    for _ in range(10):
        sum += timeit.timeit(lambda: func(*args, **kwargs), number=1)
    return sum / 10

def time_all(funcs: list[callable], *args: any, **kwargs: any) -> dict:
    return {func.__name__: time(func, *args, **kwargs) for func in funcs}
