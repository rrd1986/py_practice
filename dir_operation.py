from genericpath import isdir
import os



def list_dir(path: str):
    file_list = os.listdir(path)
    for file in file_list:
        print(os.path.abspath(file))
        if os.path.isdir(os.path.abspath(file)):
            list_dir(file)

#list_dir("C:\\Users\\Rashmi\\Desktop\\db_mail")
print("\n")
list_dir("C:\\Users\\Rashmi\\Desktop\\py_concurrency_test")