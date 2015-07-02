
import ConfigurationServer

class ThreadManager:
	""" Clase encargada de gestionar los threads"""
	
	__lista_threads = []	
	__defaultConfig = None
	def __init__(self):
		#self.defaultConfig = None
		self.hola = None
	@staticmethod
	def startAllThreads():
		print ("Iniciando todos los threads")
		ThreadManager.__defaultConfig.start()
		#for i in range(len(__lista_threads)):
		#	t = __lista_threads[i]
		#	t.start()
		for t in ThreadManager.__lista_threads:
			t.start()

	@staticmethod
	def stopAllThreads():
		#ThreadManager.__lista_threads.append(1)
		for t in ThreadManager.__lista_threads:
			t.stop()
		ThreadManager.__defaultConfig.stop()
		print ("Parando todos los threads")

	@staticmethod
	def addThread(configurationServer):
		ThreadManager.__lista_threads.append(configurationServer)
		#configurationServer.start()

	@staticmethod
	def addInitialThread(configurationServer):
		ThreadManager.__lista_threads.append(configurationServer)

	@staticmethod
	def setDefaultThread(config):
		ThreadManager.__defaultConfig = config	
 

