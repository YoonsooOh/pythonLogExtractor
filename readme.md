## Python Log 추출 예제

> 10,000 명 이상의 조회 수를 보유하고 있는 강의자 수 카운팅을 위해 신규 지표인 `total_view_for_famous_teacher` 를 ACC Log에 추가하는 상황을 가정합니다.
> (실제 상황에서는 DB에 이미 카운팅이 되어 있겠죠.)
> 10,000 명 이상의 조회 수를 가진 강의자가 접속하면 ACC LOG 에 `total_view_for_famous_teacher`항목이 표시됩니다.

> e.g.) </br>
> {"time": "17/May/2015:08:05:20 +0000", "remote_ip": "217.168.17.5", "remote_user": "-", "request": "GET /downloads/product_2 HTTP/1.1", "response": 200, "bytes": 3316, "referrer": "-", "agent": "-" , **"total_view_for_famous_teacher":50021**}



- 코드: 
  - [main.py](main.py)


- 추출 결과
  - [result.md](result.md)
