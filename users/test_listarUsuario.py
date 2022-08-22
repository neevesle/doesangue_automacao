import requests
import util.Token

payload = {}

url = f'{util.Token.get_url()}/api/users/'

token = util.Token.get_token()

headers = {
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}


def test_consultar_usuario_id_sucesso():
    id_usuario = 1
    url_endpoint = str(f'{url}{id_usuario}')
    response = requests.get(url=url_endpoint, headers=headers, data=payload)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['email'] == 'teste@QA.com.br'

def test_consultar_usuario_sem_id_sucesso():
    url_endpoint = str(f'{url}')
    response = requests.get(url=url_endpoint, headers=headers, data=payload)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 200
    assert response.json()[2]['id'] == 3
    assert response.json()[2]['name'] == 'Teste QA Leticia automatico'

def test_consultar_usuario_nao_encontrado():
    id_usuario = 999999
    url_endpoint = str(f'{url}{id_usuario}')
    response = requests.get(url=url_endpoint, headers=headers, data=payload)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 400
    assert response.json()['warning'] == 'Usuário não encontrado'

def test_consultar_usuario_token_invalido():
    id_usuario = 2
    headers['Authorization'] = 'TokenInvalido'
    url_endpoint = str(f'{url}{id_usuario}')
    response = requests.get(url=url_endpoint, headers=headers)
    print(f'\n [Status code] {response.status_code}')
    assert response.status_code == 401

