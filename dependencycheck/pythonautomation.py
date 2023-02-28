import subprocess

def run_tool(tool_name, arguments):
    process = subprocess.Popen([tool_name, *arguments], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    return output, error

tool_name = "bandit"
directory = "/Users/bilgici/Desktop/vulnerablelab"
arguments = ["-r", directory]

output, error = run_tool(tool_name, arguments)
output = output.decode("utf-8")

output_lines = output.split("\n")
for line in output_lines:
    if "VULNERABILITY FOUND" in line:
        print("\033[91m" + "VULNERABILITY FOUND" + "\033[0m")
        print("File:", line.split(" ")[0])
    elif directory in line:
        print("\033[92m" + "No vulnerabilities found" + "\033[0m")
        print("File:", line)
