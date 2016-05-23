from django.shortcuts import render

# Create your views here.

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
