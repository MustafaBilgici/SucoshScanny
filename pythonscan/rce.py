# Normal Detection output without Json
# import os
# import re

# def scan_file(file_path):
#     with open(file_path, 'r') as f:
#         contents = f.read()

#     if re.search(r'request\.(POST|GET)\.(get|post)', contents):
#         if re.search(r'eval\(', contents) or re.search(r'exec\(', contents) or re.search(r'pickle.loads\(', contents) or re.search(r'yaml.load\(', contents) or re.search(r'paramiko.exec_command\(', contents) or re.search(r'SSHClient.invoke_shell\(', contents) or re.search(r'shell=True\(', contents):
#             print('Potential RCE vulnerability found in {}'.format(file_path))
#             rce_vuln_lines = []
#             lines = contents.split('\n')
#             for i, line in enumerate(lines):
#                 if re.search(r'eval\(|exec\(|pickle.loads\(|yaml.load\(|paramiko.exec_command\(|SSHClient.invoke_shell\(|shell=True\(', line):
#                     rce_vuln_lines.append(i+1)
#             if rce_vuln_lines:
#                 print('Vulnerable lines:', rce_vuln_lines)
#         else:
#             print('Input tracking found in {}'.format(file_path))
#     else:
#         if re.search(r'eval\(', contents) or re.search(r'exec\(', contents) or re.search(r'pickle.loads\(', contents) or re.search(r'yaml.load\(', contents) or re.search(r'paramiko.exec_command\(', contents) or re.search(r'SSHClient.invoke_shell\(', contents) or re.search(r'shell=True\(', contents):
#             print('Potential RCE vulnerability found in {}'.format(file_path))
#             rce_vuln_lines = []
#             lines = contents.split('\n')
#             for i, line in enumerate(lines):
#                 if re.search(r'eval\(|exec\(|pickle.loads\(|yaml.load\(|paramiko.exec_command\(|SSHClient.invoke_shell\(|shell=True\(', line):
#                     rce_vuln_lines.append(i+1)
#             if rce_vuln_lines:
#                 print('Vulnerable lines:', rce_vuln_lines)
#         else:
#             print('Input tracking found in {}'.format(file_path))

# def scan_directory_rce(path):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith('.py'):
#                 full_path = os.path.join(root, file)
#                 scan_file(full_path)


import os
import re
import json

def scan_file(file_path):
    with open(file_path, 'r') as f:
        contents = f.read()

    result = {}

    if re.search(r'request\.(POST|GET)\.(get|post)', contents):
        if re.search(r'eval\(', contents) or re.search(r'exec\(', contents) or re.search(r'pickle.loads\(', contents) or re.search(r'yaml.load\(', contents) or re.search(r'paramiko.exec_command\(', contents) or re.search(r'SSHClient.invoke_shell\(', contents) or re.search(r'shell=True\(', contents):
            result['status'] = 'Vulnerable'
            rce_vuln_lines = []
            lines = contents.split('\n')
            for i, line in enumerate(lines):
                if re.search(r'eval\(|exec\(|pickle.loads\(|yaml.load\(|paramiko.exec_command\(|SSHClient.invoke_shell\(|shell=True\(', line):
                    rce_vuln_lines.append(i+1)
            if rce_vuln_lines:
                result['vulnerable_lines'] = rce_vuln_lines
        else:
            result['status'] = 'Input tracking found'
    else:
        if re.search(r'eval\(', contents) or re.search(r'exec\(', contents) or re.search(r'pickle.loads\(', contents) or re.search(r'yaml.load\(', contents) or re.search(r'paramiko.exec_command\(', contents) or re.search(r'SSHClient.invoke_shell\(', contents) or re.search(r'shell=True\(', contents):
            result['status'] = 'Potential RCE vulnerability found'
            rce_vuln_lines = []
            lines = contents.split('\n')
            for i, line in enumerate(lines):
                if re.search(r'eval\(|exec\(|pickle.loads\(|yaml.load\(|paramiko.exec_command\(|SSHClient.invoke_shell\(|shell=True\(', line):
                    rce_vuln_lines.append(i+1)
            if rce_vuln_lines:
                result['vulnerable_lines'] = rce_vuln_lines
        else:
            result['status'] = 'Input tracking found'

    result['file_path'] = file_path

    return result

def scan_directory_rce(path):
    results = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                result = scan_file(full_path)
                results.append(result)

    output = json.dumps(results, indent=4)
    print(output)