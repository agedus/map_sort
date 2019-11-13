import os
import time
import shutil
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

skip = ["ini", "part"]


def sorting():
    for dirs in config['SORT_DIRECTORY']['directorys'].split(","):
        path_sort = config[dirs.upper()]['path_sort']
        path_place = config[dirs.upper()]['path_place']
        file_extensions = config[dirs.upper()]['extensions'].split(",")
        for d_file in os.listdir(path_sort):
            f_extension = d_file.split(".")[-1]
            if f_extension in skip:
                print(f"bestand: {d_file} skipt")
                continue
            elif d_file + ".part" in os.listdir(path_sort):
                print(f"bestand: {d_file} heeft nog een .part file")
                continue
            elif f_extension in file_extensions:
                sort = path_sort + "/" + d_file
                place = path_place + "/" + d_file
                shutil.move(sort, place)


sorting()
# while True:
#     directory = os.listdir("path/to/dir")
#     mylist = os.listdir("path/to/dir")
#     time.sleep(1)
#     if "desktop.ini" in mylist:
#         if len(mylist) >= 2:
#             sorting()
#     else:
#         if len(mylist) >= 1:
#             sorting()
