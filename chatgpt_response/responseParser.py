import json


class jsonParser:

    def __init__(self):
        self.parsedResponse = None
    
    def set_response(self, response):
        self.response = response

    def parse(self):
        # pass
        self.parsedResponse = json.loads(self.response)

    def get_content(self):
        return self.parsedResponse["choices"][0]["message"]["content"]

    def get_command(self):

        command_enclosed = 0
        command = None
        content = self.get_content()
        for line in content.split("\n"):
            if command_enclosed == 1:
                command = line.strip()
                break
            else:
                if line.startswith("```"):
                    command_enclosed = command_enclosed+1

        return command

    def get_info(self):
        content = self.get_content()
        info = content[content.rindex("`") + 1:].strip()
        return info

    def prepare_json_response(self):
        
        return {
            "command": self.get_command(),
            "content": self.get_content(),
            "info": self.get_info()
        }
