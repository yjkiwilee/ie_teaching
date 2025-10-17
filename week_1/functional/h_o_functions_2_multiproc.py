from multiprocessing import Pool, Process, Queue
from functools import reduce
import time

def operation(x):
    return x**2

def map_normal(l):
    return reduce(
        lambda a, b: a + b,
        map(
            operation,
            l
        )
    )

def map_normal_queue(l, q):
    q.put(reduce(
        lambda a, b: a + b,
        map(
            operation,
            l
        )
    ))

def map_pool(l, n_processes):
    result = None

    with Pool(n_processes) as pool:
        # Function has to be pickleable
        result = pool.map(
            operation,
            l
        )
    
    return reduce(
        lambda a, b: a + b,
        result
    )

def map_process(l, n_processes):
    q = Queue()

    len_l = len(l)
    split_idx = [i * (len_l // n_processes) for i in range(n_processes)]
    split_idx.append(len_l)

    split_l = [
        l[split_idx[i]:split_idx[i+1]]
        for i in range(len(split_idx) - 1)
    ]

    processes = []

    # Start processes
    for l_part in split_l:
        processes.append(
            Process(target=map_normal_queue, args=(l_part,q,), daemon=True)
        )
        processes[-1].start()
    
    # Join processes
    for p in processes:
        p.join()

    # Insert sentinel
    q.put(None)
    
    # Calculate sum
    result = 0
    for part_sum in iter(lambda: q.get(timeout=0.00001), None):
        result += part_sum
    
    return result

if __name__ == '__main__':
    n = 20000000

    curr = time.time()
    result = map_normal(range(n))
    elapsed = time.time() - curr
    print(f"Normal algorithm took {elapsed} seconds, with output {result}")

    curr = time.time()
    result = map_process(range(n), 3)
    elapsed = time.time() - curr
    print(f"Multi-threaded algorithm took {elapsed} seconds, with output {result}")