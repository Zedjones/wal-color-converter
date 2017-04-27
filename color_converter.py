import os
from os.path import expanduser
import subprocess
import re

#get user home path
homepath = expanduser("~")
#get wal file for colors
walfile = open(homepath + '/.cache/wal/colors');

#create new colors dictionary
colors = {}

#iterate for all colors
for i in range(0, 16):
    #get the hex for the color 
    line = walfile.readline()[1:].strip()
    #use color-convert to convert it to RGB
    temp = subprocess.run(['color-converter', line], stdout=subprocess.PIPE)
    #decode it into utf-8
    temp = temp.stdout.decode('utf-8')
    #split into a list and take info afterwards
    rgb = temp.split("rgb")[1]
    #get text in between parentheses and remove newline
    result = re.sub('[()]', '', rgb).strip()
    #remove any leftover spaces
    result = re.sub('[ ]', '', result).strip()
    #split again by comma to get R,G,B
    rgblist = result.split(",")
    #now we have rgb for this color, so we set it in the dict
    colors[i] = rgblist

colorprofile = open("walprofile.colorscheme", 'a')

#TODO later, this will set the actual profile
#os.system("konsoleprofile colors=" + profilename)
    

