#-*-coding: UTF-8 -*-
import requests

logo = """
\033[37;1m
╔═╗┌─┐╔═╗╔╗╔┌┐┌┌─┐╦═╗
╚═╗│  ╠═╣║║║│││├┤ ╠╦╝ \033[32;1mf0R shElL oR UPloaD3r
╚═╝└─┘╩ ╩╝╚╝┘└┘└─┘╩╚═
      \033[33;1mT0oLs pOwerED SecurityXploitcrew

\033[37;1mstatus [\033[32;1m200\033[37;1m] = FoUnD
\033[37;1mstatus [\033[31;1m404\033[37;1m] = NoT f0und
\033[37;1mstatus [\033[33;1m403\033[37;1m] = ForBideN
"""
print logo
target = raw_input("list: \033[37;1m")
target = open(target,"r")

for a in target.readlines():
    pw = a.strip()
    c = requests.get(pw+"/upload.php")
    print "url: ",c.url,"\033[37;1m[\033[32;1mstatus\033[37;1m]",c.status_code

