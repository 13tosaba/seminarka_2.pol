from random import shuffle
from bucket_sort import bucket_sort_naive,bucket_sort_reversed

def test(func):
    print(f"Testing {func.__name__}:")
    test_settings = set_test()
    attempt_number = 1
    for attempt in test_settings:
        print(f"Attempt {attempt_number}:", end=" ")
        try:
            if attempt[1] == func(attempt[0]):
                print("OK")
            else:
                print("Not sorted")
        except:
            print("Error")
        attempt_number += 1
    print()

def mix(arr):
    shuffle(arr)
    return arr

def set_test():
    global test_data
    attempts = []
    for data in test_data:
        attempt = []
        """for num in data:
            if not isinstance(num, int):
                return print("Test data are not correct!")"""
        attempt.append(list(data))
        attempt.append(sorted(list(data)))
        attempts.append(attempt)
    return attempts


test_data = [
    list(range(0, 658, 5)),
    list(reversed(range(100, 5000))),
    mix(list(range(0, 500)))
]    


test(bucket_sort_naive)
test(bucket_sort_reversed)

"""arr = list(range(0, 22))
shuffle(arr)

print(arr)
print()
print(bucket_sort.bucket_sort_reversed(arr))
print(bucket_sort.bucket_sort_naive(arr))"""
