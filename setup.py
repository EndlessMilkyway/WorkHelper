from distutils.command.build import build
import sys
import cx_Freeze

buildOptions = {"packages": ["os", "tkinter", "datetime", "webbrowser"], "include_files": ['app.ico', 'example.png']}

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

exe = [cx_Freeze.Executable("main.py", base=base, icon="app.ico")]

cx_Freeze.setup(
    name= 'GNU Newsletter Work Helper',
    version = '0.1',
    author = "Yeong Ryeol Kim",
    description = "GNU Newsletter Work Helper",
    options = {"build_exe": buildOptions},
    executables = exe
)