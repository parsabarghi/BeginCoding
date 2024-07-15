def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2

if __name__ == '__main__':
    print("FIRST TRY:")
    elements = [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(elements)
    print(elements)
    print("________________________________________________")
    print("TEST:")
    test = [[89, 67, 78, 34, 34, 23, 12, 1, 32, 3, 4, 5, 7, 8],
            [],
            [1, 2, 3, 4, 5, 6, 7],
            [7, 6, 5, 4, 3, 2, 1],
            [5],
            [1299999999, 23, 2, 45]
            ]
    for elements in test:
        shell_sort(elements)
        print(elements)
