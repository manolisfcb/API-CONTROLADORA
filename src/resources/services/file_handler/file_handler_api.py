import requests
from flask import current_app
import json
class FileHandlerApi():
    def __init__(self):
        self.url = 'http://127.0.0.1:5001/'
    
    def send_file_to_unzip(self, file, routing_key, queue_name):
        dado = {'routing_key': routing_key, 'queue_name': queue_name}

        r = requests.get(self.url + 'unzip', data=dado, files=file)
        return r.text