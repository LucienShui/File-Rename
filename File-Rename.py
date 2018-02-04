import os
print('Input the substring of file name you want to replace:')
old = input()
print('You want this string be replaced to:')
new = input()
for file in os.listdir('.'):
    if file[-2: ] == 'py': continue
    os.rename(file, file.replace(old, new))
