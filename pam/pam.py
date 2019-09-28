import os
import sys
from weblogo import *

def leftRightWrite(left,right):
    if os.path.isfile("left.txt"): 
        with open("left.txt","a") as l:
            l.write(left+"\n")
    if not os.path.isfile("left.txt"): 
        with open("left.txt", "w+") as l:
            l.write(left+"\n")
    if os.path.isfile("right.txt"): 
        with open("right.txt","a") as r:
            r.write(right+"\n")
    if not os.path.isfile("right.txt"): 
        with open("right.txt","w+") as r:
            r.write(right+"\n")


def clustalW(fagfilename,spacerfilename):
    with open(fagfilename, "r") as fag:
        fagtext = fag.read()
        fagnum = fagtext.split()[0].replace(">","")
    with open(spacerfilename, "r") as spacer:
        spacertext = spacer.read()
        spacertext = spacertext.replace("\n","")
    temp = open("temp.txt","w+")
    temp.write(fagtext)
    temp.write(">spacer\n")
    temp.write(spacertext)
    temp.close()
    os.system("clustalw2.exe -infile=temp.txt")


def parseClustalW():
    with open("temp.aln","r") as parse:
        clustalWtext = parse.readlines()
    spacersline = []
    fagline = []
    spacers = []
    fags = []
    for i in clustalWtext:
        if "spacer" in i:
            spacersline.append(i)
        if fagnum in i:
            fagline.append(i)
    for i in spacersline:
        temp = i.replace("spacer","")
        temp = temp.replace("\n","")
        temp = temp.replace(" ","")
        spacers.append(temp)
    for i in fagline:
        temp = i.replace(fagnum,"")
        temp = temp.replace("\n","")
        temp = temp.replace(" ","")
        fags.append(temp)
    spacer = ""
    fag = ""
    for i in spacers:
        spacer+=i
    for i in fags:
        fag+=i
    for i in range(len(spacer)):
        if spacer[i] in nucl:
            x0 = i
            while spacer[i] in nucl or spacer[i+1] in nucl:
                xk = i
                i = i+1
            break
    left = fag[x0-10:x0]
    right = fag[xk+1:xk+10]
    leftright = []
    leftright.append(left)
    leftright.append(right)
    return leftright

def createWeblogo(filename):
    fin = open(filename)
    seqs = read_seq_data(fin)
    data = LogoData.from_seqs(seqs)
    options = LogoOptions(fineprint=False,
                                 logo_title="PAM", 
                                 number_fontsize=5, 
                                 text_font=5)                                 
    logoformat = LogoFormat(data,options)
    png = png_print_formatter(data,logoformat)
    fin.close()
    with open(filename.replace(".txt","")+".png","wb") as out :
         out.write(png)
         out.close()

# fag - 1 spacers - 2
fagnum = ""
for i in sys.argv:
    if "--phage=" in i:
        fagfilename = i.replace("--phage=","")
        with open(fagfilename, "r") as fag:
            fagtext = fag.readline()
            fagnum = fagtext.split()[0].replace(">","")
    if "--spacer=" in i:
        spacerfilename = i.replace("--spacer=","")
    if "--mode=" in i:
        mode = i.replace("--mode=","")
nucl = ["A","G","C","T"]
if mode == "search":
    clustalW(fagfilename,spacerfilename)
    leftright = parseClustalW()
    leftRightWrite(leftright[0],leftright[1])
if mode == "weblogo":
    createWeblogo("left.txt")
    createWeblogo("right.txt")
