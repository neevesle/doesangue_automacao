import requests
import json
import random
import util.Token

token = util.Token.get_token()

headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}

url_endPoint = "http://20.127.23.8/api/bloodcenter"

email = random.random()

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


def massa_cadastrar_hemocentro():
    payload2 = json.dumps(payload)
    response = requests.post(url=url_endPoint, headers=headers, data=payload2)
    return response.json()['id']


def test_deletar_hemocentro_sucesso():
    id_deletar = massa_cadastrar_hemocentro()
    url_endpoint = str(f'http://20.127.23.8/api/bloodcenter/{id_deletar}')
    response = requests.delete(url=url_endpoint, headers=headers)
    print(f'\n [id deletado] {id_deletar}')
    print(f'\n [Status code] {response.status_code}')
    assert response.status_code == 200


def test_deletar_hemocentro_nao_encontrado():
    url_endpoint = str(f'http://20.127.23.8/api/bloodcenter/999999999')
    response = requests.delete(url=url_endpoint, headers=headers)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 400
    assert response.json()['warning'] == 'Hemocentro não encontrado'


def test_deletar_hemocentro_erro_token():
    headers['Authorization'] = 'TokenInvalido'
    url_endpoint = str(f'http://20.127.23.8/api/bloodcenter/99')
    response = requests.delete(url=url_endpoint, headers=headers)
    print(f'\n [Status code] {response.status_code}')
    assert response.status_code == 401

