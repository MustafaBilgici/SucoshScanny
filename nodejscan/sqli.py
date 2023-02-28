import re
import os
import fnmatch

def check_sql_injection_vulnerability(node_js_code):
    select_pattern = re.compile(r"SELECT\s.+?\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")
    insert_pattern = re.compile(r"INSERT\sINTO\s.+?\sVALUES\s?\(.+?\)")
    update_pattern = re.compile(r"UPDATE\s.+?\sSET\s.+\s=\s.+\sWHERE\s.+\s=\s.+\s")
    delete_pattern = re.compile(r"DELETE\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")

    matches = select_pattern.findall(node_js_code) + insert_pattern.findall(node_js_code) + update_pattern.findall(node_js_code) + delete_pattern.findall(node_js_code)

    for match in matches:
        if "request.body" in match or "req.body" in match:
            print("Potential SQL injection vulnerability detected: " + match)

    if not matches:
        print("No SQL injection vulnerabilities detected.")

def scan_node_js_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if fnmatch.fnmatch(file, "*.js"):
                with open(os.path.join(root, file), "r") as f:
                    contents = f.read()
                    check_sql_injection_vulnerability(contents)

