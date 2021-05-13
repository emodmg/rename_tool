# -*- coding: utf-8 -*-
import sys
import os
import getopt
#python3 rename_tool.py -p ./test -n 20 -f win 
# help rename_tool.py to do

def rename(path, num, prefix):
    
    #argv = sys.argv[1:]
    num = int(num)
    files = os.listdir(path)# ignore the hidden file
    files = sorted(files)
    for file in files:
        fpath = path + '/' + file
        if (os.path.isdir(fpath)):
            num = rename(fpath, num, prefix)
            #os.rename(os.path.join(path, file), os.path.join(path, prefix + file))
        else:
            suffix = os.path.splitext(file)[1]
            if (file == ".DS_Store"):# todo start with dot
                print(file)
                continue;
            print(file)
            os.rename(os.path.join(path, file), os.path.join(path, prefix + str(num) + suffix))
            num += 1
    return num
 
if __name__ == '__main__':
    path = None
    num = None
    prefix = None
    argv = sys.argv[1:]
    #length = len(sys.argv)
    #argv_list = str(sys.argv)
    #print(argv_list)
 
    try:
        opts, args = getopt.getopt(argv, 'p:n:f:')
    except:
        print("Error")
        print("""usage: %s [-f|-n|-p]
        -f, file prefix input
        -p: folder exexcution path input
        -n: 'renaming number starting point"""%sys.argv[0])
    for opt, arg in opts:
        if opt in ['-p']:
        	path = arg
        elif opt in ['-n']:
        	num = arg
        elif opt in ['-f']:
        	prefix = arg
    print(rename(path, num, prefix))
