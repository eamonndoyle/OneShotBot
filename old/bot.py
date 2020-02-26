# -*- coding: utf-8 -*-
"""
Edited on Thu Oct  31 15:59:26 2019
@author: n0273661 eamonn.doyle@libertymutual.com

A rules based ChatBot for getting quick answers to simple DR questions.
All questions are saved in BotQuestions.csv and can be used to improve answer quality over time.
All answers are shortend links to either one of the 2 Resiliency SharePoint sites or PowerBI and will launch the 
web browser in the users default settings.
"""

import os, webbrowser #import the modules we need
os.chdir('C:\\Users\\n0273661\\Desktop\\python\\SimpleGUI')
#we need to use this path, if someone else runs this script they need to change the value to something they have control over.

#https://libertymutual.sharepoint.com/:x:/r/teams/BCDR/Shared%20Documents/Support-Documents/DRaaS/Python/ChatBot/BotQuestions.csv?d=w2a95bf0b65c74ea8ae492a8fbd8491a3&csf=1
#http://jump.lmig.com/64kmkr #shortened version of above link

#open the file
#f = open('BotAnswers.csv','r') #not needed atm
g = open('BotQuestions.csv','a')

print('Hi, What can I help you with today?')
Q=(str.upper(input())).replace("?","") #Q is our question from user, make upper case and remove the trailing ?
print((Q),file=g) #append to file to improve answer quality over time

#Setup variables for the shortened  links:
TIER = "http://jump.lmig.com/b7kcgc"
SRM = "http://jump.lmig.com/t2fgfb"
FIREWALL = FIREWALLS = "http://jump.lmig.com/3embxt"
CYBERARK = "http://jump.lmig.com/rr34ra"
BLADELOGIC = "http://jump.lmig.com/9ygx27"
VPN = "http://jump.lmig.com/c5exr4"
VDE = "http://jump.lmig.com/x8rbfw"
EVENT = TRACKER = "http://jump.lmig.com/pdcmze"
TROUX = "http://jump.lmig.com/tsgscp"
EXERCISE = EXERCISES = "http://jump.lmig.com/md2nf8"
WIKI = "http://jump.lmig.com/3y8zt2"
RESILIENCY = PORTAL = "http://jump.lmig.com/y4spcn"
IRR = "http://jump.lmig.com/d9f23x"
STATUS = "http://jump.lmig.com/4b6wxn"

#webbrowser.open_new(WIKI) #for testing only, to prove you can open a webpage.

#break the question string into words
words = Q.split()
#print(words) #for testing only

for word in words:
    if word == "TIER":
        webbrowser.open_new(TIER)
        print(TIER)
        break #break from loop if we get correct keyword, stops multiple hits
    elif word == "SRM":
        webbrowser.open_new(SRM)
        print(SRM)
        break
    elif word == "FIREWALL":
        webbrowser.open_new(FIREWALL)
        print(FIREWALL)
        break
    elif word == "FIREWALLS":
        webbrowser.open_new(FIREWALLS)
        print(FIREWALLS)
        break
    elif word == "CYBERARK":
        webbrowser.open_new(CYBERARK)
        print(CYBERARK)
        break
    elif word == "BLADELOGIC":
        webbrowser.open_new(BLADELOGIC)
        print(BLADELOGIC)
        break
    elif word == "VPN":
        webbrowser.open_new(VPN)
        print(VPN)
        break
    elif word == "VDE":
        webbrowser.open_new(VDE)
        print(VDE)
        break
    elif word == "TRACKER":
        webbrowser.open_new(TRACKER)
        print(TRACKER)
        break
    elif word == "TROUX":
        webbrowser.open_new(TROUX)
        print(TROUX)
        break
    elif word == "EXERCISE":
        webbrowser.open_new(EXERCISE)
        print(EXERCISE)
        break
    elif word == "EXERCISES":
        webbrowser.open_new(EXERCISES)
        print(EXERCISES)
        break
    elif word == "WIKI":
        webbrowser.open_new(WIKI)
        print(WIKI)
        break
    elif word == "PORTAL":
        webbrowser.open_new(PORTAL)
        print(PORTAL)
        break
    elif word == "RESILIENCY":
        webbrowser.open_new(RESILIENCY)
        print(RESILIENCY)
        break
    elif word == "IRR":
        webbrowser.open_new(IRR)
        print(IRR)
        break
    elif word == "STATUS":
        webbrowser.open_new(STATUS)
        print(STATUS)
        break
else:
    print()
    print("That was fun, lets try another")
    
#close the file
#f.close() #unused atm
g.close()


    