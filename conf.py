import configparser
from tkinter import *
from tkinter import filedialog

config = configparser.ConfigParser()
config.read('settings.ini')

# FIXME make 1 function for all types
# Select a directory to be sorted


def browse_button_sort():
    global folder_path_srt
    filename = filedialog.askdirectory()
    if filename:
        config['SORT'][''] = filename
    folder_path_srt.set(config['SORT']['path'])

# Select a directory to put image files in and what extensions


def browse_button_img():
    global folder_path_img
    filename = filedialog.askdirectory()
    if filename:
        config['IMAGES']['path'] = filename
    folder_path_img.set(config['IMAGES']['path'])

# Select a directory to put text files in and what extensions


def browse_button_txt():
    global folder_path_txt
    filename = filedialog.askdirectory()
    if filename:
        config['TEXT']['path'] = filename
    folder_path_txt.set(config['TEXT']['path'])


#GUI#

root = Tk()
folder_path_srt = StringVar()
folder_path_img = StringVar()
folder_path_txt = StringVar()
folder_path_srt.set(config['SORT']['path'])
folder_path_img.set(config['IMAGES']['path'])
folder_path_txt.set(config['TEXT']['path'])
# srt
main_l_srt = Label(master=root, textvariable=folder_path_srt)
main_l_srt.grid(row=0, column=1)
button_srt = Button(text="Select directory sort", command=browse_button_sort)
button_srt.grid(row=0, column=3)
# img
main_l_img = Label(master=root, textvariable=folder_path_img)
main_l_img.grid(row=1, column=1)
button_img = Button(text="Select directory foto", command=browse_button_img)
button_img.grid(row=1, column=3)
# txt
main_l_txt = Label(master=root, textvariable=folder_path_txt)
main_l_txt.grid(row=2, column=1)
button_txt = Button(text="Select directory text", command=browse_button_txt)
button_txt.grid(row=2, column=3)
# TODO add al extension types


mainloop()


#write the code in settings.ini file#
with open('settings.ini', 'w') as f:
    config.write(f)
