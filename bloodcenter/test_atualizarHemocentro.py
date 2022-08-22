import requests
import json
import random
import util.Token

url = f"{util.Token.get_url()}/api/bloodcenter"

email = random.random()

token = util.Token.get_token()

payload = {
  "id": 1,
  "active": False,
  "name": f"atualizacao QA{email}",
  "email": f" Email@{email}.com.br",
  "phone": "eu dolore",
  "address": "id",
  "addressNumber": -22234709,
  "addressComplement": "ex id quis eu qui",
  "neighborhood": "id aliquip",
  "city": "enim exercitation",
  "state": "tempor anim",
  "zipCode": "sunt mollit"
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}


def test_atualizar_hemocentro_sucesso():
    payload2 = json.dumps(payload)
    response = requests.request("PUT", url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 200
    assert response.json()['name'] == f'atualizacao QA{email}'


def test_atualizar_hemocentro_ixistente():
    payload['id'] = 99999999
    payload2 = json.dumps(payload)
    response = requests.request("PUT", url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 400
    assert 'Hemocentro não encontrado' in response.json()['warning']

def test_atualizar_hemocentro_erro_token():
    payload2 = json.dumps(payload)
    headers['Authorization'] = 'tokenInvalido'
    response = requests.request("PUT", url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 401
