import os
import hashlib
import argparse
from collections import defaultdict

def get_file_hash(file_path, block_size=65536):
    """Generate MD5 hash for a file."""
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            buf = file.read(block_size)
            while buf:
                hasher.update(buf)
                buf = file.read(block_size)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
        return None

def find_duplicates(directory):
    """Find duplicate files in the specified directory."""
    hashes = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = get_file_hash(file_path)
            if file_hash:
                hashes[file_hash].append(file_path)
    duplicates = [file_group for file_group in hashes.values() if len(file_group) > 1]
    return duplicates

def delete_duplicates(duplicates):
    """Delete duplicate files based on user confirmation."""
    for file_group in duplicates:
        # Keep the first file, delete the rest
        for file_path in file_group[1:]:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error deleting {file_path}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Find and optionally delete duplicate files.")
    parser.add_argument("directory", help="Directory to scan for duplicate files.")
    parser.add_argument("--delete", action="store_true", help="Delete duplicate files after scanning.")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print("Error: Directory does not exist.")
        return

    duplicates = find_duplicates(args.directory)
    if duplicates:
        print("Duplicate files found:")
        for file_group in duplicates:
            print("\n".join(file_group))
            print("---")

        if args.delete:
            confirm = input("Are you sure you want to delete all duplicates? (y/n): ")
            if confirm.lower() == 'y':
                delete_duplicates(duplicates)
                print("All duplicates have been deleted.")
            else:
                print("Deletion canceled.")
    else:
        print("No duplicate files found.")

if __name__ == "__main__":
    main()