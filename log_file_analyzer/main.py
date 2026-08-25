""" Main file handling application.log file and store log data to their appropriate file """
import pandas as pd

with (
    open("application.log", "r", encoding="utf-8") as log_file,
    open("errors.txt", "w", encoding="utf-8") as error_file,
    open("warnings.txt", "w", encoding="utf-8") as warning_file
):
    log_data = log_file.readlines()

    # Print Log Data and store into their appropriate file
    error_count = 0
    warning_count = 0
    info_count = 0
    print("Log Data :")
    for log in log_data:
        print(log)
        if 'ERROR' in log:
            error_count += 1
            error_file.write(log)
        if 'WARNING' in log:
            warning_count += 1
            warning_file.write(log)
        if 'INFO' in log:
            info_count += 1

    # Total Log Data
    total_logs_entries = len(log_data)
    print("Total Log Entries :", total_logs_entries)

    # Count Error, Warning, Info Occurance
    print("Error count: ", error_count)
    print("Warning count: ", warning_count)
    print("Info count: ", info_count)

    # Log frequency
    df = pd.DataFrame(log_data, columns=["log"])
    df[["level", "message"]] = df["log"].str.strip().str.split(" - ",
                                                               n=1, expand=True)

    df = df[["level", "message"]]
    print("Log dataframe/n")
    print(df)

    level_counts = df[['level', 'message']].value_counts()
    print("Log level frequency\n", level_counts)
