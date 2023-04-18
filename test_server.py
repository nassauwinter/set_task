import logging

import pytest
import requests


@pytest.mark.parametrize('endpoint, id_, expected_status, expected_response', [
    ('people', 1, 200, {
        'name': 'Luke Skywalker',
        'birth_year': '19BBY',
        'eye_color': 'blue',
        'gender': 'male',
        'hair_color': 'blond',
        'height': '172',
        'mass': '77',
        'skin_color': 'fair'
    }),
    ('people', 101, 404, {'error': 'Person with ID 101 not found'}),
    ('planets', 1, 200, {
        'name': 'Tatooine',
        'climate': 'arid',
        'diameter': '10465',
        'gravity': '1 standard',
        'terrain': 'desert',
        'population': '200000'
    }),
    ('planets', 101, 404, {'error': 'Planet with ID 101 not found'}),
    ('starships', 1, 200, {
        'name': 'X-wing',
        'model': 'T-65 X-wing',
        'manufacturer': 'Incom Corporation',
        'starship_class': 'Starfighter',
        'length': '12.5',
        'crew': '1',
        'passengers': '0'
    }),
    ('starships', 101, 404, {'error': 'Starship with ID 101 not found'}),
])
@pytest.mark.usefixtures('http_server')
def test_endpoint(endpoint, id_, expected_status, expected_response):
    logging.info(f'Testing endpoint {endpoint}/{id_}/')
    response = requests.get(f'http://127.0.0.1:3000/{endpoint}/{id_}')

    assert response.status_code == expected_status

    if expected_status < 400:
        assert response.json() == expected_response
        logging.info(f'Response: {response.status_code} {response.json()}')
    else:
        assert expected_response['error'] in response.text
        logging.info(f'Response: {response.status_code} {response.text}')
