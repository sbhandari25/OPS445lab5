#!/usr/bin/env python3
# Author ID: sbhandari25


def read_file_string(file_name):
    """Takes file_name as string for a file name, returns its entire contents as a string."""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Takes a file_name as string for a file name, returns its entire contents as a list of lines."""
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

def append_file_string(file_name, string_of_lines):
    """Appends the string to the end of the file."""
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes all items from the list to the file, each item on a new line."""
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Reads data from the first file, writes to a new file, adding line numbers."""
    with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
        for line_number, line in enumerate(f_read, start=1):
            f_write.write(f"{line_number}:{line.strip()}\n")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))


