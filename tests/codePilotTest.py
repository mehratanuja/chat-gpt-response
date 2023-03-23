import flask_unittest
import json

from chatgpt_response.pilotController import app

class codePilotTest(flask_unittest.ClientTestCase):

    app = app

    def test_when_queried_responds_back_with_command(self, client):
        '''when queried responds back with command'''
        query = "command to find files that start with xyz"
        
        response = client.get("/ask/" + query)
        #print(response.text)

        response = json.loads(response.text)
        #print(response)

        assert response["command"] != None
        assert response["info"] != None
