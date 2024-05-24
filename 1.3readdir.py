import os
directory_path = 'C:/Users/sanke/Desktop/SEM 6/OS'
with os.scandir(directory_path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f'File: {entry.name}')
                elif entry.is_dir():
                    print(f'Folder: {entry.name}')