############################################################################################
#
# The MIT License (MIT)
# 
# GeniSys TASS Helpers
# Copyright (C) 2018 Adam Milton-Barker (AdamMiltonBarker.com)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Title:         GeniSys TASS Helpers
# Description:   Helper functions for GeniSys TASS devices and applications.
# Configuration: required/confs.json
# Last Modified: 2018-10-02
#
############################################################################################

import time, json

from datetime import datetime

class Helpers():

    def __init__(self):

		###############################################################
		#
		# Nothing to do
		#
		###############################################################
        pass

    def loadConfigs(self):

		###############################################################
		#
		# Loads the core JSON configuration from required/confs.json 
		#
		###############################################################

        with open("required/confs.json") as configs:
            configs = json.loads(configs.read())
        return configs

    def timerStart(self):

		###############################################################
		#
		# Starts the timer
		#
		###############################################################

        return str(datetime.now()), time.time()

    def timerEnd(self, start):

		###############################################################
		#
		# Ends the timer
		#
		###############################################################

        return time.time(), (time.time() - start), str(datetime.now())

    def setLogFile(self, path):

		###############################################################
		#
		# Sets a log file path
		#
		###############################################################
        
        return path + datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S') + ".txt"
        
    def logMessage(self, logfile, process, messageType, message, hide = False):

		###############################################################
		#
		# Logs a message to a log file
		#
		###############################################################

        logString = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + "|" + process + "|" + messageType + ": " + message
        with open(logfile,"a") as logLine:
            logLine.write(logString+'\r\n')
        if hide == False:
            print(logString)