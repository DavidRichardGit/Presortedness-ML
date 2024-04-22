def inv_dis(arr):
    c_max_dist = 0
    inv = 0
    
    for key in range(len(arr)):
        for j in range(key):
            if arr[key] < arr[j]:
                c_max_dist = max(key-j,c_max_dist)
                inv += 1

    return inv, c_max_dist
