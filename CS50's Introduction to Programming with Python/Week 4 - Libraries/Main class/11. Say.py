# You can use python packages https://pypi.org/
# This is going to be time taking process, you have to download it unzip it and install

#  Use pip command in terminal to install packages

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])