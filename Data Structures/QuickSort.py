def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def partition_hoare(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]


    while start < end:
        while start <len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot :
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end

def partition_lomuto(elements, start, end):
    pivot_index = start
    pivot = elements[start]
    i = start + 1

    for j in range(start+1, end+1):
        if elements[j] < pivot:
            swap(i, j, elements)
            i = i + 1
    swap(pivot_index, i-1, elements)

    return i - 1



def quick_sort(elements, start, end):
    if start < end:
        pi = partition_hoare(elements, start, end)
        # left partition
        quick_sort(elements, start, pi - 1)
        # right partition
        quick_sort(elements, pi + 1, end)
        # Lomuto
        pi2 = partition_lomuto(elements, start, end)
        # left partition
        quick_sort(elements, start, pi2 - 1)
        # right partition
        quick_sort(elements, pi2 + 1, end)


if __name__ == '__main__':
    elements = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(elements, 0, len(elements)-1)
    print(elements)
    print("_________________________________")
    quick_sort(elements, 0, len(elements)-1)
    print(elements)