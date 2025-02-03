from multiprocessing import Process
import time
'''
Here, we're looking at processes! Prcoesses are seperate 
areas of memory, whereas threads share memory.
'''

def calculate_square(numbers):
    for number in numbers:
        print(f"Square of {number} is {number * number}")
        time.sleep(1)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    processes = []

    # Create 2 processes and split the work!
    for i in range(2):
        p = Process(target=calculate_square, args=(numbers[i::2],))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All calculations complete!")