#!/usr/bin/python

import threading
from pysimplesoap.pysimplesoap.server import SoapDispatcher, SOAPHandler
#from BaseHTTPServer import HTTPServer
from http.server import HTTPServer

class ConfigurationServer(threading.Thread):
	""" Clase que implementa la configuracion de un server"""
	def __init__(self):        
        	self.server = None
	        self.dispatcher = None
	        self.config = None
	        self.port = None
	        self.executing = False
	        #super(self).__init__()
	        threading.Thread.__init__(self)
	        #super(StoppableThread,self).__init__()
	        #self._stop = threading.Event()
		
        

	def run(self): 
		#self.dispatcher = SoapDispatcher(
		#                   'my_dispatcher',
		#                   location = "http://localhost:8008/",
		#                   action = 'http://localhost:8008/', # SOAPAction
		#                   namespace = "http://example.com/sample.wsdl", 
		#                   trace = True,
		#                   ns = True)
		#threading.Thread.__init__(self)
		if self.dispatcher is not None:
			self.executing = True
			print ("Init thread")
			self.server = HTTPServer(("",self.port),SOAPHandler)
			self.server.dispatcher = self.dispatcher
			print("Sirviendo")
			self.server.serve_forever()

	def stop(self):
#        	self.server.shutdown()
#	        self.server.server_close()
#		self._stop.set()
#		self.executing = False
		#t = threading.Timer(60.0,pararServidor,["config"],{ arg: self})
		t = threading.Timer(60.0,pararServidor,[self])
		t.start()
	
	def stopped(self):
		return self._stop.isSet()
	
	def getDispatcher(self):
		return self.dispatcher
		
	def setDispatcher(self,dispatcher):
		self.dispatcher = dispatcher
	
	def isExecuting(self):
		return self.executing


def pararServidor(config):
	config.server.shutdown()
	config.server.server_close()
	#config._stop.set()
	config.executing = False
