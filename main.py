import sys
import os
rootDir = '/Users/abraraltaflone/code/ml'
for x in os.walk(rootDir,topdown=False):
    print(f' {x}  ')


