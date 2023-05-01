import os
import re
import json

def scan_file(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()

    result = {}

    if re.search(r'(strcpy|strcat|sprintf|gets|scanf)\s*\(', contents):
        result['status'] = 'Potential buffer overflow vulnerability found'
        vuln_lines = []
        lines = contents.split('\n')
        for i, line in enumerate(lines):
            if re.search(r'(strcpy|strcat|sprintf|gets|scanf)\s*\(', line):
                vuln_lines.append(i+1)
        if vuln_lines:
            result['vulnerable_lines'] = vuln_lines
    elif re.search(r'system\s*\(', contents):
        result['status'] = 'Potential command injection vulnerability found'
        vuln_lines = []
        lines = contents.split('\n')
        for i, line in enumerate(lines):
            if re.search(r'system\s*\(', line):
                vuln_lines.append(i+1)
        if vuln_lines:
            result['vulnerable_lines'] = vuln_lines
    else:
        result['status'] = 'No known vulnerabilities found'

    result['file_path'] = file_path

    return result

def scan_directory_c(path):
    results = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.c'):
                full_path = os.path.join(root, file)
                result = scan_file(full_path)
                results.append(result)

    output = json.dumps(results, indent=4)
    print(output)
