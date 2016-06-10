def finddiffs_of_two_files(input_file1, input_file2):
    """
    takes two --files-- as inputs and returns
    diffs b/w the files as a 'string'
    """
    import subprocess
    import sh
    p = subprocess.Popen(['git', 'diff', "--color", "--no-index", "--word-diff=plain", input_file1, input_file2],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    return out


def finddiffs_of_two_strings(str1, str2):
    import tempfile
    tempone = tempfile.NamedTemporaryFile(suffix='_suffix', prefix='prefix_', dir='.',)
    temptwo = tempfile.NamedTemporaryFile(suffix='_suffix', prefix='prefix_', dir='.',)
    try:
        stringone = ""
        stringtwo = ""
        tempone.write(str1)
        tempone.seek(0)
        temptwo.write(str2)
        temptwo.seek(0)
        stringone = str(tempone.name)
        stringtwo = str(temptwo.name)
        return finddiffs_of_two_files(stringone, stringtwo)
    finally:
        tempone.close()
        temptwo.close()

#print finddiffs_of_two_strings("some data", "some stuff")
#print finddiffs_of_two_files("hello1.txt", "hello2.txt")
