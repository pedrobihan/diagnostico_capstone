from data import data_list

hashtags = {}

for j in range(len(data_list)):
    contenido = data_list[j]['renderedContent'].replace("\n", "").split(" ")
    for i in range(len(contenido)):
        if "#" in contenido[i]:
            indice_del_hash = contenido[i].find("#")
            if contenido[i][indice_del_hash:] not in hashtags:
                hashtags[contenido[i][indice_del_hash:]] = 1
            else:
                hashtags[contenido[i][indice_del_hash:]] = hashtags[contenido[i][indice_del_hash:]] + 1


sort_retweets = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)

def imprimir_top_10hashtags():
    for i in range(10):
        print(sort_retweets[i])


