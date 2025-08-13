#!/usr/bin/env python3

import os
import sys

class Tree:
    def __init__(self):
        self.dirCount = 0
        self.fileCount = 0

    def register(self, absolute):
        if os.path.isdir(absolute):
            self.dirCount += 1
        else:
            self.fileCount += 1

    def summary(self):
        return f"{self.dirCount} directories, {self.fileCount} files"

    def walk(self, directory, prefix=""):
        output = ""
        filepaths = sorted(os.listdir(directory))

        for index, filename in enumerate(filepaths):
            if filename.startswith("."):
                continue

            absolute = os.path.join(directory, filename)
            self.register(absolute)

            connector = "└── " if index == len(filepaths) - 1 else "├── "
            output += prefix + connector + filename + "\n"

            if os.path.isdir(absolute):
                sub_prefix = prefix + ("    " if index == len(filepaths) - 1 else "│   ")
                output += self.walk(absolute, sub_prefix)

        return output

directory = "."
if len(sys.argv) > 1:
    directory = sys.argv[1]

def	result():
	tree = Tree()
	result = tree.walk(directory) + tree.summary()
	return result
