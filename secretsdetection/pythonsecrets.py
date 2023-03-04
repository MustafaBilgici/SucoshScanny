import os
import re
import json

def secrets_scan_files(directory, keywords_file):
    results = {}
    with open(keywords_file, 'r') as f:
        keywords = [line.strip() for line in f.readlines()]
        keywords2=[]
        for key in keywords:
            key2=key+str("=")
            keywords2.append(key2)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    contents = f.read()

                matches = re.findall("|".join(keywords2), contents)
                if matches:
                    results[file_path] = matches
    
    print(json.dumps(results))
