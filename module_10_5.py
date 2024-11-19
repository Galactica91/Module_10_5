import time
from multiprocessing import Pool
import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]


start_time = time.time()
for filename in filenames:
    read_info(filename)
end_time = time.time()
linear_duration = end_time - start_time
print(f"{linear_duration} (линейный)")

if __name__ == '__main__':
    start2 = datetime.now()

    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    multiprocessing_duration = end_time - start_time
    print(f"{multiprocessing_duration} (многопроцессный)")