'''
    This script generate "requirements.txt" file.
    This file help to intall Python pacakges from local files (.whl) using Pypi package manager.
    The content of generated "requirements.txt" file should look like:
        ...
        numpy==1.24.1
        opencv-python==4.7.0.68
        openpyxl==3.0.10
        packaging==22.0
        pandas==1.5.3
        ...
    After "requirements.txt" file is generated, run below command from CMD would install pypi packages:
        pip install --no-index -r requirements.txt --find-links=.\
        
'''
import os
import glob

file_ext = 'whl'


# set working dir to to path of py script file
cwd = os.path.abspath('')
os.chdir(cwd)

# save the list of file names with extension matching 'file_ext'
# this includes also file in all subdirectories
all_filenames = [i for i in glob.glob('**/*.{}'.format(file_ext), recursive=True)]

# If all_filenames is empty then quit program
if len(all_filenames) == 0:
    print("Found no matched file in 'Input' folder")
    print("Program exit now")
    exit()

#

# filename = "aiofiles-22.1.0-py3-none-any.whl"
# prepare to writing wanted result to "requirements.txt" file
result_textfile = open("requirements.txt", "w")

for name in all_filenames:
    parts = name.split("-")
    package_name = parts[0]
    version_number = parts[1]

    package_string = f"{package_name}>={version_number}"
    print(package_string)
    result_textfile.write(package_string + "\n")

result_textfile.close()
print("Generated requirements.txt file succesfully")