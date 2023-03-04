# Normal Detection output without Json
# import os
# import re

# def check_xss_vulnerability(python_file_path):
#     with open(python_file_path) as f:
#         python_code = f.read()

#     get_pattern = re.compile(r"get\(.*\)")
#     render_pattern = re.compile(r"render_template\(.*\)")
#     response_pattern = re.compile(r"response\(.*\)")
#     cookie_pattern = re.compile(r"set_cookie\(.*\)")
#     url_pattern = re.compile(r"redirect\(.*\)")
#     input_pattern = re.compile(r"request\.get\(.*\)|request\.post\(.*\)")

#     matches = get_pattern.findall(python_code) + render_pattern.findall(python_code) + response_pattern.findall(python_code) + cookie_pattern.findall(python_code) + url_pattern.findall(python_code) + input_pattern.findall(python_code)

#     for match in matches:
#         if "html" in match or "HTML" in match or "input" in match or "value" in match or "redirect" in match:
#             print("Potential XSS vulnerability detected in " + python_file_path + ": " + match)

#     if not matches:
#         print("No XSS vulnerabilities detected in " + python_file_path)

# def check_xss_vulnerability_in_directory(path):
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             if file.endswith(".py"):
#                 check_xss_vulnerability(os.path.join(root, file))



import os
import re
import json

def check_xss_vulnerability(python_file_path):
    with open(python_file_path) as f:
        python_code = f.read()

    get_pattern = re.compile(r"get\(.*\)")
    render_pattern = re.compile(r"render_template\(.*\)")
    response_pattern = re.compile(r"response\(.*\)")
    cookie_pattern = re.compile(r"set_cookie\(.*\)")
    url_pattern = re.compile(r"redirect\(.*\)")
    input_pattern = re.compile(r"request\.get\(.*\)|request\.post\(.*\)")

    matches = get_pattern.findall(python_code) + render_pattern.findall(python_code) + response_pattern.findall(python_code) + cookie_pattern.findall(python_code) + url_pattern.findall(python_code) + input_pattern.findall(python_code)

    results = []
    for match in matches:
        if "html" in match or "HTML" in match or "input" in match or "value" in match or "redirect" in match:
            result = {
                "vulnerability": "Potential XSS vulnerability detected",
                "file_path": python_file_path,
                "match": match
            }
            results.append(result)

    if not results:
        result = {
            "vulnerability": "No XSS vulnerabilities detected",
            "file_path": python_file_path
        }
        results.append(result)
    
    return results

def check_xss_vulnerability_in_directory(path):
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                result = check_xss_vulnerability(os.path.join(root, file))
                results.extend(result)
    return results


