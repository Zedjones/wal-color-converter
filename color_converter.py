import os
from os.path import expanduser
import subprocess
import re
import random

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
    #this is a clusterfuck atm
    #TODO clean this shit up
    if i == 3:
        temp = colors[3]
        colors[3] = colors[1]
        colors[1] = temp
    elif i == 4:
        temp = colors[4]
        colors[4] = colors[3]
        colors[3] = temp
    elif i == 5:
        temp = colors[5]
        colors[5] = colors[3]
        colors[3] = temp
    elif i == 7:
        temp = colors[7]
        colors[7] = colors[6]
        colors[6] = temp

#more clusterfuckery
temp = colors[3]
colors[3] = colors[2]
colors[2] = temp

temp = colors[4]
colors[4] = colors[1]
colors[1] = temp

temp = colors[6]
colors[6] = colors[2]
colors[2] = temp

colors[2] = colors[1]
colors[1] = colors[0]

#create a new file name pseudo-randomly
newfile = "walprofile" + str(random.random())[2:]
colorprofile = open(newfile + ".colorscheme", 'w')

#write background info w/ colors 0
colorprofile.write("[Background]\n")
colorprofile.write("Color=" + colors[0][0] + "," + colors[0][1] + "," + colors[0][2])
colorprofile.write("\n\n")

#background intense is same
colorprofile.write("[BackgroundIntense]\n")
colorprofile.write("Color=" + colors[0][0] + "," + colors[0][1] + "," + colors[0][2])
colorprofile.write("\n\n")

#loop for the colors
for i in range(0, 8, 1):
    #formatting for Konsole
    colorprofile.write("[Color" + str(i) + "]\n")
    #writing the rgb for this color
    colorprofile.write("Color=" + colors[i+1][0] + "," + colors[i+1][1] + "," +
        colors[i+1][2])
    #formatting for Konsole
    colorprofile.write("\n\n")
    #formatting for Konsole
    colorprofile.write("[Color" + str(i) + "Intense]\n")
    #writing the name for this color (intense)
    colorprofile.write("Color=" + colors[i+1][0] + "," + colors[i+1][1] + "," +
        colors[i+1][2])
    #formatting for Konsole
    colorprofile.write("\n\n")

#do the same for the foreground with color 16
colorprofile.write("[Foreground]\n")
colorprofile.write("Color=" + colors[15][0] + "," + colors[15][1] + "," +
    colors[15][2])
colorprofile.write("\n\n")

#do the same for foreground intense
colorprofile.write("[ForegroundIntense]\n")
colorprofile.write("Bold=true\n")
colorprofile.write("Color=" + colors[15][0] + "," + colors[15][1] + "," +
    colors[15][2])
colorprofile.write("\n\n")

#write general description
#TODO add a way to take in opacity and use it here
colorprofile.write("[General]\n")
colorprofile.write("Description=" + newfile + "\n")
colorprofile.write("Opacity=1\n")

#close the file
colorprofile.close()
#get all files in /usr/share/konsole (where konsole profiles are stored)
allfiles = subprocess.run(['ls', '/usr/share/konsole'], stdout=subprocess.PIPE)
#decode this from stdout to utf-8
allfiles = allfiles.stdout.decode('utf-8')

#if there is already a wal profile in this 
if 'wal' in allfiles:
    #split the string into a list by lines
    lines = allfiles.splitlines()
    #iterate through the list
    for filename in lines:
            #if wal is in the item in the list
            if 'wal' in filename:
                #remove that item from the folder
                os.system("sudo rm /usr/share/konsole/" + filename)

#move the new profile to the proper location
os.system("sudo mv " + newfile + ".colorscheme  /usr/share/konsole")

#set the profile as active
os.system("konsoleprofile colors=" + newfile)
    

