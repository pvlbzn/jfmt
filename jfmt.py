#! /usr/local/bin/python

from __future__ import print_function

import sys, os

COMMAND = "java -jar ./fmt/google-java-format-1.0-all-deps.jar "
# Verbose output.
DEBUG = True


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
                c = COMMAND + "--replace " + fpath
                os.system(c)
                if DEBUG:
                    print("Path: ", dirpath)
                    print("Name: ", fname)
                    print("Done.\n")


def format_file(p):
    '''
    Format the file.
    '''
    c = COMMAND + "--replace " + p
    os.system(c)


def main():
    parse_argv()


if __name__ == '__main__':
    main()
