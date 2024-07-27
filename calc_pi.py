import random
import time
import threading

def compute_pi_part(num_points, result, index):
    count_inside_circle = 0

    for _ in range(num_points):
        x, y = random.uniform(0, 1), random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            count_inside_circle += 1

    result[index] = count_inside_circle

def approximate_pi(total_points, num_threads):
    threads = []
    results = [0] * num_threads
    points_per_thread = total_points // num_threads

    for i in range(num_threads):
        start = i * points_per_thread
        end = (i + 1) * points_per_thread

        if i == num_threads - 1:
            end = total_points

        thread = threading.Thread(target=compute_pi_part, args=(end - start, results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_inside_circle = sum(results)
    pi_approximation = 4 * total_inside_circle / total_points
    return pi_approximation

if __name__ == '__main__':
    total_points = int(input('Enter the number of points: '))
    num_threads = int(input('Enter the number of threads: '))

    start_time = time.time()
    pi_value = approximate_pi(total_points, num_threads)
    end_time = time.time()

    print(f'\nApproximated value of π with {total_points} points: {pi_value}')
    print(f'\nExecution time: {end_time - start_time} seconds')
