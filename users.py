from data import data_list

usuarios_emisiones = {}

for i in range(len(data_list)):
    if data_list[i]['user']['username'] not in usuarios_emisiones:
        usuarios_emisiones[data_list[i]['user']['username']] = 1
    elif (data_list[i]['user']['username'] in usuarios_emisiones):
        usuarios_emisiones[data_list[i]['user']['username']] += 1


sort_retweets = sorted(usuarios_emisiones.items(), key=lambda x: x[1], reverse=True)

def imprimir_top_10tweeteros():
    for i in range(10):
        print(sort_retweets[i])