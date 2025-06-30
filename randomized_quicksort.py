import time
import random

# Randomized quicksort where the pivot is chosen randomly
def randomized_quicksort(arr, low, high):
    if low < high:
        # Partition using a random pivot
        p = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)

def randomized_partition(arr, low, high):
    # Choose random pivot
    pivot_index = random.randint(low, high)
    # Swap with last
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def run_randomized_quicksort():
    # Different input sizes
    random_data = [random.randint(0, 100000) for _ in range(10000)]
    sorted_data = list(range(10000))
    reverse_sorted_data = list(range(9999, -1, -1))

    for label, data in [
        ("Random", random_data),
        ("Sorted", sorted_data),
        ("Reverse-Sorted", reverse_sorted_data)
    ]:
        test_array = data.copy()
        start = time.time()
        randomized_quicksort(test_array, 0, len(test_array) - 1)
        end = time.time()
        print(f"{label} input sorted in {end - start:.6f} seconds")

if __name__ == "__main__":
    run_randomized_quicksort()
