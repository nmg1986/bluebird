#!/usr/bin/python

import ConfigParser 

path_list=list()
#exclude_list=list()

parser=ConfigParser.SafeConfigParser()
parser.read("/etc/bluebird.conf")

#try:
#	for section in parser.sections():
#		source=parser.get(section,"source")
#		target=parser.get(section,"target")
#		list[source]=target
#
#except ConfigParser.NoOptionError,error:
#	print error
try:
	target=parser.get("target","target")
	sync_list=parser.get("source","path").split(':')
	exclude_list=parser.get("exclude","path").split(':')
except ConfigParser.NoOptionError,error:
	print error

#for key,path in parser.items("source"):
#	list2.append(path)
