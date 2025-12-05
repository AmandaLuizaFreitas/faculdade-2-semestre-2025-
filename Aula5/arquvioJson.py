# Arquivos Binários

import json
pessoas = [
    {'nome': 'Ana', 'idade': 25},
    {'nome': 'Bruno', 'idade': 30},
    {'nome': 'Carla', 'idade': 28}
]

with open('pessoas.json', 'w') as arquivo_json:
    json.dump(pessoas, arquivo_json)
