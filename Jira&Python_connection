from jira import JIRA, JIRAError
from datetime import date
from datetime import timedelta
from datetime import datetime
from slacker import Slacker
import sys


# search jira function #
def jira_Conn_Search():

    # jira id/ pasword / server
    user                = 'jira ID'
    apikey              = 'jira PASSWD'
    server              = 'jira SERVER'

    # issue & issue Count variable
    temp_list           = []
    temp_list_Count     = []

    # call select_Data Function
    Query_Data          = select_Data()

    # jira connction
    try:

        options         = {'server': server}
        jira            = JIRA(options, basic_auth=(user, apikey))

        for search_query in Query_Data:

            Current_Search_Result = jira.search_issues(search_query)
            # Check Count current issue list
            temp_list_Count.append(len(Current_Search_Result))
            # Check current issue list
            temp_list.append(Current_Search_Result)

        return temp_list

    except JIRAError as e:

        print(e.status_code, e.text)
        sys.exit(1)

# search data function
def select_Data():

    # Today
    current_day         = date.today().isoformat()
    # Yesterday
    yester_day          = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    # JSQL Query

    # Current all issue jql
    All_Query           = "project = QA AND issuetype = '오류 / 버그' AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"
    # Current AOS issue jql
    AOS_Query           = "project = QA AND issuetype = '오류 / 버그' AND component = AOS AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"
    # Current IOS issue jql
    IOS_Query           = "project = QA AND issuetype = '오류 / 버그' AND component = IOS AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"
    # Current NOT IOS/ AOS jql
    NOT_Query           = "project = QA AND issuetype = '오류 / 버그' AND component not in (AOS, IOS) AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"

    temp_list           = [All_Query, AOS_Query, IOS_Query, NOT_Query]

    return temp_list

# View Check Data
def view_Check_data(Data, Num):
    slack_alarm(Data, Num)

# Slack alarm
def slack_alarm(Result, Num):

    # my slack Token
    slack_Token        = '슬랙 접근 Token api'
    # input slack Token
    slack = Slacker(slack_Token)

    # Current filter number
    # 0 : ALL, 1 : AOS, 2 : IOS , 3 : NOT
    Issue_Component = ['ALL', 'AOS', 'IOS', 'Etc']

    count = len(Result)
    slack.chat.post_message('#python_alarmtest', Issue_Component + '이슈 등록건수 는' + count + '입니다.')

    # Current register filter informtaion
    for r_data in Result:
        slack.chat.post_message('#python_alarmtest', r_data.fields.summary)

# Main Start
if __name__ == '__main__':

    C_Num = 0
    Data = jira_Conn_Search()

    while C_Num in range(0, len(Data)):
        view_Check_data(Data[C_Num], C_Num)
        C_Num = C_Num + 1
