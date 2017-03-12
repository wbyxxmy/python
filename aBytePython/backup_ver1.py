# !/usr/bin/python
# Filename: backup_ver1.py

import os
import time

source = ['"D:\\learn\\python\\file1"','"D:\\learn\\python\\file2"']

spaces in it.

target_dir = 'D:\learn\python\backup'

using

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
	print("Successful backup to", target)
else:
	print("Backup FAILED") 