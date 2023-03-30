#coding=utf-8

import os, sys, platform

os.system('rm -rf Shahid.so Shahid32.so')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf Shahid.so Shahid32.so')

except:

    pass

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('Shahid.so'):

        os.system('curl -L https://github.com/SA-143/executables/blob/main/Shahid.cpython-311.so?raw=true -o Shahid.so') 

        import Shahid

    else:

        import Shahid

elif bit == '32bit':

    if not os.path.isfile('Shahid32.so'):

        os.system('curl -L https://github.com/SA-143/executables/blob/main/Shahid32.cpython-311.so?raw=true -o Shahid32.so') 

        import Shahid32

    else:

        import Shahid32

