from pathlib import Path
import datetime
import shutil

# 1. build today's date as a string
today_str = datetime.date.today().strftime("%Y-%m-%d")

# 2. build directory and file paths
backup_dir = Path("backups")
backup_dir.mkdir(parents=True, exist_ok=True) # create the folder if not exist

source_file = Path("app.log")
source_file.touch(exist_ok=True) # create the file if not exist

destination_path = backup_dir / f"app_{today_str}.log"

# 3. copy app.log to destination
shutil.copy(source_file, destination_path)

# 4. print confirmation
print(f"Backup created successfully at: {destination_path}")