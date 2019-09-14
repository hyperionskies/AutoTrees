import subprocess
from pathlib import Path
import os,sys

# get directory path for this file
basedir = os.path.abspath(os.path.split(sys.argv[0])[0])

# get input for name of .db file including extention
dbfile = input('Please enter the name of your data file, including the .db: ')
x = Path(str(basedir)+'/'+dbfile)

#loop checks file is present, must be in directory with AutoTrees_v2.py
while not x.is_file():
	dbfile = input('File not found in directory. Please enter the name of your data file, including the .db: ')
	x = Path(str(basedir)+'/'+dbfile)

# build r Terminal command and run with subprocess
# command syntax: [RScript] [path to unpack_v2.R] [directory of project] [name of .db file]
# last two are parameters passed to unpack_v2.R and are necessary; must be in correct order
rcmd = 'Rscript ' + basedir + '/unpack_v2.R' + ' ' + str(basedir) + ' ' + dbfile
subprocess.run(rcmd.split())

# build path for .txt file
datafile = basedir+'/matrix_file_nr.txt'

# build Blender Terminal command and run with subprocess
# command syntax: [Blender] -P [Path to animation_v2.py]
blendcmd = '/Applications/Blender/blender.app/Contents/MacOS/blender -P ' + basedir + '/animation_v2.py '
subprocess.run(blendcmd.split())

#build path for output file after HandBrake runs
filename = basedir + '/final.mp4'

# build Blender Command Prompt command and run with subprocess
# command syntax: [HandBrakeCLI] -i [Path to blender output] -o [path to desired output file location and name, does not have to exist]
handbrakecmd = 'HandBrakeCLI -i ' + basedir + '/blender.avi -o ' + filename
subprocess.run(handbrakecmd.split())

# build path to blender output and run os.remove to delete it
# AVIs get large and are unnecessary after HandBrakeCLI runs, this saves user disk space
deletecmd = 'rm ' + basedir + '/blender.avi'
subprocess.run(deletecmd.split())
