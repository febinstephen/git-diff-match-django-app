#from sh import git
#import os
#from tempfile import NamedTemporaryFile, mkdtemp


def find_diffs(input_file1, input_file2):
    """
    takes two --files-- as inputs and returns
    diffs b/w the files as a 'string'
    """
    import subprocess
    p = subprocess.Popen(['git', 'diff', "--no-index", input_file1, input_file2],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    f = open("diffs", 'w')
    f.write(out)
    return out


def difftohtml(input_file):
    f = open(input_file, 'r')
    for line in f.readlines():
        if line[0] == '-':
            print '<del>' + line + '</del>' + '\n'
        elif line[0] == '+':
            print '<ins>' + line + '</ins>' + '\n'


#print find_diffs("hello1.txt", "hello2.txt")
difftohtml("diffs")
