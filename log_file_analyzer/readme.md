# Log File Analyzer

A simple Python log-analysis project that reads an application log, counts entries by severity, separates warnings and errors into dedicated files, and converts the log data into a Pandas DataFrame.

## Features

The analyzer:

- Reads entries from `application.log`
- Prints every log entry to the terminal
- Counts total INFO, WARNING, and ERROR entries
- Writes ERROR entries to `errors.txt`
- Writes WARNING entries to `warnings.txt`
- Splits each entry into `level` and `message` fields
- Creates and displays a Pandas DataFrame
- Displays the frequency of each level-and-message combination

## Project Structure

```text
log_file_analyzer/
|-- main.py
|-- application.log
|-- errors.txt
|-- warnings.txt
`-- readme.md
```

## Log Format

Each entry should be on a separate line using this format:

```text
LEVEL - Message
```

Supported levels in the current dataset are:

- `INFO` for normal application activity
- `WARNING` for conditions that may require attention
- `ERROR` for failed operations or unavailable services

Example entries:

```text
INFO - Application started
WARNING - Memory usage high
ERROR - Database connection failed
```

The included `application.log` contains 40 entries:

| Level | Count |
|---|---:|
| INFO | 28 |
| WARNING | 7 |
| ERROR | 5 |
| **Total** | **40** |

## Requirements

- Python 3.8 or later
- Pandas

Install Pandas with:

```bash
python -m pip install pandas
```

## Running the Analyzer

Open a terminal in the project directory and run:

```bash
python main.py
```

Run the command from the project root because the script accesses its files using relative paths.

## Generated Files

Each run creates or overwrites these files:

- `errors.txt` contains every line that includes `ERROR`.
- `warnings.txt` contains every line that includes `WARNING`.

INFO entries are counted and displayed but are not written to a separate output file.

## How It Works

The script reads all lines from `application.log`, checks each line for its severity keyword, updates the relevant counter, and writes matching warnings and errors to their output files. It then uses Pandas to split each log entry at the first ` - ` delimiter:

```text
INFO - Application started
```

becomes:

| level | message |
|---|---|
| INFO | Application started |

## Notes

- Keep one log entry per line.
- Include the exact ` - ` delimiter so Pandas can separate the level and message.
- The output text files are opened in write mode, so their previous contents are replaced whenever the script runs.
- Severity counting checks whether the words `INFO`, `WARNING`, or `ERROR` occur anywhere in each line.
