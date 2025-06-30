import time
import random

def quicksort(arr, low, high):
    if low < high:
        # Partition the array and get pivot index
        p = partition(arr, low, high)
        # Recursively sort the left and right subarrays
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

def partition(arr, low, high):
    mid = (low + high) // 2
    arr[high], arr[mid] = arr[mid], arr[high]  # Use middle element as pivot
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i



def run_quicksort():
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
        quicksort(test_array, 0, len(test_array) - 1)
        end = time.time()
        print(f"{label} input sorted in {end - start:.6f} seconds")

if __name__ == "__main__":
    run_quicksort()
