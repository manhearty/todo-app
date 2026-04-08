import zipfile


def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, "r") as zip:
        zip.extractall(dest_dir)


if __name__ == '__main__':
    extract_archive(archive_path='C:\\Users\\Manoharan_Nadar\\PYTHON\\MegaCoursePython\\bonus\\dest\\compressed.zip',
                    dest_dir='C:\\Users\\Manoharan_Nadar\\PYTHON\\MegaCoursePython\\bonus\\dest')
