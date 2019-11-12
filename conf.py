import configparser
from tkinter import *
from tkinter import filedialog

config = configparser.ConfigParser()
config.read('settings.ini')

root = Tk()
root.maxsize()

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
    new_directory = e_add.get().lower().replace(" ", "")
    if not config.has_section('SORT_DIRECTORY'):
        config.add_section('SORT_DIRECTORY')
        config['SORT_DIRECTORY']['directorys'] = new_directory.lower()
    else:
        directorys = config['SORT_DIRECTORY']['directorys'].split(",")
        if e_add.get():
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
    e_add.delete(0, 'end')
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
    # titels
    l_name_titel = Label(l_block, text="Name:")
    l_extension_titel = Label(l_block, text="Extensions to filter:")
    l_sort_titel = Label(l_block, text="Sorting directory:")
    l_place_titel = Label(l_block, text="Placing directrory:")
    l_add_extension_titel = Label(l_block, text="Add extension:")
    l_select_titel = Label(l_block, text="Select directory:")
    l_edit_titel = Label(l_block, text="Edit:")
    # packing titels
    l_name_titel.grid(column=0, row=0)
    l_extension_titel.grid(column=1, row=0)
    l_sort_titel.grid(column=2, row=0)
    l_place_titel.grid(column=3, row=0)
    l_add_extension_titel.grid(column=4, row=0)
    l_select_titel.grid(column=5, row=0)
    l_edit_titel.grid(column=6, row=0)
    # columns
    l_name = Label(l_block, bg="green", bd=10)
    l_extension = Label(l_block, bg="blue", bd=10)
    l_sort = Label(l_block, bg="purple", bd=10)
    l_place = Label(l_block, bg="red", bd=10)
    l_add_extension = Label(l_block, bg="yellow", bd=10)
    l_select = Label(l_block, bg="pink", bd=10)
    l_edit = Label(l_block, bg="orange", bd=10)
    # packing columns
    l_name.grid(column=0, row=1, sticky=N)
    l_extension.grid(column=1, row=1, sticky=N)
    l_sort.grid(column=2, row=1, sticky=N)
    l_place.grid(column=3, row=1, sticky=N)
    l_add_extension.grid(column=4, row=1, sticky=N)
    l_select.grid(column=5, row=1, sticky=N)
    l_edit.grid(column=6, row=1, sticky=N)
    #
    row = 3
    for sort_dir in config['SORT_DIRECTORY']['directorys'].split(","):
        if sort_dir:
            row += 1
            l_section = Label(l_name, text=sort_dir.upper(), bg="green")
            l_extensions = Label(
                l_extension, text=config[sort_dir.upper()]['extensions'], bg="blue")
            l_path_sort = Label(
                l_sort, text=config[sort_dir.upper()]['path_sort'], bg="purple")
            l_path_place = Label(
                l_place, text=config[sort_dir.upper()]['path_place'], bg="red")
            e_extension = Entry(l_add_extension, textvariable=e_extension)
            b_entry = Button(
                l_add_extension, command=lambda sort_dir=sort_dir, e_extension=e_extension: extensions(e_extension.get().lower(), sort_dir.upper()), text="Add extension")
            b_placing = Button(
                l_select, command=lambda sort_dir=sort_dir: path("path_place", sort_dir.upper()), text="Placing directory")
            b_sorting = Button(
                l_select, command=lambda sort_dir=sort_dir: path("path_sort", sort_dir.upper()), text="Sorting directory")
            b_extension_edit = Button(
                l_edit, command=lambda sort_dir=sort_dir: extension_edit(sort_dir.upper()), text="Edit extensions")
            b_delete = Button(
                l_edit, command=lambda sort_dir=sort_dir: delete(sort_dir.upper()), text="Delete this row")
            # packing
            l_section.grid(column=count_col(), row=row, padx=30, pady=9)
            l_extensions.grid(column=count_col(), row=row, padx=30, pady=9)
            l_path_sort.grid(column=count_col(), row=row, padx=30, pady=9)
            l_path_place.grid(column=count_col(), row=row, padx=30, pady=9)
            e_extension.grid(column=count_col(), row=row, padx=30, pady=10)
            b_entry.grid(column=count_col(), row=row)
            b_placing.grid(column=count_col(), row=row, padx=20, pady=(6, 7))
            b_sorting.grid(column=count_col(), row=row, padx=20, pady=(6, 7))
            b_extension_edit.grid(
                column=count_col(), row=row, padx=20, pady=(6, 7))
            b_delete.grid(column=count_col(), row=row, padx=20, pady=(6, 7))
            #
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
# b_run = Button(root, command=lambda: mapsort, text="Run")
# b_run.grid()

#startup#


if config.has_section('SORT_DIRECTORY'):
    section_check()
    write()
    blocks()

mainloop()
