import os

with open("output/output.txt", "w", encoding="utf-8") as f:
    for dirpath, dirnames, filenames in os.walk('./'):
        print(f'目录: {dirpath}')
        f.write(f'目录: {dirpath}\n')
        for filename in filenames:
            print(f'文件: {os.path.join(dirpath, filename)}')
            f.write(f'文件: {os.path.join(dirpath, filename)}\n')
