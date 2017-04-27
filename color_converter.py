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

#write background info
colorprofile = open("walprofile.colorscheme", 'w')
colorprofile.write("[Background]\n")
colorprofile.write("Color=" + colors[0][0] + "," + colors[0][1] + "," + colors[0][2])
colorprofile.write("\n\n")

#background intense is same
colorprofile.write("[BackgroundIntense]\n")
colorprofile.write("Color=" + colors[0][0] + "," + colors[0][1] + "," + colors[0][2])
colorprofile.write("\n\n")

#loop for the colors
for i in range(0, 8, 1):
 
    colorprofile.write("[Color" + str(i) + "]\n")
    if i == 2:
        print(str(i+1) + ":")
        print(colors[4])
        colorprofile.write("Color=" + colors[4][0] + "," + colors[4][1] + "," +
            colors[4][2])
    elif i == 3:
        print(str(i+1) + ":")
        print(colors[3])
        colorprofile.write("Color=" + colors[3][0] + "," + colors[3][1] + "," +
            colors[3][2])
    else:
        colorprofile.write("Color=" + colors[i+1][0] + "," + colors[i+1][1] + "," +
            colors[i+1][2])
    colorprofile.write("\n\n")

    colorprofile.write("[Color" + str(i) + "Intense]\n")

    if i == 2:
        colorprofile.write("Color=" + colors[4][0] + "," + colors[4][1] + "," +
            colors[4][2])
    elif i == 3:
        colorprofile.write("Color=" + colors[3][0] + "," + colors[3][1] + "," +
            colors[3][2])
    else:
        colorprofile.write("Color=" + colors[i+1][0] + "," + colors[i+1][1] + "," +
            colors[i+1][2])
    
    colorprofile.write("\n\n")


colorprofile.write("[Foreground]\n")
colorprofile.write("Color=" + colors[15][0] + "," + colors[15][1] + "," +
    colors[15][2])
colorprofile.write("\n\n")

colorprofile.write("[ForegroundIntense]\n")
colorprofile.write("Bold=true\n")
colorprofile.write("Color=" + colors[15][0] + "," + colors[15][1] + "," +
    colors[15][2])
colorprofile.write("\n\n")

colorprofile.write("[General]\n")
colorprofile.write("Description=walprofile\n")
colorprofile.write("Opacity=1\n")

colorprofile.close()

#TODO change this so that it goes to an alternative names
#if file already exists
os.system("sudo cp walprofile.colorscheme /usr/share/konsole")

#TODO later, this will set the actual profile
os.system("konsoleprofile colors=walprofile")
    

