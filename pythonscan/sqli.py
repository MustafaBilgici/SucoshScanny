import os
import re
import json

def check_sql_injection_vulnerability(code, filename):
    select_pattern = re.compile(r"SELECT\s.+?\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")
    insert_pattern = re.compile(r"INSERT\sINTO\s.+?\sVALUES\s?\(.+?\)")
    update_pattern = re.compile(r"UPDATE\s.+?\sSET\s.+\s=\s.+\sWHERE\s.+\s=\s.+\s")
    delete_pattern = re.compile(r"DELETE\sFROM\s.+?\sWHERE\s.+\s=\s.+\s")

    matches = (
        select_pattern.findall(code) +
        insert_pattern.findall(code) +
        update_pattern.findall(code) +
        delete_pattern.findall(code)
    )

    vulnerabilities = []
    lines = code.split("\n")
    for i, line in enumerate(lines, start=1):
        for match in matches:
            if "request.get(" in match or "request.post(" in match:
                if match in line:
                    vulnerabilities.append({
                        "line_number": i,
                        "line_content": line.strip(),
                        "severity": "high"
                    })

    if vulnerabilities:
        return {
            "filename": filename,
            "vulnerabilities": vulnerabilities
        }
    else:
        return None


def scan_directory_for_python_files(path):
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), 'r') as f:
                    code = f.read()
                    result = check_sql_injection_vulnerability(code, file)
                    if result:
                        results.append(result)
    output=json.dumps(results, indent=2)
    print(output)
    return output
