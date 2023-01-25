************Purpose************

The purpose of this program is to create a command-line application using the Python programming language 
that implements quicksort. The application invokes on the command line with the name of a file, 
for example python3 quicksort_main.py input_values.txt. When invoked the application will read in all the
values from the file, one per line, placing the values into a list. When done it should write out a file 
with all the values in order, one per line. The output file should be named with the original file name appended
with -sorted. For example, if the original file was called money.txt the output file would be named money-sorted.txt.
It should also print to standard out the statistics of the sorting: how many values were sorted, how many comparisons
took place, and how many assignments took place. Your program should be implemented in multiple modules (python source
files).


**********Organization**********

All required files are inside the project1_python directory. 

quicksort.py - Includes two methods (algorithm) required for the quicksort sorting to take place: partition and quickSort.

numgen.py - A python file with 3 methods: create_list, write_list_to_file, and main.
            create_list: creates the Creates and returns an int list of the given size. 
                The list is filled with values within the range size, half negative.
            write_list_to_file: Writes the given data list out to a file with the given filename. 
                The values are written one per line.
            main:   . Creates a list of random values and write the list to a file
                    . Creates the name of the file to be created, the number of values to be created,
                    and optionally the range of those values are specified by command line arguments.
                    . Reads the file invoked, puts its values in a list one per line, then sorts the 
                    list using the quickSort method in quicksort.py.

pseudo_quicksort.txt - A pseudocode text file of how the quicksort algorithm is done.

.gitignore - Ignores all txt files because we do not want to track them.

**********How to use/run**********

To use this program, the user needs is to invoke on the command line with the name of a file, the number of values desired in
their list, and the range they want the values to be in. The command should follow this format:

        $ python3 numgen.py 'name of file' 'number of values' 'range of values'
Results:
1. The program prints out the unordered randomly generated values and saves the valued in the file typed in.
2. The program orders those values in ascending order, prints them out again, and saves them in a new file named with the
original file name '-sorted' at the end.

**********Design Notes**********

The program only depends on 'numgen.py' and 'quicksort.py' to execute. However, the next step of this software is to separate
the main in 'numgen.py' into a different class in order to have a cleaner code base.