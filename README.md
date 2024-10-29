# Duplicate Finder Tool

This Python tool scans a specified directory for duplicate files by comparing their content using MD5 hashing. Optionally, it can delete the duplicates, keeping only the first instance of each file.

## Features

- Scans any specified directory for duplicate files
- Uses MD5 hashing to ensure accuracy in duplicate detection
- Optional deletion of duplicate files

## Installation

1. **Clone the repository** (or download the `duplicate_finder.py` file).
2. Ensure you have **Python 3** installed on your system.
3. Place the `duplicate_finder.py` file inside a `src` folder for easy execution.

## Usage

Navigate to the root of your project directory and run the following commands in your terminal:

### 1. Find Duplicates Only
This command scans for duplicate files and lists them without deleting anything.
```bash
python3 src/duplicate_finder.py ~/Downloads

2. Find and Delete Duplicates

This command scans for duplicates and, upon confirmation, deletes all but the first instance of each duplicate file.

python3 src/duplicate_finder.py ~/Downloads --delete

Note: Replace ~/Downloads with the path to any directory you want to scan.

Example Output

When duplicates are found, they are listed as groups, with each group separated by lines. If deletion is chosen, you will see a message confirming the deletion of each duplicate file.

How It Works

The tool uses MD5 hashing to create a unique fingerprint for each file, comparing these hashes to identify duplicates. Only files with matching hashes are considered duplicates, ensuring a high level of accuracy.

License

This project is open-source and available under the MIT License.