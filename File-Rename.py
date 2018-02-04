import os
old = input('输入被替换的文件名:')
new = input('这个文件名会被替换为:')
for file in os.listdir('.'): os.rename(file, file.replace(old, new))
