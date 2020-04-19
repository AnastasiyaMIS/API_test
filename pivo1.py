import pytest
import requests
import jsonschema

# проверим,что главная открывается
def test_1_main_page():
    url = 'https://www.openbrewerydb.org/'
    resp = requests.get(url)
    assert resp.status_code == 200

schema = {'type': 'array', 'items': {
                'type': 'object',
                'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'}
                }}
          }

@pytest.mark.parametrize('query', ['dog', 'new_york', 'dsfafs'])
def test_2_complete(query):
    response = requests.get('https://api.openbrewerydb.org/breweries', params={'query': query})
    assert response.status_code == 200
    try:
        check = jsonschema.validate(response.json(), schema)
    except Exception as e:
        check = str(e)
    assert check is None, check

schema1 = {'type': 'array', 'items': {
                'type': 'object',
                'properties': {
                        'id': {'type': 'integer'},
                        'name': {'type': 'string'},
                        'brewery_type': {'type': 'string'},
                        'street': {'type': 'string'},
                        'city': {'type': 'string'},
                        'state': {'type': 'string'},
                        'postal_code': {'type': 'string'},
                        'country': {'type': 'string'},
                        'longitude': {'type': ["string", "null"]},
                        'latitude': {'type': ["string", "null"]},
                        'phone': {'type': 'string'},
                        'website_url': {'type': 'string'},
                        'updated_at': {'type': 'string'},
                        'tag_list': {'type': 'array'}
                }}
          }


@pytest.mark.parametrize('city', ['san_diego', 'not_a_city', 'pasadena'])
def test_3_get_br_by_city(city):
    response = requests.get('https://api.openbrewerydb.org/breweries', params={'by_city': city})
    assert response.status_code == 200
    try:
        check = jsonschema.validate(response.json(), schema1)
    except Exception as e:
        check = str(e)
    assert check is None, check


@pytest.mark.parametrize('state', ['north_carolina', 'new_york', 'not_a_state'])
def test_4_get_br_by_state(state):
    response = requests.get('https://api.openbrewerydb.org/breweries', params={'by_city': state})
    assert response.status_code == 200
    try:
        check = jsonschema.validate(response.json(), schema1)
    except Exception as e:
        check = str(e)
    assert check is None, check


@pytest.mark.parametrize('query', ['dog', 'new_york', 'dsfafs'])
def test_5_get_br_by_query(query):
    response = requests.get('https://api.openbrewerydb.org/breweries', params={'query': query})
    assert response.status_code == 200
    try:
        check = jsonschema.validate(response.json(), schema1)
    except Exception as e:
        check = str(e)
    assert check is None, check