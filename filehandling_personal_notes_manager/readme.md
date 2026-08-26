# Personal Notes Manager Using File Handling

A beginner-friendly Python project that demonstrates how to create, write, read, append, and display personal notes using a plain text file.

## Features

The program demonstrates:

- Creating or replacing a text file
- Writing multiple notes to a file
- Reading an entire file with `read()`
- Reading a specified number of characters
- Reading one line at a time with `readline()`
- Reading all lines into a list with `readlines()`
- Iterating over individual lines
- Appending new notes without replacing existing content
- Displaying the updated file contents

## Project Structure

```text
filehandling_personal_notes_manager/
|-- main.py
|-- notes.txt
`-- readme.md
```

## Requirements

- Python 3.8 or later

No external packages are required. The project uses Python's built-in file-handling functionality.

## Running the Program

Open a terminal in the project directory and run:

```bash
python main.py
```

Run the script from the project directory because `main.py` accesses `notes.txt` using a relative path.

## How It Works

When executed, the program performs these operations:

1. Opens `notes.txt` in write mode.
2. Writes 13 initial Python-learning notes.
3. Demonstrates reading file content with `read()`.
4. Reads and prints the first two lines with `readline()`.
5. Reads every line into a list with `readlines()`.
6. Iterates through and prints the individual notes.
7. Opens the file in append mode and adds notes 14 and 15.
8. Reads and displays the final contents.

## File Modes Used

| Mode | Purpose in this project |
|---|---|
| `w` | Creates or replaces `notes.txt` and writes the initial notes |
| `r` | Reads existing notes without modifying the file |
| `a` | Adds new notes at the end of the file |

Every file is opened with UTF-8 encoding and automatically closed through a `with` statement.

## Notes File

The resulting `notes.txt` contains 15 learning notes, for example:

```text
Note 1: Learn Python basics.
Note 2: Learn variables and data types.
Note 3: Learn conditional statements.
```

The final two notes are appended by the program:

```text
Note 14: Learn Numpy after Python basics.
Note 15: Learn Plotly after Python basics.
```

## Important Behavior

The script opens `notes.txt` in write mode at the beginning of every run. This replaces the previous contents with the original 13 notes before notes 14 and 15 are appended. As a result, repeatedly running the program does not keep accumulating duplicate appended notes.

In the first reading block, `file.read()` consumes the complete file and moves the cursor to the end. The following `file.read(20)` therefore returns an empty string unless the cursor is reset with `file.seek(0)` or the reads are performed separately.
