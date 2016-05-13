import sh
import os
#print(ifconfig("wlan0"))
#print(sh.ls("-l"))


def find_diffs(file_name1, file_name2):
    if os.path.exists(file_name1) and os.path.exists(file_name2):
        return True
    else:
        return False
print find_diffs("test_diffmatch.py", "finddiff.py")


import tempfile

# Use the TemporaryFile context manager for easy clean-up
with tempfile.TemporaryFile() as tmp:
    # Do stuff with tmp
    tmp.write('stuff')

# Clean up a NamedTemporaryFile on your own
# delete=True means the file will be deleted on close
tmp = tempfile.NamedTemporaryFile(delete=True)
try:
    # do stuff with temp
    tmp.write('stuff')
finally:
    tmp.close()  # deletes the file

# Handle opening the file yourself. This makes clean-up
# more complex as you must watch out for exceptions
fd, path = tempfile.mkstemp()
try:
    with os.fdopen(fd, 'w') as tmp:
        # do stuff with temp file
        tmp.write('stuff')
finally:
    os.remove(path)
