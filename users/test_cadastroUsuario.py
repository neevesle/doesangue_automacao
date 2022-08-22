import requests
import json
import util.Token
import random

url = f"{util.Token.get_url()}/api/users"

email = random.random()

token = util.Token.get_token()

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
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}

def test_cadastro_usuario_sucesso():
  payload2 = json.dumps(payload)
  response = requests.post(url=url, headers=headers, data=payload2)
  print(f'\n [Status code] {response.status_code}')
  print(f'\n [Response] {response.json()}')
  assert response.status_code == 200
  assert response.json()['email'] == f'teste{email}@QA.com.br'


def test_cadastro_usuario_erro_sistemico():
  payloadRecebe = payload
  payloadRecebe['phone'] = 'dolor amet id 999999999999999999999999999999999999999999999' \
                           '9999999999999999999999999999999999999999999999999999999'
  payloadRecebe['email'] = f'{random.random()}'
  payloadFinal= json.dumps(payloadRecebe)
  response = requests.post(url=url, headers=headers, data=payloadFinal)
  print(f'\n [Status code] {response.status_code}')
  print(f'\n [Response] {response.json()}')
  assert response.status_code == 500
  assert 'Ocorreu um erro ao processar a requisição' in response.json()['message']






