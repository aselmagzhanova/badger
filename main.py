import json
from pprint import pprint
import conn_db
import jira_
import io
import parse_json
import zlib


if __name__ == '__main__':

    data = parse_json.input_json()


    query_info = parse_json.find_new_slow_query(data)
    auth_jira = jira_.auth_jira()

    rg_number = int(input('рабочая группа:'))
    members = conn_db.find_rg_members(rg_number)

    for i in query_info:
#        print(len(i))
#        print(i)
        if(not conn_db.find_in_db(zlib.crc32(i[0].encode('utf-8')) & 0xffffffff)):
            auth_jira = jira_.auth_jira()
            task = jira_.create_hcs_task(auth_jira, i, members[0][2], members[0][3], members[0][4], members[0][5], members[0][6])
            conn_db.write_query(zlib.crc32(i[0].encode('utf-8')) & 0xffffffff, i[0], i[3], task)


            #task = jira_.create_task(auth_jira, i)
            #print(task)
