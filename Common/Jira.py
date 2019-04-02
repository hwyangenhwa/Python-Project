from jira import JIRA
from slacker import Slacker
from datetime import date
from datetime import timedelta
from datetime import datetime
import win32com.client
import sys
import os

# Project 인자값에 대한것은 Slack 쪽 Coomand 로직 작성 이후 TO DO
todo = 'todo'

# 현재 폴더의 경로의 정보를 얻기
path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

# Main Start #
if __name__ == '__main__':
    # my jira id/ pasword / server        
    user        = '지라 접근 아이디 입력'
    apikey      = '지라 Token api 입력'
    server      = '지라 서버 URL'

    # my slack Token
    slack_Token = '슬랙 접근 Token api'

    # jira connction
    options     = {'server' : server}
    jira        = JIRA(options, basic_auth=(user,apikey))

    # slack channel, # channel setting '#channel'
    slack       = Slacker(slack_Token)


    # search data function
    # request 함수를 Slack 에서 받아와 Command 별로 다른 결과값을 배출
def select_Data(request):

    # today #
    current_day = date.today().isoformat()

    # yesterday #
    yester_day = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    
    
    # Project 인자값에 대한것은 Slack 쪽 Coomand 로직 작성 이후 TO DO
    # current all issue jql
    All_Query = "project = QA AND issuetype = '오류 / 버그' AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"
    
    # current AOS issue jql
    AOS_Query = "project = QA AND issuetype = '오류 / 버그' AND component = AOS AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"
    
    # current IOS issue jql
    IOS_Query = "project = QA AND issuetype = '오류 / 버그' AND component = IOS AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"
    
    # current NOT IOS/ AOS jql
    NOT_Query = "project = QA AND issuetype = '오류 / 버그' AND component not in (AOS, IOS) AND created >=" + yester_day + " AND created <=" + current_day + " ORDER BY priority DESC, updated DESC"
    
    
    if(request == todo):
        temp_list = [All_Query]
        return temp_list

    
