'''
- Put this file into the directory you want to divide
- For every 100 file, it will create a directory and move all to it.
'''
import os
import shutil

def mover(cnt):
    files = os.listdir(".")
    myList = ["txt","jpg","png"] #the extensions we want
    image_files = [file for file in files if file.split(".")[1] in myList]
    n = len(image_files)
    num = int(n / cnt)  # // also works
    folder_list = []
    for i in range(0,num+1):
        os.mkdir(f"folder_{i}")
        folder_list.append(f"folder_{i}")

    
    count = 1
    for file in image_files:
        ff = int(count/(cnt+1))
        shutil.move(file, f"folder_{ff}")
        count += 1


if __name__ == "__main__":
    mover(100)
    
    
