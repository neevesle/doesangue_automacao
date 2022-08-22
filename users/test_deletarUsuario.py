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

url = f"{util.Token.get_url()}/api/users/"

email = random.random()

payload = {
  "name": "Teste QA Leticia automatico",
  "email": f"teste{email}@QA.com.br",
  "phone": "dolor amet id",
  "bloodType": "nostrud",
  "picture": "ea commodo",
  "provider": "elit laborum commodo",
  "providerId": "consequat Ut magna irure",
  "address": "nisi id Ut sunt ips",
  "addressNumber": 61779923,
  "addressComplement": "aliqua sed cupidatat voluptate",
  "neighborhood": "laborum culpa laboris",
  "city": "qui",
  "state": "fugiat",
  "zipCode": "aliquip ex"
}


def massa_cadastrar_usuario():
    payload2 = json.dumps(payload)
    response = requests.post(url=url, headers=headers, data=payload2)
    return response.json()['id']


def test_deletar_cadastro_sucesso():
    id_deletar = massa_cadastrar_usuario()
    url_endpoint = str(f'{url}{id_deletar}')
    response = requests.delete(url=url_endpoint, headers=headers)
    print(f'\n [id deletado] {id_deletar}')
    print(f'\n [Status code] {response.status_code}')
    assert response.status_code == 200


def test_deletar_cadastro_nao_encontrado():
    url_endpoint = str(f'{url}999999999')
    response = requests.delete(url=url_endpoint, headers=headers)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 400
    assert response.json()['warning'] == 'Usuário não encontrado'


def test_deletar_hemocentro_erro_token():
    headers['Authorization'] = 'TokenInvalido'
    url_endpoint = str(f'{url}99')
    response = requests.delete(url=url_endpoint, headers=headers)
    print(f'\n [Status code] {response.status_code}')
    assert response.status_code == 401

