import os

data_path = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in data_path.items():
    if os.path.exists(root):
        print(root, 'Папка существует')
    else:
        for folder in folders:
            path_dir = os.path.join(root, folder)
            os.makedirs(path_dir)

