import sh
import os
from tempfile import NamedTemporaryFile, mkdtemp

"""
def make_a_file_in_a_dir(temp_dir):
    sh.tar("cd", temp_dir)
    sh.tar("git", "init")
    temp_file = NamedTemporaryFile(delete=True, dir=".")
    return temp_file
"""


def find_diffs(input_file1, input_file2):
    if os.path.exists(input_file1) and os.path.exists(input_file2):
        try:
            temp_dir = mkdtemp(prefix="gittemp", dir=os.getcwd())
            #temp_file = make_a_file_in_a_dir(temp_dir)
            print"----------------"
            print temp_dir
            print"----------------"
            sh.cd(temp_dir)
            print(sh.pwd())
            #sh.tar("cd", temp_dir)
            #sh.tar("git", "init")
            sh.git("init")
            print"----------------"
            print(sh.ls("-al"))
            print"----------------"
            temp_file = NamedTemporaryFile(delete=True, dir=".")
            print"----------------"
            print(sh.ls("-al"))
            print"----------------"
            #either spawn a subprocess if needed
            #temp_file.write(input_file1.read())
            temp_file.write("hello world")
            print temp_file.read()
            sh.tar("git","add",".")
            temp_file.write(input_file2.read())
            print(temp_file.read())
            print sh.git("diff")
            #tempf.seek(0)
            #print(tempf.read())
            #tempf.close()
        finally:
            os.rmdir(temp_dir)
    else:
        print"File dosen't exist"

find_diffs("hello1.txt", "hello2.txt")
