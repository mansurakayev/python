import os, os.path

#1 Rename Directory
os.chdir(r"C:/")
os.rename("Test","Test1")
#2 Print number of files
dir = "C:/Test1"
print (len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]))
#3 Print number of directories
dir = "C:/Test1"
def get_dirs(dir_path: str):
    subfolders = [f.path for f in os.scandir(dir_path) if f.is_dir()]
    return subfolders
print(len(get_dirs(dir)))
print(*get_dirs(dir),sep="\n")
#4 List content of the directory
print(*os.listdir(dir),sep="\n")
#5 Add file and new directory to this directory
os.chdir(r"C:/Test1")
File = open("Test1.txt", "w")
os.mkdir("3")
