
import random

random.seed('class_01_random_seed')
BIN_SIZE = 40
nums = [ random.randint(2, 9) for _ in range(20) ]
print(nums)

#bin = [ 1, 2, 3 ]
#bins = [ bin ]

def bin_free(bin):
    return BIN_SIZE - sum(bin)

def bin_can_hold(bin, size):
    return bin_free(bin) >= size

def new_bin():
    nb = []
    bins.append(nb)
    return nb

def first_fit(size):
    for b in bins:
        if bin_can_hold(b, size):
            return b
    return new_bin()

def next_fit(size):
    global last_bin
    if last_bin and bin_can_hold(last_bin, size):
        return last_bin
    return new_bin()

def best_fit(size):
    smallest_bin = None
    smallest_size = BIN_SIZE
    for b in bins:
        free_space = bin_free(b)
        if free_space >= size and free_space < smallest_size:
            smallest_bin = b
            smallest_size = free_space
    if smallest_bin:
        return smallest_bin
    return new_bin()

def worst_fit(size):
    largest_bin = None
    largest_size = -1
    for b in bins:
        free_space = bin_free(b)
        if free_space >= size and free_space > largest_size:
            largest_bin = b
            largest_size = free_space
    if largest_bin:
        return largest_bin
    return new_bin()

bins = []
last_bin = None
for num in nums:
    bin = first_fit(num)
    bin.append(num)
    last_bin = bin

print(f'Function: <<first_fit>>')
print(bins)
