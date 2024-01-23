#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Plant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = True

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Plants(Resource):
    def get(self):
        Plants_data = [
            {
              "id": 1,
                "name": "Aloe",
                "image": "./images/aloe.jpg",
                "price": 11.50
            },
            {
                "id": 2,
                "name": "ZZ Plant",
                "image": "./images/zz-plant.jpg",
                "price": 25.98  
            }
        ]

        return Plants_data
    


class PlantByID(Resource):
    def get(self, id):
        response_dict = Plants.query.filter_by(id=id).first().to_dict()

        response = make_response(
            jsonify(response_dict),
            200
        )
    

class Resource(Resource):
    def post(self):
        allowed_fields = ["name", "image", "price"]
        new_plant_data = {key: value for key, value in request.json.items() if key in allowed_fields}

        # Assuming you have a function to generate a unique ID
        new_plant_data["id"] = self.generate_unique_id()

        self.plants_data.append(new_plant_data)

        return new_plant_data, 201



api.add_resource(Plants, '/plants')
api.add_resource(PlantByID, '/plants/int:id')
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)
