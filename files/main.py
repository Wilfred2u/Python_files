# Do not modify these lines
__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

# Add your code after this line
import os
from zipfile import ZipFile


def clean_cache():
    dir = 'files\\cache'
    if not os.path.exists(dir):
        os.makedirs(dir)
    elif os.path.exists(dir):
        for file in os.listdir(dir):
            os.remove(os.path.join(dir, file))


def cache_zip(zip_file, cache_dir):
    with ZipFile(zip_file, 'r') as zObject:
        zObject.extractall(path=cache_dir)


def cached_files():
    absolute_path = os.path.abspath('files\\cache')
    file_list = os.listdir(absolute_path)
    result = []
    for file in file_list:
        result.append(os.path.join(absolute_path, file))
    return result


def find_password(files):
    for file in files:
        with open(file, 'r') as searching_text:
            for line in searching_text:
                if 'password' in line:
                    splitted_line = line.split()
                    [x for x in splitted_line if 'password' in x]
                    return splitted_line[1]


if __name__ == "__main__":
    clean_cache()
    cache_zip('files\\data.zip', 'files\\cache')
    print(cached_files())
    print(find_password(cached_files()))
