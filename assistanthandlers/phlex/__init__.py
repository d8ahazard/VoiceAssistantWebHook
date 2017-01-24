from assistanthandlerbase import AssistantHandler

class AssistantHandlerPhlex(AssistantHandler):
	def __init__(self):
		AssistantHandler.__init__(self,"Playmedia")

	def getApiToken(self,parameters, data):
		query = data.get('apiToken')
        if query is None:
            return "No API Key specified"
		
	def getBaseUrl(self,parameters):
		pass


	def getEndpoint(self,parameters):
		pass


	def getEndpointParameters(self,parameters):
		pass

	def getSpeech(self, parameters, data):
		return "Phlex is listening!  And I have your api key" + query
