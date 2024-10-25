import os 
def read_file(file):                #read file
    with open(file, 'r') as f:
        l_s = f.readlines()              # read all lines in file
    lst = " " #str()

    for l in l_s:
        l = l.strip()                   #clean lines
        if l:
            lst += f"{l}\n"
        else:
            lst += '\n'                 # hope to another row
    return lst

def write_file(file, path):
    with open(path, 'w') as f_:       #read and write text 
        f_.write(file)



path = os.path.join(os.getcwd(),'mamma_mia.txt')
file = read_file(path)
out_put = os.path.join(os.getcwd(), "mamma_mia_output.txt")
write_file(file, out_put)


            


