import json

def substituir_cedilha_por_c(texto):
    acentos = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'ä': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
               'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ö': 'o',
               'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'ç': 'c',
               'Á': 'a', 'À': 'a', 'Â': 'a', 'Ã': 'a', 'Ä': 'a', 'É': 'e', 'È': 'e', 'Ê': 'e', 'Ë': 'e',
               'Í': 'i', 'Ì': 'i', 'Î': 'i', 'Ï': 'i', 'Ó': 'o', 'Ò': 'o', 'Ô': 'o', 'Õ': 'o', 'Ö': 'o',
               'Ú': 'u', 'Ù': 'u', 'Û': 'u', 'Ü': 'u'}
    texto_sem_acentos = ''.join(acentos.get(char, char) for char in texto)
    texto_minusculo = texto_sem_acentos.lower() 
    
    return texto_minusculo

def main(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo: #abre o arquivo para leitura
        dados = json.load(arquivo) #armazena todo conteúdo do arquivo json na variável dados
        for feature in dados['features']:
            properties = feature['properties'] #armazena as propriedades em uma variável (para cada propriedade de cada feature)
            for propriedade, valor in properties.items(): #items() é um método python que chama chave e valor
                if isinstance(valor, str): #verifica se o valor da propriedade é uma string
                    properties[propriedade] = substituir_cedilha_por_c(valor) #executa a função no valor da propriedade

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo: # abre o arquivo para escrita
        arquivo.write('[\n')
        for index, feature in enumerate(dados['features']):
            json.dump(feature, arquivo)
            if index < len(dados['features']) - 1:  # verifica se não é o último item
                arquivo.write(',\n')
        arquivo.write('\n]')

    print("Reescrita bem-sucedida!")