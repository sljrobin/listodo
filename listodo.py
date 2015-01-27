#!/usr/bin/python
# -*- coding: utf-8 -*-

import collections
import os
import re
import sys
from colorama import init
from colorama import Fore, Back, Style
init()


##########################################################################################
PATTERN_01 = r'# TODO'


##########################################################################################
def check_args():
    """
    Check the number of arguments
    Check if the source file exists
    """
    # Check there is one argument
    if len(sys.argv) < 2:
        sys.exit(Back.RED + Fore.WHITE + "ERROR: incorrect argument!\nUsage: %s source_code" % sys.argv[0] + Style.RESET_ALL)

    # Check if the argument exists
    if not os.path.exists(sys.argv[1]):
        sys.exit(Back.RED + Fore.WHITE + "ERROR: '%s' does not exist!" % sys.argv[1] + Style.RESET_ALL)


##########################################################################################
def create_list(source_code):
    """
    Create the list of todos
    Search the pattern '# TODO'
    Save the TODO's line and the TODO's description
    Return the dictionary 'todos'
    """
    todos = {}
    pattrn = re.compile(PATTERN_01)
    with open(source_code) as f:
        for todo_numero, file_line in enumerate(f, 1):
            if pattrn.search(file_line):
                matcher = re.match( r'(.*) TODO (.*)', file_line, re.M|re.I)
                if matcher:
                    todo_description = matcher.group(2)
                    todos.update({todo_numero:todo_description})
    return todos


##########################################################################################
def sort_list():
    """
    Sort items from smallest to largest
    """
    todos = create_list(sys.argv[1])
    ordered_todos = collections.OrderedDict(sorted(todos.items()))
    return ordered_todos


##########################################################################################
def print_list():
    """
    Print the dictionary
    """
    print(Fore.RED + "%s" % sys.argv[1] + Style.RESET_ALL)
    todos = sort_list()
    for item in todos:
        print(Fore.YELLOW + "\t%i:\t%s" %(item, todos[item]) + Style.RESET_ALL)


##########################################################################################
def main():
    """
    Check the arguments
    Print the TODOs
    """
    check_args()
    print_list()
    

##########################################################################################
if __name__ == "__main__":
    main()
