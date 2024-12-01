import random
import time
from multiprocessing import Pool

workers = 12
DATA_SIZE = 10_000_000

def fill_data(n):
    return [random.randint(1, 100) for _ in range(n)]

class Timer:
    def __init__(self, message="Elapsed: {}s"):
        self.message = message

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = time.time() - self.start_time
        print(self.message.format(elapsed_time))

if __name__ == "__main__":
    with Timer("Elapsed: {}s"):
        with Pool(workers) as pool:
            input_data = [DATA_SIZE // workers for _ in range(workers)]
            result = pool.map(fill_data, input_data)

    lst = [item for sublist in result for item in sublist]

    print(len(lst), lst[:100])
