import math

def introsort(arr):

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def insertion_sort(arr, low, high):
        for i in range(low + 1, high + 1):
            key = arr[i]
            j = i - 1
            comparisons[0] += 1
            while j >= low and arr[j] > key:
                comparisons[0] += 1
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def heap_sort(arr):
        def heapify(arr, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and arr[i] < arr[l]:
                largest = l

            if r < n and arr[largest] < arr[r]:
                largest = r

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)

        n = len(arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

    def introsort_util(arr, low, high, depth_limit):
        size = high - low + 1

        if size < 16:
            insertion_sort(arr, low, high)
            return

        if depth_limit == 0:
            heap_sort(arr)
            return

        pivot = partition(arr, low, high)

        introsort_util(arr, low, pivot - 1, depth_limit - 1)
        introsort_util(arr, pivot + 1, high, depth_limit - 1)

    comparisons = [0]
    introsort_util(arr, 0, len(arr) - 1, 2 * math.log(len(arr)))
    return comparisons[0]
