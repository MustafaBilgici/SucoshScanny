import os
import re

dangerous_functions = ['eval', 'exec', 'unserialize']

def check_for_rce(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()
        for function in dangerous_functions:
            if re.search(f'{function}\(', contents):
                if re.search(r'(req(uest)?\.body|req(uest)?\.query|req(uest)?\.params)', contents):
                    return True
    return False

def scan_directory_for_rce(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                if check_for_rce(file_path):
                    print(f'RCE vulnerability found in {file_path}')

