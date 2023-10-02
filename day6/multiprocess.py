import multiprocessing

def square_numbers(numbers):
    for num in numbers:
        print(f"Square of {num}: {num*num}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    process = multiprocessing.Process(target=square_numbers, args=(numbers,))
    process.start()
    process.join()
