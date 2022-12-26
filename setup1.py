import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"D:\new_python\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"D:\new_python\tcl\tk8.6"

executables = [cx_Freeze.Executable("text_editory.py", base=base, icon="icon2.ico",shortcutName="Text Editor",shortcutDir="DesktopFolder")]

cx_Freeze.setup(
    name = "Text Editor",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["icon2.ico",'tcl86t.dll','tk86t.dll', 'icons2']}},
    version = "1.0",
    author="Kali",
    description = "Tkinter Application",
    executables = executables
    )
