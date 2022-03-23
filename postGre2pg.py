#!/usr/bin/env python3
##################################################################
# postGre2pg: Easily migrate your postGre databases to PostgreSQL
# Author: Anthony Nowocien
##################################################################

import argparse

conf = { 
    'version': "0.1"
}

def option_handling():
    """Command line options handling"""

    parser = argparse.ArgumentParser(description='Migrate from your legacy postGre to PostgreSQL')
    parser.add_argument("-p", "--pronounce",
                        help="How to pronounce",
                        action="store_true", default=False)
    parser.add_argument("-V", "--version",
                        help="print the script version and exit",
                        action="store_true", default=False)
    args = parser.parse_args()
    parser.set_defaults(initialize=True)

    if args.pronounce:
        print ("(/ˈpoʊstɡrɛs ˌkjuː ˈɛl/ \nPOHST-gres kyoo el ")
        exit(1)

    if args.version:
        print ("postGre2pg version " + conf["version"])
        exit(1)

def main():

    option_handling()
    print ("It's called PostgreSQL !")

if __name__ == "__main__":
    main()
