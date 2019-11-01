import configparser
from tkinter import *
from tkinter import filedialog

config = configparser.ConfigParser()
config.read('settings.ini')

root = Tk()

extension_array_img = []
extension_array_txt = []


# FIXME make 1 function for all types
# Select a directory to be sorted


# def browse_button_sort():
#     global folder_path_srt
#     filename = filedialog.askdirectory()
#     if filename:
#         config['SORT']['path'] = filename
#     folder_path_srt.set(config['SORT']['path'])


# # Select a directory to put image files in and what extensions and commit the exentesions to filter


# def browse_button_img():
#     global folder_path_img
#     filename = filedialog.askdirectory()
#     if filename:
#         config['IMAGES']['path'] = filename
#     folder_path_img.set(config['IMAGES']['path'])


# def push_button_img(event):
#     extension = entry_img.get()
#     extension = extension.replace(".", "")
#     if extension not in extension_array_img:
#         extension_array_img.append(extension)
#     entry_img.delete(0, 'end')


# def commit_button_img():
#     push_extensions = ""
#     for extension in extension_array_img:
#         extension = extension.replace(" ", "")
#         push_extensions += extension + ","
#     push_extensions = push_extensions[:-1]
#     if push_extensions:
#         config['IMAGES']['extensions'] = push_extensions
#     extensions_img.set(config['IMAGES']['extensions'])

# # Select a directory to put text files in and what extensions and commit the exentesions to filter


# def browse_button_txt():
#     global folder_path_txt
#     filename = filedialog.askdirectory()
#     if filename:
#         config['TEXT']['path'] = filename
#     folder_path_txt.set(config['TEXT']['path'])


# def push_button_txt(event):
#     extension = entry_txt.get()
#     extension = extension.replace(".", "")
#     if extension not in extension_array_txt:
#         extension_array_txt.append(extension)
#     entry_txt.delete(0, 'end')


# def commit_button_txt():
#     push_extensions = ""
#     for extension in extension_array_txt:
#         extension = extension.replace(" ", "")
#         push_extensions += extension + ","
#     push_extensions = push_extensions[:-1]
#     if push_extensions:
#         config['TEXT']['extensions'] = push_extensions
#     extensions_txt.set(config['TEXT']['extensions'])
################################################################

#write the code in settings.ini file#


def write():
    with open('settings.ini', 'w') as f:
        config.write(f)

# checks for all your selected directorys


def section_check():
    for sort_dir in config['SORT_DIRECTORY']['directorys'].split(","):
        if not sort_dir == "":
            if not config.has_section(sort_dir.upper()):
                config.add_section(sort_dir.upper())
                config[sort_dir.upper()]['path_sort'] = "None"
                config[sort_dir.upper()]['path_place'] = "None"


# add a new directory to sort


def add_sort():
    new_directory = entry_add.get().lower()
    if not config.has_section('SORT_DIRECTORY'):
        config.add_section('SORT_DIRECTORY')
        config['SORT_DIRECTORY']['directorys'] = new_directory.lower()
    else:
        directorys = config['SORT_DIRECTORY']['directorys'].split(",")
        if entry_add.get():
            if not new_directory in directorys:
                directorys.append(new_directory)
                push_dirs = ""
                for dirs in directorys:
                    dirs = dirs.replace(" ", "")
                    push_dirs += dirs + ","
                push_dirs = push_dirs[:-1]
                if push_dirs.startswith(","):
                    push_dirs = push_dirs[1:]
                config['SORT_DIRECTORY']['directorys'] = push_dirs
    entry_add.delete(0, 'end')
    section_check()
    write()


if config.has_section('SORT_DIRECTORY'):
    section_check()
    write()

#GUI#

# make the layout for every directory you made to sort


def blocks():
    for sort_dir in config['SORT_DIRECTORY']['directorys'].split(","):
        pass


################################################################
# # TODO make one layout to use multiple times
# folder_path_srt = StringVar()
# folder_path_img = StringVar()
# folder_path_txt = StringVar()
# extensions_img = StringVar()
# extensions_txt = StringVar()
# folder_path_srt.set(config['SORT']['path'])
# folder_path_img.set(config['IMAGES']['path'])
# folder_path_txt.set(config['TEXT']['path'])
# extensions_img.set(config['IMAGES']['extensions'])
# extensions_txt.set(config['TEXT']['extensions'])

# # srt
# main_l_srt = Label(root, textvariable=folder_path_srt)
# main_l_srt.grid(row=0, column=1)
# button_srt = Button(root, text="Select directory sort",
#                     command=browse_button_sort)
# button_srt.grid(row=0, column=3)

# # img
# main_l_img = Label(root, textvariable=folder_path_img)
# main_l_img.grid(row=1, column=1)
# button_img = Button(root, text="Select directory foto",
#                     command=browse_button_img)
# button_img.grid(row=1, column=3)
# entry_img = Entry(root)
# entry_img.grid(row=4, column=1)
# entry_img.bind('<Return>', push_button_img)
# button_img_entry = Button(
#     root, text="commit exetension foto", command=commit_button_img)
# button_img_entry.grid(row=4, column=3)
# main_l_img = Label(root, textvariable=extensions_img)
# main_l_img.grid(row=4, column=5)


# # txt
# main_l_txt = Label(root, textvariable=folder_path_txt)
# main_l_txt.grid(row=2, column=1)
# button_txt = Button(root, text="Select directory text",
#                     command=browse_button_txt)
# button_txt.grid(row=2, column=3)
# entry_txt = Entry(root)
# entry_txt.grid(row=5, column=1)
# entry_txt.bind('<Return>', push_button_txt)
# button_txt_entry = Button(root, text="commit exetension text",
#                           command=commit_button_txt)
# button_txt_entry.grid(row=5, column=3)
# main_l_txt = Label(root, textvariable=extensions_txt)
# main_l_txt.grid(row=5, column=5)
# # TODO add al extension types


button_add_sort = Button(root, command=add_sort, text="+")
button_add_sort.grid(row=10, column=1)
entry_add = Entry(root)
entry_add.grid(row=10, column=3)


mainloop()
