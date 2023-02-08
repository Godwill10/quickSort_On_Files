# main.py
# Reads text file created by numgen.py, sorts its values
# and stores them in a new file
#
# Created - 2023 January - Godwill Afolabi

import quicksort
import numgen
import os


def main():
    """
    Reading the randomly generated values from the the_filename
    Puts them in list_of_nums list and print them out
    """
    path = '/Users/owner/Downloads/project1_python/project1_python/text_files'
    folder = os.fsencode(path)
    list_of_nums = []

    for file in os.listdir(folder):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            the_filename = filename
            infile = open(filename, 'r')
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
            assign, comp = quicksort.quickSort(list_of_nums, 0, size - 1)
            print('Ordered list:')
            print(list_of_nums)
            print()
            print("Input size: ", the_filename)
            print("Assignment: ", assign)
            print("Comparison: ", comp)

            the_new_filename = the_filename + '-ordered.txt'
            numgen.write_list_to_file(the_new_filename, list_of_nums)
            print('Sorted values to ', the_new_filename)


if __name__ == "__main__":
    main()
