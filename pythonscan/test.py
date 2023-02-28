import pyfiglet
from termcolor import colored
banner = pyfiglet.figlet_format("SucoshScan", font="slant")
colored_banner = colored(banner, color="green")
author = "MustafaBilgici&AnduriCaser"

print(colored_banner)
print(f"\n\tBy {author}")