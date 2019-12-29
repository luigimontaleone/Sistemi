from _collections import deque
if __name__ == '__main__':
    j = 3
    a = [1, 2, 3, 4, 5, 6]
    #un modo di fare lo shift
    while j > 0:
        i = len(a) - 1
        temp = a[0]
        while i > 0:
            a[(i + 1) % len(a)] = a[i]
            i -= 1
        a[1] = temp
        j -= 1
    #altro modo di fare lo shift
    d = deque([1, 2, 3, 4, 5])
    d.rotate(1)
    print(f"{d}")