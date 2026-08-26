# resilient_reader.py
from pathlib import Path


def process_log_file(path_str: str):
    """Opens and reads the given file.

    Returns:
    - "MISSING" if the file does not exist.
    - "EMPTY" if the file exists but has zero lines.
    - An integer count of lines containing the word "ERROR".
    """
    path = Path(path_str)

    try:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if len(lines) == 0:
            return "EMPTY"

        # Count lines containing "ERROR"
        error_count = sum(1 for line in lines if "ERROR" in line)
        return error_count

    except FileNotFoundError:
        # Catches missing files so the script never crashes
        return "MISSING"


# Step 4: Create a deliberately empty file for testing
open("empty.log", "w").close()

# Step 2 & 4: List of files to check (including real, empty, and non-existent ones)
files_to_check = [
    "app.log",
    "backups/app_backup.log",
    "empty.log",
    "web02.log",
    "db01.log",
    "cache01.log",
]

# Step 3: Loop through all paths and print aligned results using f-string formatting
for file_path in files_to_check:
    result = process_log_file(file_path)

    # Format the result display
    if isinstance(result, int):
        status_text = f"{result} error(s)"
    else:
        status_text = result

    # Left-align filename in a 25-character field for neat formatting
    print(f"{file_path:<25} -> {status_text}")