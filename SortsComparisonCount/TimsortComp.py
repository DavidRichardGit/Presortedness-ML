MINIMUM = 32
global comparisons
def find_minrun(n): 
    r = 0
    while n >= MINIMUM: 
        r |= n & 1
        n >>= 1
    return n + r 

def tim_insertion_sort(array, left, right): 
    global comparisons
    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1
        comparisons += 1
        while j >= left and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            comparisons += 1
        array[j + 1] = key
    return array
              
def tim_merge(array, l, m, r): 
    global comparisons
    array_length1 = m - l + 1
    array_length2 = r - m 
    left = []
    right = []
    for i in range(array_length1): 
        left.append(array[l + i]) 
    for i in range(array_length2): 
        right.append(array[m + 1 + i]) 
  
    i = 0
    j = 0
    k = l
   
    while j < array_length2 and i < array_length1: 
        if left[i] <= right[j]: 
            array[k] = left[i] 
            i += 1
        else: 
            array[k] = right[j] 
            j += 1
        k += 1
        comparisons += 1
  
    while i < array_length1: 
        array[k] = left[i] 
        k += 1
        i += 1
        comparisons += 1
  
    while j < array_length2: 
        array[k] = right[j] 
        k += 1
        j += 1
        comparisons += 1
  
def timsort(array): 
    n = len(array) 
    minrun = find_minrun(n) 
  
    for start in range(0, n, minrun): 
        end = min(start + minrun - 1, n - 1) 
        tim_insertion_sort(array, start, end) 
   
    size = minrun 
    while size < n: 
        for left in range(0, n, 2 * size): 
            mid = min(n - 1, left + size - 1) 
            right = min((left + 2 * size - 1), (n - 1)) 
            tim_merge(array, left, mid, right) 
        size = 2 * size

    return comparisons
