# Python-Project

현재 구현된 기능[Updated : 2019년 4월 1일]
- 지라 JQL코드를 통하여 금일 이슈로 등록된 것들을 가지고 옴 
(* JQL 변경을 통해 다른 것들을 가지고 올 수 있음)
- 결과 값을 통해 금일날짜에 등록된 이슈의 번호와, 제목 그리고 이슈의 갯수를 슬랙에 알람

추가 구현예정 기능
- 현재 이슈 중 AOS, IOS에 관련하여 각각 분류하여 슬랙에 각 항목별로 이슈의 갯수와 번호, 제목을 뿌려주는 기능 제공 예정
- slack, mail 등을 이용한 알람 메시지 연동기능 추가 예정
- 코드 고도화

(외부 모듈)
JIRA : JIRA 접근 및 JQL을 사용하기 위한 모듈
[설치방법 : pip install JIRA or pycharm plugin을 통한 검색 후 적용]
Slacker : slack 알림을 사용하기 위한 모듈
[설치방법 : pip install slacker or pycharm plugin을 통함 검색 후 적용
