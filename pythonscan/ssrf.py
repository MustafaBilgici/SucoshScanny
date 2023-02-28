import os
import re
def find_files(path):
    python_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def detect_input_functions(contents):
    input_functions = []
    if re.search(r'request\.method', contents):
        input_functions.append("request.method")
    if re.search(r'request\.POST\.get', contents):
        input_functions.append("request.POST.get")
    if re.search(r'request\.GET\.get', contents):
        input_functions.append("request.GET.get")
    return input_functions

def detect_ssrf_functions(contents):
    ssrf_functions = []
    if re.search(r'httplib\.', contents):
        ssrf_functions.append("httplib")
    if re.search(r'requests\.', contents):
        ssrf_functions.append("requests")
    if re.search(r'urllib\.(request|parse)', contents):
        ssrf_functions.append("urllib.request/urllib.parse")
    return ssrf_functions

def detect_ssrf(path):
    python_files = find_files(path)
    ssrf_files = []
    for python_file in python_files:
        with open(python_file, 'r') as f:
            contents = f.read()
            input_functions = detect_input_functions(contents)
            ssrf_functions = detect_ssrf_functions(contents)
            if len(input_functions) > 0 and len(ssrf_functions) > 0:
                ssrf_files.append({
                    'file': python_file,
                    'input_functions': input_functions,
                    'ssrf_functions': ssrf_functions
                })
    return ssrf_files


