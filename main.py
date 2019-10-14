import os
import time
import shutil


path = "C:/Users/basse/Downloads"
fotos = ["jpeg", "jpg", "png"]
text = ["txt", "pdf"]
extensions = [{"C:/Users/basse/Pictures/downloads": fotos},
              {"C:/Users/basse/Documents/downloads": text}]
skip = ["ini", "part"]
downloads = os.listdir("C:/Users/basse/Downloads")


def sorting():
    for d_file in downloads:
        file_extension = d_file.split(".")[-1]
        for i in extensions:
            for j in i:
                if file_extension in skip:
                    print(f"bestand: {d_file} skipt")
                    continue
                elif d_file + ".part" in downloads:
                    print(
                        f"bestand: {d_file} heeft nog een .part file")
                    continue
                elif file_extension in i[j]:
                    print(f"bestand: {d_file} gaat naar {j}/{d_file}")
                    shutil.move(f"{path}/{d_file}", f"{j}/{d_file}")
                else:
                    print(f"bestand: {d_file} gaat naar onbekend")
                    shutil.move(f"{path}/{d_file}",
                                f"D:/unknown _downloads/{d_file}")

        # while True:
        #     mylist = os.listdir("C:/Users/basse/Downloads")
        #     time.sleep(1)
        #     if "desktop.ini" in mylist:
        #         if len(mylist) >= 2:
        #             print(mylist)
        #             sorting()
        #     else:
        #         if len(mylist) >= 1:
        #             print(mylist)
        #             sorting()


sorting()
