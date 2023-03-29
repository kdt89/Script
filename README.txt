A hub contains my Script (mostly in Python) to do some small work on Windows OS

# Script: py_generate_pip_requirements_txt_file.py:
- Automatically install Pypi package from local files (.whl) by one-click
- Logic: Python get list of .whl files and export list files to 'requirements.txt' file.
	 Python then send command "pip install --no-index -r requirements.txt --find-links=.\" to Windows Terminal to setup
         Then Pypi will do the rest of work for installation
