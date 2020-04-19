import pytest
import requests
import jsonschema

def test_posts_status_code_1():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200

schema = {'type': 'array', 'items': {
                'type': 'object',
                'properties': {
                        'userId': {'type': 'integer'},
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'body': {'type': 'string'}
                }}
          }

def test_posts_schema_2():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    try:
        check = jsonschema.validate(response.json(), schema)
    except Exception as e:
        check = str(e)
    assert check is None, check


@pytest.mark.parametrize('id, title', [(1, 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'),
                                       (2, 'qui est esse'), (100, 'at nam consequatur ea labore ea harum')])
def test_3_post(id, title):
    response = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(id))
    assert response.status_code == 200
    assert response.json()['id'] == id
    assert response.json()['title'] == title



@pytest.mark.parametrize('userId', [1, 2, 10])
def test_posts_status_code_4(userId):
    response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': userId})
    for item in response.json():
        assert item['userId'] == userId, item

def test_post_5():
    body = {
        "title": "my_title",
        "body": "Новое тело",
        "userId": 10
    }
    response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body)
    assert response.status_code == 201, response.text
    assert response.json()['id'] == 101
    assert response.json()['title'] == 'my_title', response.text
    assert response.json()['body'] == 'Новое тело', response.text
    assert response.json()['userId'] == 10, response.text