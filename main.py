import os
import shutil


mylist = os.listdir("../../../testrange")

path = "../../../testrange"

for x in mylist:
    if x == "test_txt.txt":
        shutil.move(f"{path}/{x}", f"{path}/txt")
