import unittest
from unittest.mock import MagicMock

#from chatgpt_response.pilotController import Controller
from chatgpt_response.pilotController import ask

class responseControllerShould(unittest.TestCase):

    service = MagicMock()
    #pilotcontroller = ask()

    def test_controller_should_call_the_service(self):
        query = "command to find files that start with xyz"

        response = ask(query, self.service)

        assert self.service.ask.iscalled
        
