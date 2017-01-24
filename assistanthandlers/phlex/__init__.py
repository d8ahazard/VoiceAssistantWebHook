from assistanthandlerbase import AssistantHandler

class AssistantHandlerPhlex(AssistantHandler):
	def __init__(self):
		AssistantHandler.__init__(self,"Playmedia")

	def getSpeech(self, parameters, data):
        query = data.get('query')
        if query is None:
            return "No query"

        result = query.get('apiToken')
        if result is None:
            return "No results"

	def getSpeech(self, parameters, data):
		return "Phlex is listening!  And I have your api key" + result
