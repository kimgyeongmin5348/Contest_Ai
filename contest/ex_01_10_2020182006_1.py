import random

words = [
    '2020182006', 'hut', 'apostle', 'equipment', 'fop', 'refined', 'parapet', 'mog', 'amputate', 'covetous', 'somebody',
    'all', 'lobbyist', 'remark', 'subscriber', 'quorum', 'steppe', 'clean', 'cu', 'commend', 'prosy',
    'supererogation', 'indignation', 'wolverine', 'emporium', 'intersect', 'constitution', 'miscast', 'rabbi', 'enmity', 'loft',
    'temporize', 'speedboat', 'agenda', 'delusion', 'class01', 'idolize', 'romance', 'overestimate', 'revive', 'smell',
    'toast', 'singe', 'inlay', 'field', 'speed', 'farad', 'adult', 'pansy', 'crawl', 'smith', 'exude',
    'froze', 'litho', 'inuit', 'fakir', 'noddy', 'sheen', 'sandy', 'gaffe', 'spark', 'cavil', 'tenor',
    'clonk', 'stung', 'boult', 'inapt', 'taker', 'cliff', 'shine', 'sable', 'agile', 'evens', 'pluck',
    'blade', 'niece', 'paste', 'theft', 'young', 'bonny', 'aggro', 'bevel', 'rebel', 'clown', 'quote',
    'horsy', 'wrong', 'hindu', 'acute', 'sloop', 'tuner', 'expel', 'motel', 'divan', 'gesso', 'strop',
    'lance', 'lifer', 'dunce', 'lemur', 'scree', 'basic', 'wring', 'graph', 'conch', 'favor', 'anise',
    'value', 'queue', 'poppy', 'staid', 'snook', 'spurt', 'canto', 'sprat', 'first', 'sidle', 'douse',
]
def insertionSort(arr, left, right):  # right-inclusive
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, start, mid, end):
    left_array = arr[start:mid + 1]
    right_array = arr[mid + 1:end + 1]

    merged = []
    left_idx, right_idx = 0, 0

    while left_idx < len(left_array) and right_idx < len(right_array):
        if left_array[left_idx] <= right_array[right_idx]:
            merged.append(left_array[left_idx])
            left_idx += 1
        else:
            merged.append(right_array[right_idx])
            right_idx += 1

    merged.extend(left_array[left_idx:])
    merged.extend(right_array[right_idx:])

    for i, value in enumerate(merged):
        arr[start + i] = value

def mergeSort(arr, start, end):  # end-inclusive
    size = end - start + 1
    if size <= 5:
        insertionSort(arr, start, end)
        return

    mid = (start + end) // 2

    mergeSort(arr, start, mid)
    mergeSort(arr, mid + 1, end)
    merge(arr, start, mid, end)



mergeSort(words, 0, len(words) - 1)
print(words)