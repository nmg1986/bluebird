#!/usr/bin/python


import ConfigParser
import sys

try:
	parser=ConfigParser.SafeConfigParser()
	if parser.read("/usr/bluebird/conf/global.conf") != []:
		pass
	else:
		raise IOError('Cannot open configuration file')

	try:
		logfile=parser.get("global","logfile")
		pidfile=parser.get("global","pidfile")
	except  ConfigParser.NoSectionError,error:
		print 'ERROR:',error
	except	ConfigParser.NoOptionError,error:
		print 'ERROR:',error

except IOError,error:
	sys.exit(error)
