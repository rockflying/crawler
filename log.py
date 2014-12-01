#!/usr/bin/env python
import os
import logging

global LOG_FILE
LOG_FILE   = 'crawler.log'
LOG_CONFIG = 'conf.ini'

class Log:
	__instance = None

	def __init__(self):
		if os.path.isfile(str(LOG_CONFIG)):
			pass
		else:
			logHandle = open(str(LOG_CONFIG),'w')
			logHandle.writelines(str("the log status is enforcing\n"))
			logHandle.close()
