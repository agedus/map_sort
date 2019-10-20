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


def browse_button_sort():
    global folder_path_srt
    filename = filedialog.askdirectory()
    if filename:
        config['SORT']['path'] = filename
    folder_path_srt.set(config['SORT']['path'])


# Select a directory to put image files in and what extensions and commit the exentesions to filter


def browse_button_img():
    global folder_path_img
    filename = filedialog.askdirectory()
    if filename:
        config['IMAGES']['path'] = filename
    folder_path_img.set(config['IMAGES']['path'])


def push_button_img(event):
    extension = entry_img.get()
    if extension not in extension_array_img:
        extension_array_img.append(extension)
    entry_img.delete(0, 'end')


def commit_button_img():
    push_extensions = ""
    for extension in extension_array_img:
        extension = extension.replace(" ", "")
        push_extensions += extension + ","
    push_extensions = push_extensions[:-1]
    if push_extensions:
        config['IMAGES']['extensions'] = push_extensions
    extensions_img.set(config['IMAGES']['extensions'])

# Select a directory to put text files in and what extensions and commit the exentesions to filter


def browse_button_txt():
    global folder_path_txt
    filename = filedialog.askdirectory()
    if filename:
        config['TEXT']['path'] = filename
    folder_path_txt.set(config['TEXT']['path'])


def push_button_txt(event):
    extension = entry_txt.get()
    if extension not in extension_array_txt:
        extension_array_txt.append(extension)
    entry_txt.delete(0, 'end')


def commit_button_txt():
    push_extensions = ""
    for extension in extension_array_txt:
        extension = extension.replace(" ", "")
        push_extensions += extension + ","
    push_extensions = push_extensions[:-1]
    if push_extensions:
        config['TEXT']['extensions'] = push_extensions
    extensions_txt.set(config['TEXT']['extensions'])


#GUI#
# TODO make one layout to use multiple times
folder_path_srt = StringVar()
folder_path_img = StringVar()
folder_path_txt = StringVar()
extensions_img = StringVar()
extensions_txt = StringVar()
folder_path_srt.set(config['SORT']['path'])
folder_path_img.set(config['IMAGES']['path'])
folder_path_txt.set(config['TEXT']['path'])
extensions_img.set(config['IMAGES']['extensions'])
extensions_txt.set(config['TEXT']['extensions'])

# srt
main_l_srt = Label(root, textvariable=folder_path_srt)
main_l_srt.grid(row=0, column=1)
button_srt = Button(root, text="Select directory sort",
                    command=browse_button_sort)
button_srt.grid(row=0, column=3)

# img
main_l_img = Label(root, textvariable=folder_path_img)
main_l_img.grid(row=1, column=1)
button_img = Button(root, text="Select directory foto",
                    command=browse_button_img)
button_img.grid(row=1, column=3)
entry_img = Entry(root)
entry_img.grid(row=4, column=1)
entry_img.bind('<Return>', push_button_img)
button_img_entry = Button(root, text="commit exetension foto",
                          command=commit_button_img)
button_img_entry.grid(row=4, column=3)
main_l_img = Label(root, textvariable=extensions_img)
main_l_img.grid(row=4, column=5)


# txt
main_l_txt = Label(root, textvariable=folder_path_txt)
main_l_txt.grid(row=2, column=1)
button_txt = Button(root, text="Select directory text",
                    command=browse_button_txt)
button_txt.grid(row=2, column=3)
entry_txt = Entry(root)
entry_txt.grid(row=5, column=1)
entry_txt.bind('<Return>', push_button_txt)
button_txt_entry = Button(root, text="commit exetension text",
                          command=commit_button_txt)
button_txt_entry.grid(row=5, column=3)
main_l_txt = Label(root, textvariable=extensions_txt)
main_l_txt.grid(row=5, column=5)
# TODO add al extension types


mainloop()


#write the code in settings.ini file#
with open('settings.ini', 'w') as f:
    config.write(f)
