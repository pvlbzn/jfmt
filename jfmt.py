import sys, os

command = "java -jar ./fmt/google-java-format-1.0-all-deps.jar "

def parse_argv():
    if len(sys.argv) == 3:
        # First arg is always the script name,
        # second arg is argument to the java formatter,
        # third is a path to target file.
        pass
    if len(sys.argv) == 2:
        # Auto mode: second arg is a path to target.
        # It will replace current code with a new one.
        p = os.path.abspath(sys.argv[1])
        c = command + "--replace " + p
        os.system(c)


def main():
    parse_argv()


if __name__ == '__main__':
    main()
