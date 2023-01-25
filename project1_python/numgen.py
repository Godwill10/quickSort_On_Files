# numgen.py
# Module to create arrays filled with random integers and sort them
#
# Usage: python3 numgen.py filename quantity [rangesize]
#
# Created - 2021 January - Erik Steinmetz
# Updated - 2021 September - Erik Steinmetz

import numpy
import sys
import quicksort


def create_list(how_many, range_size):
    """ Creates and returns an int list of the given size.

    The list is filled with values within the range size, half negative.

    Parameters
    ----------
    how_many : int
        The number of values desired in the list
    range_size : int
        The range of the values from -size/2 to +size/2

    Returns
    -------
    list
        A list of ints randomly selected in the given range
    """
    halfsize = range_size // 2
    answer = numpy.random.randint(-halfsize, halfsize, how_many)
    return answer


def write_list_to_file(filename, data_list):
    """ Writes the given data list out to a file with the given filename.

    The values are written one per line.

    Parameters
    ----------
    filename : string
        The name of the file to be written
    data_list : list
        A list of ints to be written to the file
    """
    outfile = open(filename, 'w')
    for value in data_list:
        aline = str(value) + "\n"
        outfile.write(aline)
    outfile.close()


def main():
    """ Creates a list of random values and write the list to a file.

    The name of the file to be created, the number of values to
    be created, and optionally the range of those values are
    specified by command line arguments.
    """
    if len(sys.argv) < 3:
        print("Usage: python3 numgen.py filename quantity [rangesize]")
        exit()
    the_filename = sys.argv[1]
    the_quantity = int(sys.argv[2])
    the_rangesize = 200
    if len(sys.argv) >= 4:
        the_rangesize = int(sys.argv[3])
    the_data = create_list(the_quantity, the_rangesize)
    write_list_to_file(the_filename, the_data)
    print(the_quantity, "values written to", the_filename)

    """
    Reading the randomly generated values from the the_filename
    Puts them in list_of_nums list and print them out
    """

    list_of_nums = []
    infile = open(the_filename, 'r')
    for aline in infile:
        anumber = int(aline)
        list_of_nums.append(anumber)
    print('Unordered list:')
    print(list_of_nums)

    """
    Orders the randomly generated values in list_of_nums
    Print the values out in the new order and stores them in a new file
    named with the original file name '-sorted' at the end
    """
    size = len(list_of_nums)
    quicksort.quickSort(list_of_nums, 0, size - 1)
    print('Ordered list:')
    print(list_of_nums)

    the_new_filename = the_filename + '-ordered'
    write_list_to_file(the_new_filename, list_of_nums)
    print('Sorted values to ', the_new_filename)


if __name__ == "__main__":
    main()
