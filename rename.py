import os
import string

def rename_files():
    file_list = os.listdir(r"C:\Users\gopi\Documents\Python\prank")
    #print(file_list)
    current_dir = os.getcwd()
    os.chdir(r"C:\Users\gopi\Documents\Python\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
     #   print(file_name)
     #os.chdir(current_dir)

rename_files()
