import os
import re


rce_functions = ['Process\.Start\(', 'Reflection\.', 'unsafe', 'Serialization\.']
input_functions = ['Console\.ReadLine\(', 'System\.Console\.ReadLine\(']
file_extensions = ['.cs', '.cshtml', '.vb', '.aspx', '.ascx', '.asmx']
inputs = []
def search_files(path):
    for dirpath, dirs, files in os.walk(path):
        for file_name in files:

            if any(file_name.endswith(ext) for ext in file_extensions):

                file_path = os.path.join(dirpath, file_name)

                with open(file_path, 'r') as f:
                    file_content = f.readlines()

                line_number = 1

                for line in file_content:

                    for rce_func in rce_functions:
                        if re.search(rce_func, line):
                            print(f"RCE zafiyeti tespit edildi: {rce_func} - {file_path} - Satır {line_number}")

                            for input_str in inputs:
                                if input_str in line:
                                    print(f"Kullanıcı girdisi RCE fonksiyonuyla birlikte kullanıldı: {input_str} - {rce_func} - {file_path} - Satır {line_number}")

                    for input_func in input_functions:
                        if re.search(input_func, line):

                            inputs.append(input_func)
                            print(f"Input fonksiyonu tespit edildi: {input_func} - {file_path} - Satır {line_number}")

                    line_number += 1


search_files('/path/to/directory')