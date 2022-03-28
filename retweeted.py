from data import data_list

usuarios_y_tweets = {}

for i in range(len(data_list)):
    if data_list[i]['user']['username'] not in usuarios_y_tweets:
        usuarios_y_tweets[data_list[i]['user']['username']] = data_list[i]['retweetCount']
    elif (data_list[i]['user']['username'] in usuarios_y_tweets) & (data_list[i]['retweetCount'] != 'null'):
        if(data_list[i]['retweetCount'] > usuarios_y_tweets[data_list[i]['user']['username']]):
            usuarios_y_tweets[data_list[i]['user']['username']] = data_list[i]['retweetCount']


sort_retweets = sorted(usuarios_y_tweets.items(), key=lambda x: x[1], reverse=True)

def imprimir_top_10retweets():
    for i in range(10):
        print(sort_retweets[i])