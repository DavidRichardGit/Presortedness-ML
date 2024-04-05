def quicksort(A):
    comparisons = [0]
    quickSorter(A, 0, len(A) - 1, comparisons)
    return comparisons[0]

def partition(A, low, high, comparisons):
    pivot = A[high]
    i = low - 1
    for j in range(low, high):
        comparisons[0] += 1
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

def quickSorter(A, low, high, comparisons):
    if low < high:
        pi = partition(A, low, high, comparisons)
        quickSorter(A, low, pi - 1, comparisons)
        quickSorter(A, pi + 1, high, comparisons)
