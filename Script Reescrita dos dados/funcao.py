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

def main(arquivo2):
    with open(arquivo2, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo) #carrega todo conteudo do arquivo json na variável dados

    for feature in dados:
        feature['Cidade'] = substituir_cedilha_por_c(feature['Cidade']) #utiliza a função "substituir..." em todas as features cidade

    with open(arquivo2, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=2) #reescreve o arquivo inicial

    print("Reescrita bem-sucedida!") #confirmação