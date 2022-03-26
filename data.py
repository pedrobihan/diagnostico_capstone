# VOY A USAR ESTE ARCHIVO PARA PODER LEER UNA UNICA VEZ EL DATASET
import json

data_list = []
with open ('farmers-protest-tweets-dataset-raw-json/farmers-protest-tweets-2021-03-5.json', 'r') as f:
    for l in f.readlines():
        if not l.strip (): # skip empty lines
            continue

        data_list.append(json.loads (l))
