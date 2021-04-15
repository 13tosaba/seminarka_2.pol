def bucket_sort_reversed(arr):
    def bucket_sort_reversed_base(arr, order):
        new_arr = []
        for bucket in range(0,10):
            for num in arr:
                digit = int(f"{num//(10**(order - 1))}"[-1])
                if digit == bucket:
                    new_arr.append(num)
        return new_arr


    arr = arr[:]
    final_order = len(str(max(arr)))
    for order in range(1, final_order + 1):
        arr = bucket_sort_reversed_base(arr, order)

    return arr


def bucket_sort_naive(arr):
    def bucket_sort_naive_base(arr, order, new_arr):
        if arr == []:
            return
        if order == 0 or len(arr) == 1:
            new_arr.extend(arr)
            return
        buckets = [[],[],[],[],[],[],[],[],[],[]]
        for num in arr:
            digit = int(f"{num//(10**(order - 1))}"[-1])
            buckets[digit].append(num)
        for bucket in buckets:
            bucket_sort_naive_base(bucket, order - 1, new_arr)


    arr = arr[:]
    max_order = len(str(max(arr)))
    new_arr = []
    bucket_sort_naive_base(arr, max_order, new_arr)
    
    return new_arr
    


