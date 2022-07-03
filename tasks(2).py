old_collection = [1, 3, 5, 2, 8, 9, 6, 11, 14, 12, 16, 19, 0]


def bubbleSort(collection):
    l = len(collection)

    for i in range(l - 1):
        for j in range(l - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]

    return collection


def insertionSort(collection):
    for i in range(1, len(collection)):
        temp = collection[i]
        j = i - 1
        while j >= 0 and temp < collection[j]:
            collection[j + 1] = collection[j]
            j = j - 1
        collection[j + 1] = temp
    return collection


new_collection = bubbleSort(old_collection.copy())
new_collection_2 = insertionSort(old_collection.copy())

print('изначальный список: ' + str(old_collection))
print('пузырьковая сортировка: ' + str(new_collection))
print('сортировка вставками: ' + str(new_collection_2))
