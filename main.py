import os
import shutil


mylist = os.listdir("../../../testrange")
path = "../../../testrange"
fotos = ["fotos", ".jpeg", ".jpg", ".png"]
music = ["music", ".mp3"]
ingepakt = ["ingepakt", ".zip", ".rar"]
text = ["text", ".txt"]
file_types = [fotos, music, ingepakt, text]

for x in file_types:
    for file_extension in x:
        for q in mylist:
            if q.lower().endswith(file_extension):
                shutil.move(f"{path}/{q}", f"{path}/{x[0]}")
