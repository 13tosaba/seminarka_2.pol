from timeit import repeat
from random import sample, shuffle
from bucket_sort import bucket_sort_naive, bucket_sort_reversed


def test_time(func):
    global testing_counts
    print(f"Timing function {func.__name__}:")
    for count in testing_counts:
        print(f"For count = {count}:")
        test_data = create_test_data(count)
        for data in test_data:
            time = repeat(f"{func.__name__}({data[1]})", number=1, repeat=5, globals=globals())
            max_time = max(time)
            min_time = min(time)
            print(f"{data[0]}: {min_time} s - {max_time} s")
        print()
    print()


def create_test_data(count):
    if count >= 900000:
        print("Not able to test")
        count = 100000
        print(f"For count = {count}:")
    full_list = list(range(1, count + 1))
    randomized = full_list[:]
    shuffle(randomized)
    third = sample(randomized, k=count//3)
    big_num = sample(list(range(100000, 1000000)), k=count)
    bigger_num = sample(list(range(100000000, 1000000000, 17)), k=count)

    return [
        ["Full sorted list", full_list],
        ["Randomized full list", randomized],
        ["Random third", third],
        ["Random 6 digits numbers", big_num],
        ["Random 9 digits numbers", bigger_num]
    ]

testing_counts = (100, 200, 300, 100000000)

test_time(bucket_sort_naive)
test_time(bucket_sort_reversed)
