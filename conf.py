import configparser
from tkinter import *
from tkinter import filedialog

config = configparser.ConfigParser()
config.read('settings.ini')

root = Tk()

label_check = False
l_block = None
# extension_array_img = []
# extension_array_txt = []

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
                config[sort_dir.upper()]['extensions'] = "None"


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
    blocks()


#GUI#

# make the layout for every directory you made to sort


def blocks():
    global label_check, l_block
    if label_check:
        l_block.destroy()
    l_block = Label(root)
    row = 3
    for sort_dir in config['SORT_DIRECTORY']['directorys'].split(","):
        row += 1
        l_section = Label(l_block, text=sort_dir.upper())
        l_section.grid(column=1, row=row)
        e_section = Entry(l_block)
        e_section.grid(column=2, row=row)
        l_text = Label(l_block, text="Sorting directory:")
        l_text.grid(column=3, row=row)
    l_block.grid()
    label_check = True

# make a directory


button_add_sort = Button(root, command=add_sort, text="+")
button_add_sort.grid()
entry_add = Entry(root)
entry_add.grid()

#startup#


if config.has_section('SORT_DIRECTORY'):
    section_check()
    write()
    blocks()

mainloop()
