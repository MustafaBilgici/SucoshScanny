import os
import re

def check_for_ssti(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        if re.search(r"<%=.*%>", file_contents) or re.search(r"<%#.*%>", file_contents) or re.search(r"\{\{.*\}\}", file_contents) or re.search(r"<%[^(=|#)].*%>", file_contents):
            print(f"[+] Possible SSTI vulnerability found in {file_path}")
        else:
            print(f"[-] No SSTI vulnerability found in {file_path}")

def check_input_type(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
        if re.search(r"req\.body", file_contents) or re.search(r"req\.query", file_contents) or re.search(r"req\.params", file_contents):
            return "POST/GET"
        elif re.search(r"readline", file_contents):
            return "STDIN"
        else:
            return "Not found"

def nodejs_ssti_scan(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".ejs"):
                file_path = os.path.join(dirpath, filename)
                input_type = check_input_type(file_path)
                if input_type != "Not found":
                    check_for_ssti(file_path)
                else:
                    print(f"[-] No input method found in {file_path}")

