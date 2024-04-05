import os 
# find files, directories, user choice than get anser according users choice.


def list_dir(dir_path):
    sca_0 = os.scandir(dir_path)                                         #code scan path and serch about directories
    for dir in sca_0:                                                           # if find directories 
        if dir.is_dir():
            print(dir.name)                                                          # print direcktories name
    return sca_0


def list_files(dir_path):
    sca_1 = os.scandir(dir_path)                                      # find files
    for fil in sca_1:
        if fil.is_file():
            print(fil.name)
    return sca_1
    
 #path 
path_0 = r"C:\Users\shaom\OneDrive\Desktop\python_course\assignment-03"                       # map which will be scanned

path_1 = r"C:\Users\shaom\OneDrive\Desktop\python_course\assignment-03"

#choices which user will choice of :
while True:
    print()
    print("1. List directories")
    print("2. Change directory")
    print("3. list files")
    print("4. Quit") 
    print()
    choice_i = input("==> ")
    if choice_i == "1":                             #get list of directories
      list_dir(path_0)                                       

    elif choice_i == "2": 

        by_choice_ii = input("Name of directory to enter: ")                # user will get a massage for choice any name of directory then will get again chocies 
        print()
        change = os.path.join(path_0, by_choice_ii)
        
    elif choice_i =="3":                       # if user choice 3, will wirten all files which find such as a list
        list_files(path_1)
        print()
    
    elif choice_i =="4":       
        break                          # program end