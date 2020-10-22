import time
import os
import sys
from folderWatcher import Watcher
import tkinter as tk
from tkinter import filedialog

dirname = os.path.dirname(__file__)
pathFile = os.path.join(dirname, 'IL2_PATH')
IL2Path = ''
f = None

# Check if IL2 path file exists. If not, open dialog and ask user for input
if not os.path.isfile(pathFile):
	root = tk.Tk()
	root.withdraw()
	IL2Path = filedialog.askdirectory()
# Else read IL2 path file
else: 
	try:
		f = open(pathFile, "r")
		IL2Path = f.read()
	except:
		print("Something went wrong when reading IL2 path file! Try deleting it.")
	finally:
		f.close()

# Overwrites IL2 path file
try:
	f = open(pathFile, 'w')
	f.write(IL2Path)
except:
	print("Could not write to IL2 path file!")
finally:
	f.close()

# Set up folder watching
recFolder = IL2Path + '\data\Tracks'
if not os.path.isdir(recFolder):
	print("Could not find tracks folder. Try passing IL2 folder as argument again!")
	sys.exit(0)

w = Watcher()
w.PATH = recFolder
w.run()
