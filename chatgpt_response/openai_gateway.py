import os
import sys
import http.client
import json
import requests
from chatgpt_response.responseParser import jsonParser


CURRDIR = os.path.dirname(__file__)
sys.path.append(CURRDIR)


class Openai_gateway:

    def __init__(self, jsonparser = jsonParser()):
        self.jsonparser = jsonparser

    def completion(self, requestData):
        query = "sample unix commands"
        # requestData = """
        # {
        #         "model": "gpt-3.5-turbo",
        #         "messages": [{"role": "user", "content": """ + query + """}],
        #         "temperature": 0.3
        #         }
        # """

        requestData = json.loads("""
        {
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": "linux command to find files that start with xyz"}],
                "temperature": 0.3
                }
        """)

        api_key = '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'
        endpoint = "https://api.openai.com/v1/chat/completions"

        headers = {"Authorization": f"Bearer {api_key}",
                   "Content-Type": "application/json"}
        response = requests.post(endpoint, json=requestData, headers=headers)
        #print("-----")
        #print(response.text)

        self.jsonparser.set_response(response.text)

        self.jsonparser.parse()
        #print("-----")
        return self.jsonparser.prepare_json_response()
