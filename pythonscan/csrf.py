import os
import re
import json

def scan_directory_csrf(path):
    results = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(('.html')):
                full_path = os.path.join(root, file)
                result = scan_file(full_path)
                if result["vulnerability"]:
                    results.append(result)
    return json.dumps(results, indent=4)

def scan_file(file_path):
    result = {
        "file_path": file_path,
        "vulnerability": False,
        "vulnerable_lines": []
    }
    with open(file_path, 'r') as f:
        contents = f.read()

        if re.search(r'(form.*(method="post").*(action=".*{{ url_for.*}}.*"))', contents, re.IGNORECASE | re.DOTALL):
            if not re.search(r'(.*(csrf_token).*)', contents, re.IGNORECASE):
                result["vulnerability"] = True
                result["vulnerable_lines"].append("Line: " + str(re.search(r'(form.*(method="post").*(action=".*{{ url_for.*}}.*"))', contents, re.IGNORECASE | re.DOTALL).group(0)))

        if re.search(r'(form.*(method="post").*(action=".*{% url.*%}.*"))', contents, re.IGNORECASE | re.DOTALL):
            if not re.search(r'(.*(csrf_token).*)', contents, re.IGNORECASE):
                result["vulnerability"] = True
                result["vulnerable_lines"].append("Line: " + str(re.search(r'(form.*(method="post").*(action=".*{% url.*%}.*"))', contents, re.IGNORECASE | re.DOTALL).group(0)))

    return result
