# import termcolor

# help(termcolor)

# from termcolor import colored

# text = colored("Hi THERE !",color="cyan")
# print(text)

#ASCII ART Exercise

import pyfiglet
from termcolor import colored

msg = input("What would you like to pring?")
color = input("What color?")

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art,color="green")
print(colored_ascii)