import requests
import json
import random
import util.Token

url = f"{util.Token.get_url()}/api/users"

email = random.random()

token = util.Token.get_token()

payload = {
  "id": 1,
  "active": False,
  "name": "ea",
  "phone": "cillum aliqua esse",
  "bloodType": "anim",
  "picture": "commodo",
  "address": "eiusmod",
  "addressNumber": 44572213,
  "addressComplement": "non ipsum dolore ",
  "neighborhood": "voluptate proident sit sint",
  "city": "officia do dolore ipsum adipisicing",
  "state": "ut veniam",
  "zipCode": "occaecat cupidatat dolore ea ex"
}

headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}


def test_atualizar_usuario_sucesso():
    payload2 = json.dumps(payload)
    response = requests.request("PUT", url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 200
    assert response.json()['email'] == 'teste@QA.com.br'


def test_atualizar_usuario_ixistente():
    payload['id'] = 99999999
    payload2 = json.dumps(payload)
    response = requests.request("PUT", url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 400
    assert 'Usuário não encontrado' in response.json()['warning']

def test_atualizar_usuario_erro_token():
    payload2 = json.dumps(payload)
    headers['Authorization'] = 'tokenInvalido'
    response = requests.request("PUT", url, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 401
