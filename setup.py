# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import os

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit',
        'init_script': os.path.abspath('prelaunch.py'),
        'include_files': [("/opt/local/Library/Frameworks/R.framework/Resources", "R")],
    },
    'bdist_mac': {
    },
    'bdist_dmg': {
        'volume_label': 'testApp',
        #'applications-shortcut': True,
    }
}

print "Platform: %s" % sys.platform

executables = [
    Executable(
        script='main.py',
        base=base
    )
]

setup(name='simple_PyQt4',
      version='0.1',
      description='Sample cx_Freeze PyQt4 script',
      options=options,
      executables=executables
      )
