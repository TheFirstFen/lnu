import os 

# find in which dir and file:

def count_directories(dir_path): 
    lst = os.scandir(dir_path)                 #print directories
    count = 0
    for dir_coun in lst:
        if dir_coun.is_dir():                 #count directories
            count += 1
    return count
   
    # find all files 
def count_files(dir_path): 
    lst = os.scandir(dir_path)              #scan path 
    count = 0
    for dir_coun in lst:
        if dir_coun.is_file():               #count fils
            count += 1
    return count

path = r"C:\Users\shaom\OneDrive\Desktop\python_course\assignment-03"
print(f"I am right now at: {path}")
print(f"Below me I have {count_directories(path)} directories/folders")
print(f"This directory contains {count_files(path)} files")
