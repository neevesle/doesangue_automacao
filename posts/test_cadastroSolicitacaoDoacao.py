import requests
import json

import util.Token

url_endPoint = f"{util.Token.get_url()}/api/posts"

token = util.Token.get_token()

payload = {
  "beneficiaryName": "Leticia Neves QA",
  "bloodCenterId": -88089940,
  "content": "ad veniam aliquip dolor",
  "imagePath": "Caminho IMG"
}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}


def test_cadastro_solicaitacao_sucesso():
    payload2 = json.dumps(payload)
    response = requests.post(url=url_endPoint, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 200

def test_cadastro_solicaitacao_erro():
    payload2 = json.dumps({})
    response = requests.post(url=url_endPoint, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 500
    assert 'Ocorreu um erro ao processar a requisição.' in response.json()['message']


def test_cadastro_solicitacao_erro_token():
    payload2 = json.dumps(payload)
    headers['Authorization'] = 'TokenInvalido'
    response = requests.post(url=url_endPoint, headers=headers, data=payload2)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [payload] {payload}')
    assert response.status_code == 401

