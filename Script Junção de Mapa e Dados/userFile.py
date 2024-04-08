import json
from scriptJunção import funcaoprincipal

#Coloque aqui a rota até o arquivo Json dos dados
arquivo1 = '/home/paulathaines/Documentos/DEV/Funciona/aa.json' 

#Coloque aqui a rota até o arquivo Json da região
arquivo2 = '/home/paulathaines/Documentos/DEV/Funciona/testeretransmissorasRN.json' 

#Nome da Emissora
emissora = 'Tv Ponta Negra' 

#Sigla do estado
estado = 'RN' 

#Onde o arquivo novo seŕa salvo
arquivosaida = '/home/paulathaines/Documentos/DEV/Funciona/'

#Agora basta rodar o arquivo


###############################
######### NÃO MEXER ###########
###############################


arquivonovo = 'Mapa de cobertura '+emissora+" em "+estado+".json"
arquivofinal = arquivosaida+arquivonovo

conteudofinal = funcaoprincipal(arquivo1, arquivo2)

with open(arquivofinal, 'w', encoding='utf-8') as output:
    json.dump(conteudofinal, output, indent=2) #escrevendo o novo arquivo json

print("O script rodou sem complicações! Arquivo JSON criado foi salvo em:", arquivofinal) #confirmação
