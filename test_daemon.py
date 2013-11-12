#! /usr/bin/env python3

''' Test program daemon

Description:
The program should make daemon out of test.py.

Requirements:
It assumes there is python-daemon installed.
(https://pypi.python.org/pypi/python-daemon/)

See details of instalation and settings in install.txt
'''

import daemon

from test import main

with daemon.DaemonContext():
    main()
