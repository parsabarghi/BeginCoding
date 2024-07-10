from Time import time_it

@time_it
def linear_search(numbers_list, find_number):
    for index, element in enumerate(numbers_list):
        if element == find_number:
            return index
    return -1
@time_it
def binary_search(numbers_list, find_number):
    left_index = 0
    right_index = len(numbers_list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index)//2
        mid_number = numbers_list[mid_index]

        if mid_number == find_number:
            return mid_index

        if mid_number < find_number:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1
    return -1


def binary_search_recursive(numbers_list, find_number, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1
    mid_number = numbers_list[mid_index]

    if mid_number == find_number:
        return mid_index

    if mid_number < find_number:
        left_index = mid_index + 1

    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, find_number, left_index, right_index)

if __name__ == "__main__":
    numbers_list = [i for i in range(1000001)]

    find_number = 1000000


    index = linear_search(numbers_list, find_number)
    print(f"The number find at index {index} using linear serach")
    print("_____________________________________________________")
    index = binary_search(numbers_list, find_number)
    print(f"The number find in index {index} using binary search")
    print("_____________________________________________________")
    index = binary_search_recursive(numbers_list, find_number, 0, len(numbers_list))
    print(f"The number find at index {index} using binary search recusrive.")