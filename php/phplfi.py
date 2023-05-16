import os
import re
import json


def scan_file(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()

    result = {}

    if re.search(r'<\?php', contents):
        if re.search(r'include\s*\(|include_once\s*\(|require\s*\(|require_once\s*\(|fopen\s*\(|file_get_contents\s*\(|readfile\s*\(', contents):
            result['status'] = 'Vulnerable'
            lfi_vuln_lines = []
            lines = contents.split('\n')
            for i, line in enumerate(lines):
                if re.search(r'include\s*\(|include_once\s*\(|require\s*\(|require_once\s*\(|fopen\s*\(|file_get_contents\s*\(|readfile\s*\(', line):
                    lfi_vuln_lines.append(i+1)
            if lfi_vuln_lines:
                result['vulnerable_lines'] = lfi_vuln_lines
        else:
            result['status'] = 'Input tracking found'
    else:
        pass

    result['file_path'] = file_path

    return result


def scan_directory_lfi(path):
    results = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.php'):
                full_path = os.path.join(root, file)
                result = scan_file(full_path)
                results.append(result)

    output = json.dumps(results, indent=4)
    print(output)