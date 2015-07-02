
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from ThreadManager import ThreadManager
from ConfigurationServer import ConfigurationServer

import random


def triatgeDispatcher_logic(ADT_A01):
	#print "Hola!!"

	response = ""
	fileName = ""
	if random.randint(0,9) <= 4:
		fileName = './TriatgeWS/resp_ack.xml'
	else:
		fileName = './TriatgeWS/resp_ack_error.xml'
	f = open(fileName,"r")	
	response = f.read()
	f.close
	return response


def triatgeDispatcher_init():
	config =  ConfigurationServer()
	config.port = 8009
	config.dispatcher = SoapDispatcher(
		'triatgeDispatcher',
		location = "http://localhost:8009",
		action = 'http://localhost:8009', #SOAPAction
#		namespace = "urn:hl7-org:v2xml", prefix = "ns0",
		namespace = "http://xml.apache.org/axis/wsdd/", prefix = "wsdd",
		trace = True,
		ns = True
	) 

	config.dispatcher.register_function('processHL7',triatgeDispatcher_logic,
		returns = {'processHL7Return' : str},
		args = { 'ADT_A01' : str }

#		args={'MSH' : 	{'MSH.1' : str,
#				 'MSH.2' : str,
#				 'MSH.3' : {'HD.1' : str},
#				 'MSH.4' : {'HD.1' : str},
#				 'MSH.5' : {'HD.1' : str},
#				 'MSH.6' : {'HD.1' : str},
#				 'MSH.7' : {'TS.1' : str},
#				 'MSH.9' : {'MSG.1' : str, 'MSG.2' : str},
#				 'MSH.10' : str,
#				 'MSH.11' : {'PT.1' : str},
#				 'MSH.12' : {'VID.1' : str},
#				 'MSH.13' : str,
#				 'MSH.16' : str,
#				 'MSH.18' : str
#				} ,
#			'PID' : {
#				'PID.3' : { 'CX.1' : str},
#				['PID.5' : { 'XPN.1' : str}]
#			},
#			'ORU_R30.VISIT': str,
#			'ORC' :	str,
#			'OBR' : str,
#			'ORU_R30.OBSERVATION' : str,
#		}		
	)

#	config.dispatcher.register_function('Adder',adder,
#		returns = {'AddResult' : int},
#		args = {'a':int, 'b':int}
#	)

	return config
