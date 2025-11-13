import requests

def buscar_cep(cep_usuario):
    link_api = "https://cep.awesomeapi.com.br/json"
    url = f"{link_api}/{cep_usuario}"
    try:
        requisicao_cep = requests.get(url, timeout=5)

        # Verifica se a resposta foi bem-sucedida
        if requisicao_cep.status_code != 200:
            raise Exception(f"Erro na requisição: {requisicao_cep.status_code}")

        # Verifica se há conteúdo na resposta
        if not requisicao_cep.content:
            raise Exception("Resposta vazia da API")

        cep_dic = requisicao_cep.json()

        # Verifica se a resposta contém erro
        if "status" in cep_dic and cep_dic["status"] == 404:
            return None

        cep = cep_dic.get('cep')
        endereco = cep_dic.get('address')
        bairro = cep_dic.get('district')
        cidade = cep_dic.get('city')
        estado = cep_dic.get('state')
        latitude = float(cep_dic.get('lat', 0))
        longitude = float(cep_dic.get('lng', 0))

        return [cep, endereco, bairro, cidade, estado, latitude, longitude]

    except Exception as e:
        raise Exception(f"Erro ao buscar o CEP: {e}")