import ex_01_10_2020182006_2 as qs

def selection(arr, beg, end, nth):
    pi = qs.partition(arr,beg,end)
    ss = pi - beg + 1
    if ss == nth:
        return arr[pi]
    elif ss < nth:
        return selection(arr, pi + 1, end, nth - ss)
    else:
        return selection(arr, beg, pi - 1, nth)

def main():
    print(qs.words)
    print(qs.partition)

    ranks = [ 3, 7, 23, 88, 99 ]

    last_word_index = len(qs.words) - 1
    for rank in ranks:
        words = qs.words[:]
        word = selection(words, 0, last_word_index, rank)
        print(f'{rank=} {word=}')


if __name__ == '__main__':
    main()


