import os
import re
import json
def read_html_files(path):
   
    html_files = []
    for filename in os.listdir(path):
        if filename.endswith(".html"):
            file_path = os.path.join(path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                file_content = file.read()
                html_files.append(file_content)
    return html_files

def check_xss_vulnerability_in_directory(html_files):
    
    xss_vulnerabilities = []
    for file_content in html_files:
        matches = re.findall("<[^\s<>]*[^\s<>]*(?:\s\w+=(?:(?:\"[^\"]*\")|(?:\'[^\']*\')|[^\"\'>\s]*))*[^\s<>]*\s*(?:(?:\/>)|(?:>[\s\S]*?<\/[^\s<>]*\s*>))|[\s\S]*?(?:(?<=\=)[\'\"]\+[^\"\'>]*?(\+|%2[Bb]){2}[^\S]*?\w*\([^\S]*?[\'\"]\)|(?<=\=)[\'\"][^\"\'>]*?javascript:[^\"\'>]*?((?:(?:\%25)|%)[\dA-Fa-f]{2}){2}[\S]*?)([\"\'][^\"\'>]*?)(?:javascript:\S*?)?['\"]", file_content)
        if matches:
            xss_vulnerabilities.append({'matches':matches})
    return json.dumps(xss_vulnerabilities)
