************Purpose************

The purpose of this program is to create a command-line application using the Python programming language 
that implements quicksort. The application invokes on the command line with the name of a file to create many files, 
for example python3 quicksort_main.py input_values.txt. Those files are then placed in a folder. When invoked the application will read in all the values from each file in the folder, one per line, placing the values into a list. When done it writes out a file 
with all the values in order, one per line. The output file is now named with the original file name appended
with -sorted. For example, if the original file was called money.txt the output file will be named money-sorted.txt.
It also prints to standard out the statistics of the sorting: how many values were sorted, how many comparisons
took place, and how many assignments took place. The program is implemented in multiple modules (python source
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

main.py -  Takes the files created with numgen.py from their folder and call quicksort.py to sort their values. It then names the files
            where the sorted values are put with '-sorted' at the end and prints out the numbers of assignments and comparisons that occurred during the sort.

Results_of_quicksort_using_Python.docx - A short word document showcasing the results of each experiements and compares the number of 
            comparisons and assignments to O (n lg(n)).

.gitignore - Ignores all txt files because we do not want to track them. It excludes the files we used for the experiements and their 
            results.

**********How to use/run**********

To use this program, the user needs is to invoke on the command line with the name of a file, the number of values desired in
their list, and the range they want the values to be in. The command should follow this format:

        $ python3 numgen.py 'name of file' 'number of values' 'range of values'
Results:
1. The program prints out the unordered randomly generated values and saves the valued in the file typed in.
2. The program's main class can then be used to iterate over each file created in their folder and order their values in ascending
    order            
    print them out again, and save them 
    in a new file named with the original file name '-sorted' at the end. Then it displays a message about the number of inputs it took in and comparisons and assignments that occured.

**********Design Notes**********

- The program runs with three files: quicksort.py, numgen.py, and main.py.
- quicksort.py and main.py are independent files, while main uses the text files created by numgen.py and call quicksort to sort them.
- The unsorted files created with the command line are in the 'text_files' folder.
- The results of the experiments are in the docx file 'Results_of_quicksort_using_Python.docx'
