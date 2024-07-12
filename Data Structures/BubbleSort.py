def bubble_sort(elements, key=None):

    size = len(elements)

    for i in range(size-1):
        swap = False

        for j in range(size-1-i):
            if key is None:
                a = elements[j]
                b = elements[j + 1]
            else:
                a = elements[j][key]
                b = elements[j + 1][key]

            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swap = True
        if not swap:
            break

if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]

    bubble_sort(elements)
    print(elements)
    print("________________________________________")
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'vahid', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'katty', 'transaction_amount': 200, 'device': 'sony'},
        {'name': 'amir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    bubble_sort(elements, key="name")
    print(elements)
