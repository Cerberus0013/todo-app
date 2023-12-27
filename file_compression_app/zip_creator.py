import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.Zipfile(dest_path, "w") as archive:
        for filepath in filepaths:
            archive.write(filepath)

