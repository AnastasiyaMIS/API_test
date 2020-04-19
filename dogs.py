import pytest
import requests
import cerberus

#проверим,что главная открывается
def test_1_main_page():
   url = 'https://dog.ceo/dog-api/'
   resp = requests.get(url)
   assert resp.status_code == 200

#список пород
def test_2():
    r = requests.get('https://dog.ceo/api/breeds/list/all',)
    requests.get('https://dog.ceo/api/breeds/list/all')
    resp = requests.get('https://dog.ceo/api/breeds/list/all')
    assert resp.status_code == 200

#породы
def test_3_breed():
    breed_name = 'hound'
    url = 'https://dog.ceo/api/breed/' + breed_name + '/images'
    response = requests.get(url).json()

    for image_url in response['message']:
        assert breed_name in image_url

#с параметризацией
schema1 = {
          'message': {'type': 'list'},
          'status': {'type': 'string'}
}

@pytest.mark.parametrize('count', [1, 3, 50])
def test_4_randlom_multiple(count):
    response = requests.get('https://dog.ceo/api/breeds/image/random/' + str(count))
    v = cerberus.Validator()
    assert v.validate(response.json(), schema1)
    assert len(response.json()['message']) == count

schema2 = {
          'message': {'type': 'string'},
          'status': {'type': 'string'}
}
@pytest.mark.parametrize('breed, sub_breed', [('hound', 'afghan'), ('hound', 'english'), ('hound', 'walker')])
def test_5_random_img(breed, sub_breed):
    response = requests.get('https://dog.ceo/api/breed/' + breed + '/' + sub_breed + '/images/random')
    v = cerberus.Validator()
    assert v.validate(response.json(), schema2)