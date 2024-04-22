def max_dist_inversion(arr):
    c_max_dist = 0

    for key in range(len(arr)):
        for j in range(key):
            if arr[key] < arr[j]:
                c_max_dist = max(key-j,c_max_dist)

    return c_max_dist
