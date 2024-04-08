import json


def funcaoprincipal(file1_path, file2_path):
    with open(file1_path, 'r', encoding='utf-8') as file1:
        data1 = json.load(file1) #aloca o conteudo do arquivo dos dados em uma variável
        
    with open(file2_path, 'r', encoding='utf-8') as file2:
        data2 = json.load(file2) #aloca o conteudo do arquivo do mapa em uma variável

    arraydecidades = {entry['Cidade']: entry['Consult2'] for entry in data1} #cria um array com todas as cidades do arquivo json de dados

    for feature in data2['features']: #repete o processo a seguir para cada feature do arquivo de mapa
        cidade = feature['properties']['description'] #aloca o valor da propriedade descripition em uma variável
        if cidade in arraydecidades: #verifica se a cidade existe no json de dados
            feature['properties']['Consult2'] = arraydecidades[cidade] #cria nova feature com valor de consult2

    return data2

    #criando o arquivo com resultado
    arquivonovo = 'Mapa de cobertura '+emissora+" em "+estado+".json"
    arquivofinal = arquivosaida+arquivonovo

    #chamando a função principal
    conteudofinal = funcaoprincipal(arquivo1, arquivo2)

    # Salvar o resultado em um novo arquivo JSON
    with open(arquivofinal, 'w', encoding='utf-8') as output:
        json.dump(conteudofinal, output, indent=2) #escrevendo o novo arquivo json

    print("O script rodou sem complicações! Arquivo JSON criado foi salvo em:", arquivofinal) #confirmação


