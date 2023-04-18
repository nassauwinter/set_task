import json
import logging
from datetime import datetime

from flask import Flask, request, abort


app = Flask(__name__)


@app.route('/people/<int:person_id>/', methods=['GET'])
def get_person(person_id):
    if person_id > 100:
        response = {'error': f'Person with ID {person_id} not found'}
        app.logger.info(f'Requested URL: {request.url}, Response Code: 404')
        abort(404, json.dumps(response))
    else:
        response = {
            'name': 'Luke Skywalker',
            'birth_year': '19BBY',
            'eye_color': 'blue',
            'gender': 'male',
            'hair_color': 'blond',
            'height': '172',
            'mass': '77',
            'skin_color': 'fair'
        }
        app.logger.info(f'Requested URL: {request.url}, Response Code: 200')
        return json.dumps(response)


@app.route('/planets/<int:planet_id>/', methods=['GET'])
def get_planet(planet_id):
    if planet_id > 100:
        response = {'error': f'Planet with ID {planet_id} not found'}
        app.logger.info(f'Requested URL: {request.url}, Response Code: 404')
        abort(404, json.dumps(response))
    else:
        response = {
            'name': 'Tatooine',
            'climate': 'arid',
            'diameter': '10465',
            'gravity': '1 standard',
            'terrain': 'desert',
            'population': '200000'
        }
        app.logger.info(f'Requested URL: {request.url}, Response Code: 200')
        return json.dumps(response)


@app.route('/starships/<int:starship_id>/', methods=['GET'])
def get_starship(starship_id):
    if starship_id > 100:
        response = {'error': f'Starship with ID {starship_id} not found'}
        app.logger.info(f'Requested URL: {request.url}, Response Code: 404')
        abort(404, json.dumps(response))
    else:
        response = {
            'name': 'X-wing',
            'model': 'T-65 X-wing',
            'manufacturer': 'Incom Corporation',
            'starship_class': 'Starfighter',
            'length': '12.5',
            'crew': '1',
            'passengers': '0'
        }
        app.logger.info(f'Requested URL: {request.url}, Response Code: 200')
        return json.dumps(response)


@app.after_request
def log_response(response):
    app.logger.info(f'Response Code: {response.status_code}')
    return response


if __name__ == '__main__':
    log_file = f'request_logs_{datetime.now().strftime("%Y%m%d%H%M%S")}.log'
    app.logger.addHandler(logging.FileHandler(log_file))
    app.logger.setLevel(logging.INFO)
    app.run(host='127.0.0.1', port=3000)
