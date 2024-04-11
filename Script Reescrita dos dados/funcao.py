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

def rename_properties(data):
    for item in data:
        if 'Cidade' in item:
            item['name'] = item.pop('Cidade')
        if 'Consult2' in item:
            item['value'] = item.pop('Consult2')
    return data

def main(arquivo2):
    with open(arquivo2, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo) #carrega todo conteudo do arquivo json na variável dados

    for feature in dados:
        feature['name'] = substituir_cedilha_por_c(feature['name']) #utiliza a função "substituir..." em todas as features cidade

    rename_properties(dados)

    with open(arquivo2, 'w', encoding='utf-8') as arquivo: #reescriya do arquivo
        arquivo.write('[\n')
        for index, item in enumerate(dados):
            json.dump(item, arquivo),
            if index < len(dados)-1:  # verifica se nao é o último item
                arquivo.write(',\n')
        arquivo.write('\n]')

    print("Reescrita bem-sucedida!") #confirmação



