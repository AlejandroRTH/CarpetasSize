import os
from os.path import join, getsize
for root, dirs, files in os.walk('D:\CARPETAS\Docu\Python\FolderSize'):
    # print(root, "consumes ")
    # print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
    if '.git' in dirs:
        dirs.remove('.git') # don't visit CVS directories