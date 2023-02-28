import os
import re

def is_valid_filename(filename):
    # Geçerli dosya isimleri için bir düzenli ifade
    pattern = r'^[\w\d\-]+\.py$'
    return re.match(pattern, filename)
#mitigation functions
def find_input_taint_and_lfi(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        input_taint = False
        lfi_potential = False
        if re.search(r'request\.method', file_contents) or re.search(r'request\.POST\.get', file_contents) or re.search(r'request\.GET\.get', file_contents):
            input_taint = True
        if re.search(r'\.open\(', file_contents) or re.search(r'\.read\(', file_contents):
            lfi_potential = True
        if input_taint and lfi_potential:
            print(f"[LFI POTENTIAL]: {file_path}")
        elif input_taint:
            print(f"[POTENTIAL INPUT TAINT]: {file_path}")
        else:
            print(f"[OK]: {file_path}")

def scan_directory_lfi(path):
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.py') and is_valid_filename(filename):
                file_path = os.path.join(dirpath, filename)
                find_input_taint_and_lfi(file_path)


