#! /usr/local/bin/python

from __future__ import print_function

import sys, os


# Get script location path in order to find
# a real address of the google-java-format.
def origin_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

# Global variable which represents a command
# to OS, which later will be executes.
COMMAND = "java -jar " + origin_path(
) + "/" + "fmt/google-java-format-1.0-all-deps.jar"

# Verbose output.
DEBUG = False


def parse_argv():
    if len(sys.argv) == 2:
        p = os.path.abspath(sys.argv[1])
        if os.path.isfile(p):
            format_file(p)
        if os.path.isdir(p):
            format_files(p)
    if len(sys.argv) == 1:
        p = os.getcwd()
        format_files(p)


def format_files(p):
    '''
    Format files in `p` directory.
    '''
    for (dirpath, dnames, fnames) in os.walk(p):
        for fname in fnames:
            if fname.endswith('.java'):
                fpath = dirpath + '/' + fname
                c = COMMAND + " --replace " + fpath
                os.system(c)
                if DEBUG:
                    print("Path: ", dirpath)
                    print("Name: ", fname)


def format_file(p):
    '''
    Format the file.
    '''
    c = COMMAND + " --replace " + p
    os.system(c)


def main():
    print("Processing...")
    parse_argv()
    print("Done.")


if __name__ == '__main__':
    main()
