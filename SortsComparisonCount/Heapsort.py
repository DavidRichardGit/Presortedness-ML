# has to be repaired

def heapify(A, n, i, comparisons):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and A[l] > A[largest]:
        largest = l
        comparisons[0] += 1

    if r < n and A[r] > A[largest]:
        largest = r
        comparisons[0] += 1

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest, comparisons)

def heap_sort(A):
    comparisons = [0]
    n = len(A)

    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i, comparisons)

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0, comparisons)

    return comparisons[0]
