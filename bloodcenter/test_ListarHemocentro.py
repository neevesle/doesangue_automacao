import requests
import util.Token

payload = {}

url = f'{util.Token.get_url()}/api/bloodcenter/'

token = util.Token.get_token()

headers = {
  'Accept': 'text/plain',
  'Authorization': f'Bearer {token}'
}


def test_consultar_hemocentro_sucesso():
    id_hemocentro = 2
    url_endpoint = str(f'{url}{id_hemocentro}')
    response = requests.get(url=url_endpoint, headers=headers, data=payload)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 200
    assert response.json()['id'] == 2
    assert response.json()['active'] is True

def test_consultar_hemocentro_nao_encontrado():
    id_hemocentro = 999999
    url_endpoint = str(f'{url}{id_hemocentro}')
    response = requests.get(url=url_endpoint, headers=headers, data=payload)
    print(f'\n [Status code] {response.status_code}')
    print(f'\n [Response] {response.json()}')
    assert response.status_code == 400
    assert response.json()['warning'] == 'Hemocentro não encontrado'

def test_consultar_hemocentro_token_invalido():
    id_hemocentro = 2
    headers['Authorization'] = 'TokenInvalido'
    url_endpoint = str(f'{url}{id_hemocentro}')
    response = requests.get(url=url_endpoint, headers=headers)
    print(f'\n [Status code] {response.status_code}')
    assert response.status_code == 401

