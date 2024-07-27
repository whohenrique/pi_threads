import random
import threading
import time

def sum_of_squares(start, end, thread_id, result):
    partial_sum = 0
    for i in range(start, end):
        partial_sum += vector[i] ** 2
    result[thread_id] = partial_sum

if __name__ == "__main__":
    vector_size = int(input('Enter the size of the vector: '))
    thread_size = int(input('Enter the number of threads: '))

    vector = [random.randint(1, 1000) for _ in range(vector_size)]
    
    results = [0] * thread_size
    threads = []

    for i in range(thread_size):
        start = i * (vector_size // thread_size)
        end = (i + 1) * (vector_size // thread_size)
        
        if i == thread_size - 1:
            end = vector_size

        thread = threading.Thread(target=sum_of_squares, args=(start, end, i, results))
        threads.append(thread)

    print('\nStarting the threads')
    start_time = time.time()

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()
    execution_time_thread = end_time - start_time
    total_thread_sum = sum(results)

    print("\nTime with threads: {:.6f} seconds".format(execution_time_thread))
    print("Sum of squares by each thread: ", results)
    print("Total sum of squares (threads): ", total_thread_sum)

    print("\nStarting sequential sum")
    start_time = time.time()
    total_sequential_sum = sum(x ** 2 for x in vector)
    end_time = time.time()
    execution_time_sequential = end_time - start_time

    print("\nSequential time: {:.6f} seconds".format(execution_time_sequential))
    print("Total sum of squares (sequential): ", total_sequential_sum)
