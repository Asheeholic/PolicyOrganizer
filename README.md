# PolicyOrganizer
2022 05 07

async 처리 완료

남은일은 
1. 업로드 하는 파일 확인 만들기
2. 분석 제대로 만들기
3. 페이지 꾸미기 (마지막엔 패널까지 넣어보자)

------------------------------------------------------------------------------------
2022 05 04

async await 는 근본적인 해결이 안됨.

시간을 줄려니 다른 방식이 필요함.

다른 링크를 하나 더 줘서 다른 곳에 보내버리게 할까? 그게 나을 것 같은데, 그다음에 끝나기 전까지 대기 상태로 두다가 리다이렉트를 주면서 파일 다운로드 링크? 그게 나을지도?

1. 라우트 하나 추가
	대기 화면 하나 만들기 -> 그냥 쉽게 Rest 로 대기 페인 뜨게 하자.
2. 다운로드 상태가 끝나면 프로세스 전달 후 리다이렉트 전달
3. 다운로드 링크 클릭 후 파일 전달. 
4. 홈화면 버튼 추가.

아 제이슨으로 하려니 머리가 아프다. 안하던거 하니 ㄹㅇ 머리가 아프고 파이썬이니 다시 찾아봐야하고..

생각해본거
1. json으로 받아서 할려면 javascript 단에서 정보를 미리 넘겨야함.
	그게 아니면 플라스크 단에서 처리 할 수 있는 방식이 있을까? 가능은 할 수도
2. 파일 체크는 만들었는데, 페이지 넘기 말고 페인으로 작업하게 된다면 부트스트랩도 고려 해봐야함
3. 넘겨야 하는 데이터의 총 정보는 json으로 넘기면 된다 => 다양한 정보들을 전부 넘겨도 가능하지 않을까?
	예를 들어.. 파일 크기라던가, 아니면 데이터 성공 또는 실패 등등 분석 성공 실패 등등을 넘기면 가능 할 수도
4. 나중에 할일이지만 하루(짧으면 5분)마다 upload에 있는 모든 파일들을 지워야 하는 작업 해야함.
5. 현타온다.

이룬거
1. 부트스트랩, ajax 연결
2. 파일 있는지 확인 하는 작업 분리