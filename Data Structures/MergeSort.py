def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left, right)

def merge_two_sorted_list(a, b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = 0
    j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list

if __name__ == '__main__':
    a = [2, 5, 12, 13, 20, 66]
    b = [1, 4, 6, 23, 26, 56]
    print(merge_two_sorted_list(a, b))
    print("_______________________________________________")
    arr = [23, 4, 15, 34, 21, 2, 33, 24]
    print(merge_sort(arr))
