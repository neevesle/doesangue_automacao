import requests
import json
import random
import util.Token

url = F"{util.Token.get_url()}/api/bloodcenter"

email = random.random()

token = util.Token.get_token()

payload = {
  "name": "elit ex culpa",
  "email": f" Email@{email}.com.br",
  "phone": "irure aute",
  "address": "sit amet velit",
  "addressNumber": 87427928,
  "addressComplement": "in quis id veniam nostrud",
  "neighborhood": "et nostrud",
  "city": "voluptate ad anim laborum",
  "state": "amet fugiat",
  "zipCode": "sed Duis"
}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}


def test_cadastrar_hemocentro_sucesso():
    payload2 = json.dumps(payload)
    response = requests.post(url=url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 200


def test_cadastrar_hemocentro_email_existente():
    payload['email'] = 'Email@0.4201264632154582.com.br'
    payload2 = json.dumps(payload)
    response = requests.post(url=url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 400
    assert 'Já existe um hemocentro registrado com E-mail' in response.json()['warning']

def test_cadastrar_hemocentro_erro_token():
    payload2 = json.dumps(payload)
    headers['Authorization'] = 'tokenInvalido'
    response = requests.post(url=url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 401
