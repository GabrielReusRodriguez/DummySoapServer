
from pysimplesoap.server import SoapDispatcher
from ThreadManager import ThreadManager
from ConfigurationServer import ConfigurationServer



def defaultDispatcher_logic(operation):
	if operation == "exit":
		ThreadManager.stopAllThreads()
		return "ok"
	else:
		return "unknown"

def adder(a,b):
	return a+b

def defaultDispatcher_init():
	config =  ConfigurationServer()
	config.port = 8008
	config.nombre = "admin"
	config.dispatcher = SoapDispatcher(
		'my_dispatcher',
		location = "http://localhost:8008",
		action = 'http://localhost:8008', #SOAPAction
		namespace = "http://example.com/sample.wsdl", prefix = "ns0",
		trace = True,
		ns = True
	) 

	config.dispatcher.register_function('adminRequest',defaultDispatcher_logic,
		returns = {'msg' : str},

		args={'operation' : str }
	)

#	config.dispatcher.register_function('Adder',adder,
#		returns = {'AddResult' : int},
#		args = {'a':int, 'b':int}
#	)

	return config
