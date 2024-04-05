def insertion_sort(A):
    comparisons = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and A[j] > key:
            comparisons += 1
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return comparisons
