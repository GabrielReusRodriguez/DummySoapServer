#!/usr/bin/python

import Constants

from ThreadManager import ThreadManager
import DefaultDispatcher
from TriatgeWS import TriatgeWS
import logging
import sys


# LOG_FILENAME = '/var/mail/pysimplesoap.server'
# LOG_FILENAME = 'C:/Users/greusr/Desktop/borrame.txt'



if len(sys.argv) > 1:
    Constants.HOME_DIR = sys.argv[1]

LOG_FILENAME = Constants.HOME_DIR + '/log/log.log'

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)


print ("Init")

defaultConfig = DefaultDispatcher.defaultDispatcher_init()

threadManager = ThreadManager()
ThreadManager.setDefaultThread(defaultConfig)

#Add your WS here

triatgeConfig = TriatgeWS.triatgeDispatcher_init()
ThreadManager.addThread(triatgeConfig)

#Init all Threads
ThreadManager.startAllThreads()


print ("Finish")



