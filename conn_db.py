import sqlite3

def write_query(hash, query, db, task):
    conn = sqlite3.connect("mydatabase.db")  # или :memory: чтобы сохранить в RAM
    cursor = conn.cursor()
    cursor.execute("INSERT INTO queries (hash, query_text, data, database, task_number) values('%s', '%s', date('now'), '%s', '%s') " % (hash, query, db, task))
    conn.commit()
    conn.close()


def find_in_db(query):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("select 1 from queries where hash = '%s'" % query)
#    print('*********')
#    print(cursor.fetchone())
#    conn.commit()
#    conn.close()

    if (cursor.fetchone()):
        conn.commit()
        conn.close()
        return True
    else:
        conn.commit()
        conn.close()
        return False


def find_rg_members(rg_num):
    members = []
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    sql = "select * from rg_matrix where rg_number = ?"
    cursor.execute(sql, [(5)])
    members = cursor.fetchall()
#    print(members[0][1])
    conn.commit()
    conn.close()
    return members

