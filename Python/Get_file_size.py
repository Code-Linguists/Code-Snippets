''' Get file size '''
import os
STATINFO = os.stat('testimage.jpg')
FILESIZE = (STATINFO.st_size)
print(FILESIZE, "Bytes")