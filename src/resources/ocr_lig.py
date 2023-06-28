from flask_restful import Resource
from flask import request, current_app
from resources.services.file_handler.file_handler_api import FileHandlerApi

class OCR_LIG(Resource):
    def post(self):
        routing_key = current_app.config['ROUTING_KEY']
        queue_name = 'api_controladora_'
        fh = FileHandlerApi()
        
        file_zip = request.files['file']
        file = {'file': file_zip}
        fh.send_file_to_unzip(file, routing_key, queue_name)
        
        
        return {'about':'Hello World!'}