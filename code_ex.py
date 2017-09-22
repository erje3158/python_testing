from tempfile import mkstemp
from shutil import move
from os import fdopen, remove

import subprocess

def plot(plot_script,file_path):
    command = 'Rscript'
    cmd = [command, plot_script, file_path]
    print(cmd)
    subprocess.call(cmd)

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
    replace('rand.txt','//IFDEF OPENACC','//~~~~~~~~~~~~~~')
    with open('rand.txt') as file:
        for line in file:
            print(line)
    replace('rand.txt','//~~~~~~~~~~~~~~','//IFDEF OPENACC')

    print("####      Plotting Stuff in R      ####")
    plot('quad_plot.R','quad.csv')

if __name__ == "__main__": 
    main()
