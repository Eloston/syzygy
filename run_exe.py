#!/usr/bin/env python

import subprocess
import sys

def main(argv):
    subprocess.check_call(argv, shell=True)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
