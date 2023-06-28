import requests

class FileHandlerApi():
    def __init__(self):
        self.url = 'http://localhost:5001/'
        
    
    def send_file_to_unzip(self, file, routing_key):
        
        r = requests.get(self.url + 'unzip', files=file, data={'routing_key': routing_key})
        return r.text