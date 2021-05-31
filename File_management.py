#!/usr/bin/env python
# coding: utf-8

# In[3]:
import os
import subprocess
import zipfile
from sys import platform

def Folder_Size(dir_path):
    total = sum(os.path.getsize(os.path.join(path, f)) 
        for path, dirs, files in os.walk(dir_path) for f in files)
    print(total,"byte")
    total_gb = total/(1024*1024*1024)
    return total

def file_deleted(dir_path, extension): #하위 모든 폴더 확장자 삭
    if os.path.exists(dir_path):
        if os.path.isdir(dir_path):
            for root_folder, folders, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root_folder, file)
                    file_extension = os.path.splitext(file_path)[1]
                    if extension == file_extension:
                        if not os.remove(file_path):
                            print(f"{file_path} deleted successfully") 
                        else:
                            print(f"Unable to delete the {file_path}")
        else:
            print(f"{dir_path} is not a directory")
    else:
        print(f"{dir_path} doesn't exist")
        

def Folder_Open(dir_path):
    if any([platform.startswith(os_name) for os_name in ['linux', 'darwin', 'freebsd']]):
        subprocess.Popen(['xdg-open', dir_path])
    elif platform.startswith('win'):
        os.startfile(dir_path)
        
# In[ ]:


def file_zip(zip_dir,file_dir,zip_name):
    os.chdir(file_dir)
    ## check the current working directory
    os.getcwd()
    ## show the lists of files in the current working directory
    file_list=os.listdir()
    with zipfile.ZipFile(zip_dir+"\\"+zip_name, 'w') as myzip_all:
        for f in file_list:
            myzip_all.write(f,compress_type = zipfile.ZIP_DEFLATED)
        #print(f, 'is written to myzip_all.zip')
        myzip_all.close()
    myzip_all.namelist()


def zip_open(zip_file, open_dir):        
    fantasy_zip = zipfile.ZipFile(zip_file)
    fantasy_zip.extractall(open_dir)
    fantasy_zip.close()


