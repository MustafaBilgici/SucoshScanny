import os
import re

def check_directory_for_xss_vulnerabilities(directory):
    # Define regular expressions to search for XSS patterns
    input_pattern = re.compile(r"req\.query\..*|req\.params\..*|req\.body\..*")
    render_pattern = re.compile(r"res\.render\(.*\)")
    send_pattern = re.compile(r"res\.send\(.*\)")
    redirect_pattern = re.compile(r"res\.redirect\(.*\)")

    # Loop through all files in the given directory and its subdirectories
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # Only check Node.js files
            if file.endswith(".js"):
                # Open the file and read its contents
                filepath = os.path.join(subdir, file)
                with open(filepath) as f:
                    nodejs_code = f.read()

                # Find all instances of vulnerable code
                matches = input_pattern.findall(nodejs_code) + render_pattern.findall(nodejs_code) + send_pattern.findall(nodejs_code) + redirect_pattern.findall(nodejs_code)

                # If there are matches, check for potential XSS vulnerabilities
                for match in matches:
                    # Look for instances where user input is being used without being sanitized or escaped
                    if "script" in match or "Script" in match or "input" in match or "value" in match or "redirect" in match:
                        print("Potential XSS vulnerability detected in file " + filepath + ": " + match)

                # If no vulnerabilities were found, print a message indicating that the code is safe
                if not matches:
                    print("No XSS vulnerabilities detected in file " + filepath + ".")
