from pathlib import Path

# Folder to scan
FOLDER = Path(r"C:\Users\AdanG\Desktop\logsig")

# File extensions to delete (lowercase)
TARGET_EXTENSIONS = {".tmp", ".log", ".bak", ".old"}


def find_junk_files(folder: Path, target_extensions: set[str]) -> list[Path]:
    """Return files in folder (and subfolders) matching target extensions."""
    matches: list[Path] = []

    for file_path in folder.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in target_extensions:
            matches.append(file_path)

    return matches


def delete_files(files: list[Path]) -> int:
    """Delete files and return how many were deleted."""
    deleted_count = 0

    for file_path in files:
        try:
            file_path.unlink()
            deleted_count += 1
            print(f"Deleted: {file_path}")
        except Exception as error:
            print(f"Could not delete {file_path}: {error}")

    return deleted_count


def main() -> None:
    if not FOLDER.exists():
        print(f"Folder does not exist: {FOLDER}")
        return

    junk_files = find_junk_files(FOLDER, TARGET_EXTENSIONS)

    if not junk_files:
        print("No junk files found.")
        return

    print("Files found:")
    for file_path in junk_files:
        print(f" - {file_path}")

    print(f"\nTotal files found: {len(junk_files)}")
    answer = input("Delete these files? (y/n): ").strip().lower()

    if answer == "y":
        deleted = delete_files(junk_files)
        print(f"\nDeleted {deleted} file(s).")
    else:
        print("No files were deleted.")


if __name__ == "__main__":
    main()

