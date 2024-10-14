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

def insertionSort(arr,left,right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i-1
    #주인공 피신
        while j >= left and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1]= key  # 주인공이 들어잘 자리는 여기다.

def partition(arr,start,end):
    random_index = random.randint(start, end)
    arr[start], arr[random_index] = arr[random_index], arr[start]

    pivot = arr[start]
    p = start + 1
    q = end

    while True:
        while p <= end and arr[p] > pivot:
            p += 1
        while q >= start + 1 and arr[q] < pivot:
            q -= 1
        if p>=q:
            break

        arr[p],arr[q] = arr[q],arr[p]

    arr[start], arr[q] = arr[q], arr[start]

    return q

def quickSort(arr,start,end):
    size = end-start+1
    if size <=5:
        insertionSort(arr,start,end)
        return

    pivot_index = partition(arr, start, end)
    quickSort(arr,start,pivot_index-1)
    quickSort(arr,pivot_index+1,end)
if __name__ == '--main__':
    quickSort(words,0,len(words)-1)
    insertionSort(words,0,len(words)-1)

print(words)



