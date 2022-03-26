from data import data_list

different_days = {}

for i in range(len(data_list)):
    if (data_list[i]['date'])[0:10] not in different_days:
        different_days[data_list[i]['date'][0:10]] = 1
    elif ((data_list[i]['date'])[0:10] in different_days) :
        different_days[data_list[i]['date'][0:10]] = different_days[data_list[i]['date'][0:10]] + 1


sort_retweets = sorted(different_days.items(), key=lambda x: x[1], reverse=True)

def imprimir_top_10days():
    for i in range(10):
        print(sort_retweets[i])