import os
import re
import json
from termcolor import colored

def find_files_to_check(path):
    java_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".java"):
                java_files.append(os.path.join(dirpath, filename))
    return java_files

def check_for_ssti(file_path):
    result = {"file_path": file_path, "vulnerabilities": []}
    with open(file_path, "r") as file:
        file_contents = file.read()
        if re.search(r"\$\{.*\}", file_contents) or re.search(r"\$\!.*\!", file_contents):
            lines = file_contents.split('\n')
            for i, line in enumerate(lines):
                if re.search(r"\$\{.*\}", line) or re.search(r"\$\!.*\!", line):
                    vulnerability = {"line_number": i+1, "line_content": line}
                    result["vulnerabilities"].append(vulnerability)
        else:
            vulnerability = {"line_number": None, "line_content": None}
            result["vulnerabilities"].append(vulnerability)

    return result

def main_ssti(path):
    results = []
    files_to_check = find_files_to_check(path)
    for file in files_to_check:
        result = check_for_ssti(file)
        results.append(result)
    output=json.dumps(results, indent=4)
    print(json.dumps(results, indent=4))
    return output
main_ssti(".")
