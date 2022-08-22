import requests
import util.Token

payload = {}

url = f'{util.Token.get_url()}/api/posts'

token = util.Token.get_token()

headers = {
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}


def test_listar_solicitacao_sucesso():
    response = requests.get(url=url, headers=headers, data=payload)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 200
    assert response.json()[1]['beneficiaryName'] == 'Leticia Neves QA'
    assert response.json()[1]['id'] == 2


def test_listar_solicitacao_token_invalido():
    headers['Authorization'] = 'TokenInvalido'
    response = requests.get(url=url, headers=headers)
    print(f'\n [Status code] {response.status_code}')
    assert response.status_code == 401

