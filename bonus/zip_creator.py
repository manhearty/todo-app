import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as zip:

        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zip.write(filepath, arcname=filepath.name)



if __name__ == '__main__':
    make_archive(filepaths=["bonus11.py", "bonus12.py", "bonus13.py"],dest_dir="dest")