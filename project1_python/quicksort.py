# quicksort.py
# Module to execute quicksort algorithm
#
# Created - 2023 January - Godwill Afolabi


# function to find the partition position
def partition(array, low, high):
    comp = 0
    assign = 0

    # choose the rightmost element as pivot
    pivot = array[high]
    assign += 1

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        comp += 1
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            assign += 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            assign += 2

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    assign += 1

    # return the position from where partition is done
    return i + 1, assign, comp


# function to perform quicksort
def quickSort(array, low, high):
    assign = 0
    comp = 0
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi, ass, cc = partition(array, low, high)
        assign += ass
        comp += cc

        # recursive call on the left of pivot
        ass, cc = quickSort(array, low, pi - 1)
        assign += ass
        comp += cc

        # recursive call on the right of pivot
        ass, cc = quickSort(array, pi + 1, high)
        assign += ass
        comp += cc
    return assign, comp
