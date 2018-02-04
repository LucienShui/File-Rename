import os
print('输入被替换的文件名:')
old = input()
print('这个文件名会被替换为:')
new = input()
for file in os.listdir('.'):
    if file[-2: ] == 'py': continue
    os.rename(file, file.replace(old, new))
