from jira import JIRA



'''
options = {
    'server': 'https://hcs.jira.lanit.ru',
    'verify': False}
jira = JIRA(options)

authed_jira = JIRA(auth=('magzhanova', 'slaeM%62063'), options = {'server': 'https://hcs.jira.lanit.ru', 'verify': False}
                   )

issue_dict = {
    'project': {'id': id},
    'summary': 'test1',
    'description': 'Aloha',
    'issuetype': {'name': 'Task'},
}

issue1 = authed_jira.create_issue(fields=issue_dict)

authed_jira.assign_issue(issue1, 'ASoldatov')

authed_jira.add_comment(issue1, 'некая хрень')

'''

def auth_jira():
    options = {
        'server': 'https://hcs.jira.lanit.ru',
        'verify': False}
    jira = JIRA(options)

    authed_jira = JIRA(auth=('magzhanova', 'slaeM%62063'),
                       options={'server': 'https://hcs.jira.lanit.ru', 'verify': False}
                       )

    issue = authed_jira.issue('HCS-86692')

    for field_name in issue.raw['fields']:
        print ("Field:", field_name, "Value:", issue.raw['fields'][field_name])


    return authed_jira


def create_task(authed_jira, query_info):

    projects = authed_jira.projects()

    id = 0

    for i in projects:
        if (i.key == 'HCSINT'):
            id = i.id

    summary = query_info[3] + ' оптимизация ' + (query_info[0])[0:70]
    description = '''Долгая работа запроса: 
    
    {code}
    %s
    {code}
    
    Пример самого долгого запроса с параметрами (дата - %s) :
    
    {code}
    %s
    {code}
    

    
    Максимальное время - %s мс, минимальное время - %s мс
    Количество вызовов - %s
 
    '''%(query_info[0], query_info[6], query_info[4], query_info[1], query_info[2], query_info[5])


    if (len(query_info) > 7):
        description += '''Приеры долгих запросов с параметрами:
        {code}
        %s
        {code}
        '''%(query_info[7])
        if(len(query_info)>8):
            description += '''
            {code}
            %s
            {code}
            '''%(query_info[8])

    issue_dict = {
        'project': {'id': id},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Task'},
    }

    issue1 = authed_jira.create_issue(fields=issue_dict)

    return issue1


def create_hcs_task(authed_jira, query_info, in_trp, in_lead, in_analyst, in_qa, in_dba):

    projects = authed_jira.projects()

    id = 0

    for i in projects:
        if (i.key == 'HCS'):
            id = i.id

    summary = query_info[3] + ' оптимизация ' + (query_info[0])[0:70]
    description = '''Долгая работа запроса: 
    
    {code}
    %s
    {code}
    
    Пример самого долгого запроса с параметрами (дата - %s) :
    
    {code}
    %s
    {code}
    

    
    Максимальное время - %s мс, минимальное время - %s мс
    Количество вызовов - %s
 
    '''%(query_info[0], query_info[6], query_info[4], query_info[1], query_info[2], query_info[5])


    if (len(query_info) > 7):
        description += '''Приеры долгих запросов с параметрами:
        {code}
        %s
        {code}
        '''%(query_info[7])
        if(len(query_info)>8):
            description += '''
            {code}
            %s
            {code}
            '''%(query_info[8])



    issue_dict = {
        'project': {'id': id},
        'summary': summary,
        'issuetype': {'name': 'Bug'},
        'components': [{'name': 'База данных'},{'name': 'Оптимизация производительности'}],
#аналитик
        'customfield_10044': {'name': in_analyst},
#трп
        'customfield_15120':{'name': in_trp},
#тимлид
        'customfield_10828':{'name': in_lead},
#тестер
        'customfield_16120':{'name': in_qa},
        'fixVersions': [{'name': '12.2.8.0'}],
#Код сценария из ЧТЗ
        'customfield_12621':'-',
#Шаги воспроизведения
        'customfield_14531':'Выяснить, какой функционал пораждает запрос',
#Фактический результат
        'customfield_15522':description,
#Ожидаемый результат
        'customfield_15523':'Запрс выполняется менее * сек/мин',
#Ссылка на ЧТЗ
        'customfield_10821':'-',
        'environment':'FT01',
#Версия ЧТЗ
        'customfield_12120':'-',
#предусловие
        'customfield_15520':'-',
        'assignee':{'name': in_dba}

    }

    issue1 = authed_jira.create_issue(fields=issue_dict)

    return issue1


#    authed_jira.assign_issue(issue1, 'ASoldatov')

 #   authed_jira.add_comment(issue1, 'некая хрень')
'''
jira = JIRA('server': "http://<url>",
      basic_auth=("user", pass))

fields=jira.fields()

for field in fields:    
    print(field["name"])'''