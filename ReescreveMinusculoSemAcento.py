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


caminho_arquivo = "/home/paulathaines/Documentos/DEV/Funciona/testeretransmissorasRN.json"

with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    for feature in dados['features']:
        properties = feature['properties']
        for propriedade, valor in properties.items():
            if isinstance(valor, str):
                properties[propriedade] = substituir_cedilha_por_c(valor)

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2)
