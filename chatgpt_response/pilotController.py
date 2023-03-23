
from flask import Flask
import os
import sys
from chatgpt_response.pilotService import PilotService

# CURRDIR = os.path.dirname(__file__)
# sys.path.append(CURRDIR)


app = Flask(__name__)

@app.route("/ask/<query>")
def ask(query, pilotService = PilotService() ):
        print("----------------------")
        return pilotService.ask(query)
        # return self.service.ask(query)
    
if __name__ == '__main__':
    app.run()




    
