import os

for dirpath, dirnames, filenames in os.walk('你的目录路径'):
    print(f'目录: {dirpath}')
    for filename in filenames:
        print(f'文件: {os.path.join(dirpath, filename)}')
