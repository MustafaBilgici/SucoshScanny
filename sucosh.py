from pythonscan.csrf import *
from pythonscan.lfi import *
from pythonscan.rce import *
from pythonscan.sqli import *
from pythonscan.ssrf import *
from pythonscan.ssti import *
from pythonscan.xss import *
from nodejscan.lfi import *
from nodejscan.rce import *
from nodejscan.sqli import *
from nodejscan.ssrf import *
from nodejscan.ssti import *
from nodejscan.xss import *
from secretsdetection.pythonsecrets import *
import pyfiglet
from termcolor import colored
from pythonscan.scanpath import scanpath
import optparse
from php.phplfi import *
from php.phprce import *
from php.phpssti import *


keywords_file="/Users/bilgici/Desktop/SucoshScan/secretsdetection/secrets.txt"
banner = pyfiglet.figlet_format("SucoshScan", font="slant")
colored_banner = colored(banner, color="green")
author = "MustafaBilgici&AnduriCaser"

print(colored_banner)
print(f"\n\tBy {author}")
print(f"\n\t")


def getuserinput():

    parse_object = optparse.OptionParser()
    parse_object.add_option("-p", "--path",dest="path",help="Enter Source Code Path")
    options = parse_object.parse_args()[0]

    if not options.path:
        print("Enter Source Code Path")


    return options
number = 0

user_data = getuserinput()
path = user_data.path

print(scan_directory_csrf(path))

scan_directory_lfi(path)
scan_directory_rce(path)
print(scan_directory_for_python_files(path))

php_scan_directory_rce(path)
php_scan_directory_lfi(path)
find_files_to_check(path)
result = detect_ssrf(path)
print(result)

# for file_path in find_files_to_check(path):
#     check_for_ssti(file_path)

main_ssti(path)

results = check_xss_vulnerability_in_directory(path)
print(json.dumps(results, indent=4))


# scan_directory_for_rce(path)
# scan_node_files_lfi(path)
# scan_node_js_files(path)

# scan_directory_ssrf(path)
# nodejs_ssti_scan(path)
secrets_scan_files(path,keywords_file)