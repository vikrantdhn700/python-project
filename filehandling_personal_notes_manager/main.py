""" Python File Handling Example File: notes.txt"""

FILENAME = 'notes.txt'

# Creating a file
with open(FILENAME, 'w', encoding='utf-8') as file:
    file.write("""Note 1: Learn Python basics.
Note 2: Learn variables and data types.
Note 3: Learn conditional statements.
Note 4: Learn loops in Python.
Note 5: Learn Python functions.
Note 6: Learn exception handling.
Note 7: Learn Python packages.
Note 8: Learn logging in Python.
Note 9: Learn object-oriented programming.
Note 10: Learn Python file handling.
Note 11: Practice file handling regularly.
Note 12: Build projects using Python.
Note 13: Learn Pandas after Python basics.""")


# Reading the entire file and specific number of character
with open(FILENAME, 'r', encoding='utf-8') as file:
    # content = file.read()  # Keep blank to get entire file content
    content = file.read(20)  # Pass number to get specific number of character
    print("Reading file content /n")
    print(content)

# # # Using readline()
with open(FILENAME, 'r', encoding='utf-8') as file:
    # reads only one line at a time and returns a string
    first_content = file.readline()
    second_content = file.readline()
    third_content = file.readline()
    print("Reading using readline: \n ")
    print(first_content)
    print(second_content)
    print(third_content)

# # # Using readlines()
with open(FILENAME, 'r', encoding='utf-8') as file:
    content_list = file.readlines()
    print("List of content \n")
    print(content_list)
    for content in content_list:
        print(content)

# # Appending additional notes
with open(FILENAME, 'a', encoding='utf-8') as file:
    file.write("\n")
    file.write("Note 14: Learn Numpy after Python basics. \n")
    file.write("Note 15: Learn Plotly after Python basics. \n")

# # Displaying updated content
with open(FILENAME, 'r', encoding='utf-8') as file:
    content = file.read()
    print("Displaying updated content: /n")
    print(content)
