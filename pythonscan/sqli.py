import os
import re
from flask import Flask, request
app = Flask(__name__)

def check_sql_injection_vulnerability(code):
    select_pattern = re.compile(r"SELECT\s.+?\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")
    insert_pattern = re.compile(r"INSERT\sINTO\s.+?\sVALUES\s?\(.+?\)")
    update_pattern = re.compile(r"UPDATE\s.+?\sSET\s.+\s=\s.+\sWHERE\s.+\s=\s.+\s")
    delete_pattern = re.compile(r"DELETE\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")

    matches = select_pattern.findall(code) + insert_pattern.findall(code) + update_pattern.findall(code) + delete_pattern.findall(code)

    for match in matches:
        if "request.get(" in match or "request.post(" in match:
            print("Potential SQL injection vulnerability detected: " + match)

    if not matches:
        print("No SQL injection vulnerabilities detected.")


def scan_directory_for_python_files(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), 'r') as f:
                    code = f.read()
                    check_sql_injection_vulnerability(code)
