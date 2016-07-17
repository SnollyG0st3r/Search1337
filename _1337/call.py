#------------------Bombermans Team---------------------------------#
# Author  : B3mB4m
# Concat  : b3mb4m@protonmail.com
# Project : https://github.com/b3mb4m/Search1337
# LICENSE : https://github.com/b3mb4m/Search1337/blob/master/LICENSE
#------------------------------------------------------------------#


from day1337 import *
from helper import *


def main():
    HelpMan()
    parser = optparse.OptionParser()
    parser.add_option('-e', '--exploit', action="store")

    # To save all exploits
    parser.add_option('-a', '--all', action="store_true")

    # Output folder, create folder if its not exists.
    parser.add_option('-o', '--output', action="store")
    parser.add_option('-d', '--download', action="store_true")

    options, args = parser.parse_args()

    if not options.exploit:
        HelpMan().usage()
    else:
        Engine(exploit=options.exploit, download=options.download, output=options.output, all=options.all)
