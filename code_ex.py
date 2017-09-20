from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

def plot(file_path):
    print(file_path)

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                new_file.write(line.replace(pattern, subst))
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

def main():
    print("\n\n\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("           TESTING PYTHON              ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\n\n\n")

    print("#### Find/Replace Strings in File  ####")
    replace('main.cpp','//IFDEF OPENACC','//~~~~~~~~~~~~~~')
    with open('main.cpp') as file:
        for line in file:
            print(line)
    replace('main.cpp','//~~~~~~~~~~~~~~','//IFDEF OPENACC')

    print("####   Plotting Stuff in gnuplot   ####")
    plot('quad.gold')

if __name__ == "__main__": 
    main()
