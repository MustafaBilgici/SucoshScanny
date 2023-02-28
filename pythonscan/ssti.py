import os
import re
from termcolor import colored



def find_files_to_check(path):
    py_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".py"):
                py_files.append(os.path.join(dirpath, filename))
    return py_files
#mail functions
def check_for_ssti(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        if re.search(r"request.method", file_contents) or re.search(r"request.POST.get", file_contents) or re.search(r"request.GET.get", file_contents):
            if re.search(r"\{\{.*\}\}", file_contents) or re.search(r"\{%.*%\}", file_contents) or re.search(r"str\((.*)\)", file_contents):
                lines = file_contents.split('\n')
                for i, line in enumerate(lines):
                    if re.search(r"\{\{.*\}\}", line) or re.search(r"\{%.*%\}", line) or re.search(r"str\((.*)\)", line):
                        print(colored(f"[+] Possible SSTI vulnerability found in {file_path} on line {i+1}: {line}","red"))
            else:
                print(colored(f"[-] No SSTI vulnerability found in {file_path}","green"))
        else:
            print(colored(f"[-] No input handling found in {file_path}","green"))


