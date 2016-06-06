def find_diffs(input_file1, input_file2):
    """
    takes two --files-- as inputs and returns
    diffs b/w the files as a 'string'
    """
    import subprocess
    p = subprocess.Popen(['git', 'diff', "--no-index", input_file1, input_file2],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    diffs = out.split("\n")
    diffs_list = list()
    for line in diffs:
        str = ""
        if line.startswith('-'):
            str = '<del>' + line + '</del>'
            diffs_list.append(str)
        elif line.startswith('+'):
            str = '<ins>' + line + '</ins>'
            diffs_list.append(str)
    return diffs_list

#print find_diffs("hello1.txt", "hello2.txt")
