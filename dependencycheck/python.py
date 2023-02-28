import subprocess
import sys
def check_dependencies(path):
    requirements_path = path + '/requirements.txt'

    try:
        result = subprocess.run(
            ['pip', 'check', '-r', requirements_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )

        print("Dependencies Version Up to Date.")
        sys.exit(0)

    except subprocess.CalledProcessError as e:
        print("Dependencies Versions Outdated.")
        print(e.stderr.decode())
        sys.exit(1)

if __name__ == '__main__':
    path = "/Users/bilgici/Desktop/vulnerablelab/"
    check_dependencies(path)