from sh import git
import os
from tempfile import NamedTemporaryFile, mkdtemp


def find_diffs(input_file1, input_file2):
    import subprocess
    p = subprocess.Popen(['git', 'diff', "--no-index", input_file1, input_file2], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    print out
    print type(out)
find_diffs("hello1.txt", "hello2.txt")
