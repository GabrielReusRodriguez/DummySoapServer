#!/usr/bin/python


from ThreadManager import ThreadManager
#import ThreadManager
from ConfigurationServer import ConfigurationServer
import DefaultDispatcher
import TriatgeWS
import logging



#LOG_FILENAME = '/var/mail/pysimplesoap.server'
LOG_FILENAME = 'C:/Users/greusr/Desktop/borrame.txt'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)


print ("Init")

#defaultConfig = DefaultDispatcher.defaultDispatcher_init()

#threadManager = ThreadManager()
#threadManager.defaultConfig = defaultConfig
#ThreadManager.setDefaultThread(defaultConfig)

#triatgeConfig = TriatgeWS.triatgeDispatcher_init()
#ThreadManager.addThread(triatgeConfig)


#ThreadManager.startAllThreads()


print ("Finish")



