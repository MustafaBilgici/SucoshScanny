import os
import re

def scan_directory_csrf(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(('.html')):
                full_path = os.path.join(root, file)
                scan_file(full_path)

def scan_file(file_path):
    with open(file_path, 'r') as f:
        print(file_path)
        contents = f.read()
        
#ajax fetch queries
        if re.search(r'(form.*(method="post").*(action=".*{{ url_for.*}}.*"))', contents, re.IGNORECASE | re.DOTALL):
            if not re.search(r'(.*(csrf_token).*)', contents, re.IGNORECASE):
                print(f"CSRF vulnerability found in file: {file_path}")
        

        if re.search(r'(form.*(method="post").*(action=".*{% url.*%}.*"))', contents, re.IGNORECASE | re.DOTALL):
            if not re.search(r'(.*(csrf_token).*)', contents, re.IGNORECASE):
                print(f"CSRF vulnerability found in file: {file_path}")

# Example usage