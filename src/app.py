from flask import Flask
from flask_restful import Api

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


from resources.ocr_lig import OCR_LIG
api.add_resource(OCR_LIG, '/ocr_lig')


if __name__ == '__main__':
    app.run(debug=True, port=5000)