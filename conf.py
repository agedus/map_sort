import configparser
from tkinter import *
from tkinter import filedialog

config = configparser.ConfigParser()
config.read('settings.ini')


#Select a directory to be sorted#


def browse_button_sort():
    global folder_path_sort
    filename = filedialog.askdirectory()
    if filename:
        config['PATHS']['sort_directory'] = filename
    folder_path_sort.set(config['PATHS']['sort_directory'])

#Select a directory to put image files in and what extensions#


def browse_button_img():
    global folder_path_img
    filename = filedialog.askdirectory()
    if filename:
        config['PATHS']['img_directory'] = filename
    folder_path_img.set(config['PATHS']['img_directory'])


#GUI#

root = Tk()
folder_path_sort = StringVar()
folder_path_img = StringVar()
folder_path_sort.set(config['PATHS']['sort_directory'])
folder_path_img.set(config['PATHS']['img_directory'])
# sort
main_l_sort = Label(master=root, textvariable=folder_path_sort)
main_l_sort.grid(row=0, column=1)
button_sort = Button(text="Select directory", command=browse_button_sort)
button_sort.grid(row=0, column=3)
# img
main_l_img = Label(master=root, textvariable=folder_path_img)
main_l_img.grid(row=1, column=1)
button_img = Button(text="Select directory", command=browse_button_img)
button_img.grid(row=1, column=3)


mainloop()


#write the code in settings.ini file#
with open('settings.ini', 'w') as f:
    config.write(f)
