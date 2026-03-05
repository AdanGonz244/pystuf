from pathlib import Path

folder = Path(r"C:\Users\AdanG\Desktop\logsig")
extensions = {".log", ".tmp"}


def findjnkfiles(files, extensions):
    filelst: list[Path] = []
    for file in files.rglob("*"):
        if file.is_file() and file.suffix.lower() in extensions:
            filelst.append(file)
    return filelst

findjnkfiles(folder, extensions)
print(findjnkfiles(folder, extensions))