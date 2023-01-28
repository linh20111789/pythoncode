import os

path = r"D:\DataAnalyst\mpython"

directory_list = os.listdir(path)




for filename in directory_list:
    src = filename
    dst = filename[filename.find('_') + 1:]

    # print(dst)
    if os.path.join(path, src) != os.path.join(path, dst):
        os.rename(os.path.join(path, src), os.path.join(path, dst))

print("File renamed!")