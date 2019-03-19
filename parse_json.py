import json
from pprint import pprint
import conn_db
import jira_
import io


def input_json():

#    with open('out_0820.json') as data_file:
#        data = (json.load(data_file))['normalyzed_info']
#log_2018_11_15_2.json
    with io.open('out_2019_03_19_01.json', encoding='utf-8') as data_file:
        data = (json.load(data_file))['normalyzed_info']

    return data


def find_new_slow_query(data):
    query_info = []

    k = 0

    for i in data:
        query_info.append([])
        query_info[k].append(i)

#        conn_db.write_query(i)

#перенести в main
#        if(not conn_db.find_in_db(i)):
#            conn_db.write_query(i)

        samples = (data[i])['samples']

#        max_time = max(samples)
#       query_info[k].append(max_time)

        max_dur = (data[i])['max']
        query_info[k].append(max_dur)

        min_dur = (data[i])['min']
        query_info[k].append(min_dur)

        db = samples[max_dur]["db"]
        query_info[k].append(db)

        max_query = samples[max_dur]["query"]
        query_info[k].append(max_query)

#        explain_plan = samples[max_dur]["plan"]
#        query_info[k].append(explain_plan)

        count = (data[i])['count']
        query_info[k].append(count)

        long_date = samples[max_dur]["date"]
        query_info[k].append(long_date)

        for i in samples:
            if(i != max_dur):
                query_info[k].append(samples[i]["query"])

        k += 1
#чтобы не генерить лишнего
        if(k == 1):
            return query_info
#потом убрать до сюда
    return query_info



