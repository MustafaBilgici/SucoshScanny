import os
import re

def scan_node_files_lfi(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".js"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    file_contents = f.read()
                    if re.search(r'require\(', file_contents) or re.search(r'readFile\(', file_contents):
                        if re.search(r'process.argv\[', file_contents) or re.search(r'process.env\[', file_contents) or re.search(r'request.query\[', file_contents) or re.search(r'request.body\[', file_contents) or re.search(r'request.params\[', file_contents) or re.search(r'$_GET\[', file_contents) or re.search(r'$_POST\[', file_contents):
                            print(f"Potential LFI vulnerability found in {file_path}")

