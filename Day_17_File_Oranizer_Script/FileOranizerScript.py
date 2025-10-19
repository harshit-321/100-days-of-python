import os
import shutil

path = input("Enter folder path: ")

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext == "":
        continue
    if not os.path.exists(os.path.join(path, ext)):
        os.makedirs(os.path.join(path, ext))
    shutil.move(os.path.join(path, file), os.path.join(path, ext, file))

print("Files Organized Successfully!")
