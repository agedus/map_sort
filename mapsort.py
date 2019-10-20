import os
import time
import shutil
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

# TODO make folders from .ini file
path = "C:/Users/basse/Downloads"
# TODO add al etensions to var extensions
extensions = [{config['IMAGES']['path']: config.get(
    'IMAGES', 'extensions').split(',')}, {config['TEXT']['path']: config.get(
        'TEXT', 'extensions').split(',')}]
print(extensions[0].keys)
skip = ["ini", "part"]
downloads = None


def sorting():
    for d_file in downloads:
        value = None
        src = None
        dst = None
        file_extension = d_file.split(".")[-1]
        for i in extensions:
            if file_extension in skip:
                value = f"bestand: {d_file} skipt"
            elif d_file + ".part" in downloads:
                value = f"bestand: {d_file} heeft nog een .part file"
            else:
                for j in i:
                    if file_extension in i[j]:
                        src = f"{path}/{d_file}"
                        dst = f"{j}/{d_file}"
            if not value and not src:
                src = f"{path}/{d_file}"
                dst = f"D:/unknown_downloads/{d_file}"
        if value:
            print(value)
        else:
            shutil.move(src, dst)


while True:
    downloads = os.listdir("C:/Users/basse/Downloads")
    mylist = os.listdir("C:/Users/basse/Downloads")
    time.sleep(1)
    if "desktop.ini" in mylist:
        if len(mylist) >= 2:
            sorting()
    else:
        if len(mylist) >= 1:
            sorting()
