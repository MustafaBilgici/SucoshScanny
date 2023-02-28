import os
import re

# tehlikeli fonksiyonların regex'leri
dangerous_functions = [
    r'http\.get\(',
    r'https\.get\(',
    r'request\(',
    r'axios\.get\(',
    r'fetch\('
]

def scan_directory_ssrf(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.js'):
                full_path = os.path.join(root, file)
                scan_file(full_path)

def scan_file(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()
        for dangerous_function in dangerous_functions:
            if re.search(dangerous_function, contents):
                inputs = re.findall(r'(req(uest)?\.query\[.+?\]|req(uest)?\.body\[.+?\])', contents)
                for input in inputs:
                    if re.search(r'http[s]?://', input):
                        print(f'Potential SSRF: {file_path} - {dangerous_function} - {input}')