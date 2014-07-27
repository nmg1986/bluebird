#!/usr/bin/python

from ConfigParser import SafeConfigParser 

parser=SafeConfigParser()
parser.read("/usr/bluebird/conf/rsync.conf")

option=parser.get("rsync","option")
binary=parser.get("rsync","binary")


parser.read("/etc/bluebird.conf")
user=parser.get("user","user")
port=parser.get("port","port")

#print option 
#print binary
#print user
#print port
