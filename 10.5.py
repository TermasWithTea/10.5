from multiprocessing import Pool
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]


start_time = time.time()
for filename in filenames:
    read_info(filename)
print(f"Линейный вызов занял {time.time() - start_time:.2f} секунд")

start_time = time.time()

if __name__ == '__main__':
    with Pool(processes = 4) as pool:
     pool.map(read_info, filenames)
    print(f"Многопроцессный вызов занял {time.time() - start_time:.2f} секунд")







