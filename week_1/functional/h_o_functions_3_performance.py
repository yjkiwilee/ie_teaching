import time

def timed(f):
    def inner(*args, **kwargs):
        s = time.process_time_ns()
        result = f(*args, **kwargs)
        e = time.process_time_ns()
        print(f"Function executed in {(e - s) / (1e9)} seconds")
        return result
    
    return inner

@timed
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

measure_me(10)