import os
import sys

from chatgpt_response.openai_gateway import Openai_gateway


CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)


class PilotService:
    
    def __init__(self, openai_gateway = Openai_gateway()):
        self.openai_gateway = openai_gateway
        # self.response = response

    def ask(self, query):
        requestData = """
        {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": """ + query + """}],
                "temperature": 0.7
                }
        """
        print("------------")
        response = self.openai_gateway.completion(requestData)

        return response
