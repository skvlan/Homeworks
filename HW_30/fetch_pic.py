import os
import random
import string
import requests
import time

from multiprocess.pool import ThreadPool


def fetch_pic(num_pic):
    url = 'https://picsum.photos/400/600'
    path = os.path.join(os.getcwd(), 'img')
    for _ in range(num_pic):
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
        response = requests.get(url)
        if response.status_code == 200:
            with open(f'{path}/{random_name}.jpg', 'wb') as f:
                f.write(response.content)
                print(f"Fetched pic [{os.getpid()}]: {f.name}" )

workers = 72
DATA_SIZE = 100


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
        with ThreadPool(workers) as pool:
            input_data = [DATA_SIZE // workers for _ in range(workers)]
            pool.map(fetch_pic, input_data)
