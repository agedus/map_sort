import mapsort
import configparser
from tkinter import *
from tkinter import filedialog

config = configparser.ConfigParser()
config.read('settings.ini')

root = Tk()
root.geometry("1500x500")

label_check = False
label_check_edit = False
l_block = None
l_edit_block = None
collumn_count = 0
e_extension = ""

#backend#

# write the code in settings.ini file


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
    new_directory = entry_add.get().lower().replace(" ", "")
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

# update the sorting en placing directory


def path(type_directory, directory):
    filename = filedialog.askdirectory()
    if filename:
        config[directory][type_directory] = filename
        write()
        blocks()

# push extensions to settings.ini


def extensions(extension, directory):
    extension = extension.replace(".", "")
    if extension:
        if extension not in config[directory]['extensions'].split(","):
            if config[directory]['extensions'].startswith("None"):
                config[directory]['extensions'] = extension
            else:
                new_extension = config[directory]['extensions'] + \
                    "," + extension
                config[directory]['extensions'] = new_extension
            write()
            blocks()
        e_extension.delete(0, 'end')

# delete a directory


def delete(directory):
    push_dirs = ""
    directorys = config['SORT_DIRECTORY']['directorys'].split(",")
    if directory.lower() in directorys:
        directorys.remove(directory.lower())
        for dirs in directorys:
            push_dirs += dirs + ","
        push_dirs = push_dirs[:-1]
        config['SORT_DIRECTORY']['directorys'] = push_dirs
        config.remove_section(directory)
        write()
        blocks()

# delete extesnions


def delete_extension(extension, directory):
    exten_push = ""
    extensions = config[directory]['extensions'].split(",")
    extensions.remove(extension)
    for exten in extensions:
        exten_push += exten + ","
    exten_push = exten_push[:-1]
    if not exten_push:
        exten_push = "None"
    config[directory]['extensions'] = exten_push
    write()
    extension_edit(directory)


#GUI#

# make the layout for every directory you made to sort


def count_col():
    global collumn_count
    collumn_count += 1
    return collumn_count


def blocks():
    global label_check, l_block, collumn_count, e_extension
    if label_check:
        l_block.destroy()
    l_block = Label(root)
    row = 3
    for sort_dir in config['SORT_DIRECTORY']['directorys'].split(","):
        if sort_dir:
            row += 1
            l_section = Label(l_block, text=sort_dir.upper())
            l_text_extensions = Label(
                l_block, text="The extesions it filters:")
            l_extensions = Label(
                l_block, text=config[sort_dir.upper()]['extensions'])
            l_text_entry = Label(l_block, text="Extension to filter:")
            e_extension = Entry(l_block, textvariable=e_extension)
            b_entry = Button(
                l_block, command=lambda sort_dir=sort_dir, e_extension=e_extension: extensions(e_extension.get().lower(), sort_dir.upper()), text="Add extension")
            b_extension_edit = Button(
                l_block, command=lambda sort_dir=sort_dir: extension_edit(sort_dir.upper()), text="Edit extensions")
            b_sorting = Button(
                l_block, command=lambda sort_dir=sort_dir: path("path_sort", sort_dir.upper()), text="Select sorting directory:")
            b_placing = Button(
                l_block, command=lambda sort_dir=sort_dir: path("path_place", sort_dir.upper()), text="Select placing directory:")
            l_path_sort = Label(
                l_block, text=config[sort_dir.upper()]['path_sort'])
            l_path_place = Label(
                l_block, text=config[sort_dir.upper()]['path_place'])
            b_delete = Button(
                l_block, command=lambda sort_dir=sort_dir: delete(sort_dir.upper()), text="Delete this")
            # packing
            l_section.grid(column=count_col(), row=row)
            l_text_extensions.grid(column=count_col(), row=row)
            l_extensions.grid(column=count_col(), row=row)
            l_text_entry.grid(column=count_col(), row=row)
            e_extension.grid(column=count_col(), row=row)
            b_entry.grid(column=count_col(), row=row)
            b_extension_edit.grid(column=count_col(), row=row)
            b_sorting.grid(column=count_col(), row=row)
            l_path_sort.grid(column=count_col(), row=row)
            b_placing.grid(column=count_col(), row=row)
            l_path_place.grid(column=count_col(), row=row)
            b_delete.grid(column=count_col(), row=row)
            collumn_count = 0
    # end for loop
    l_block.grid()
    label_check = True


def extension_edit(directory):
    global l_edit_block, label_check_edit
    blocks()

    def close():
        l_edit_block.destroy()
    if label_check_edit:
        l_edit_block.destroy()
    l_edit_block = Label(root)
    l_edit_block.grid()
    if not config[directory]['extensions'] == "None":
        for extension in config[directory]['extensions'].split(","):
            b_delete_extension = Button(
                l_edit_block, command=lambda extension=extension: delete_extension(extension, directory), text=f"Delete the {extension} extension")
            b_delete_extension.grid()
        b_close_edit = Button(
            l_edit_block, command=close, text="Close")
        b_close_edit.grid(sticky="e")
    label_check_edit = True

# make a directory


b_add_sort = Button(root, command=add_sort, text="+")
b_add_sort.grid()
e_add = Entry(root)
e_add.grid()
b_run = Button(root, command=lambda: mapsort, text="Run")
b_run.grid()

#startup#


if config.has_section('SORT_DIRECTORY'):
    section_check()
    write()
    blocks()

mainloop()
