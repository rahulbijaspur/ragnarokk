import pickle
from flask import Flask, request
from flask_restful import Api, Resource
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
api = Api(app)
run_with_ngrok(app) 

with open('model_pickle','rb') as file:
  model = pickle.load(file)
print("Loaded model from disk")


class Predict(Resource):
    def get(self):
        return "app running"
    def post(self):
        input = request.data
        input  = input.decode("utf-8")
        input=[input]
        return model.predict(input)[0]

api.add_resource(Predict, "/")

if __name__ == '__main__':
    app.run()