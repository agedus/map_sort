import os
import time
import shutil


path = "C:/Users/basse/Downloads"
fotos = ["jpeg", "jpg", "png"]
text = ["txt", "pdf"]
extensions = [{"C:/Users/basse/Pictures/downloads": fotos},
              {"C:/Users/basse/Documents/downloads": text}]
skip = ["ini", "part"]
downloads = None


def sorting():
    print("0")
    for d_file in downloads:
        print("1")
        value = None
        src = None
        dst = None
        file_extension = d_file.split(".")[-1]
        for i in extensions:
            print("2")
            if file_extension in skip:
                value = f"bestand: {d_file} skipt"
            elif d_file + ".part" in downloads:
                value = f"bestand: {d_file} heeft nog een .part file"
            else:
                for j in i:
                    print("3")
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
            print(mylist)
            sorting()
    else:
        if len(mylist) >= 1:
            print(mylist)
            sorting()
