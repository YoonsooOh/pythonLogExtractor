import json

def print_log_sample():
    raw_log_line = '{"time": "04/Jun/2015:06:06:24 +0000", "remote_ip": "192.235.75.62", "remote_user": "-", "request": "GET /downloads/product_1 HTTP/1.1", "response": 304, "bytes": 0, "referrer": "-", "agent": "Debian APT-HTTP/1.3 (0.8.16~exp12ubuntu10.12)"}'
    json_dict = json.loads(raw_log_line)
    print(json_dict)
    print(json_dict["time"])
    print(json_dict["request"])
    print(json_dict["response"])
    print(json_dict["agent"])
    print(json_dict["remote_ip"])


def print_sample_acc_log_file():
    with open("sample_acc_100.log", "r", encoding='utf-8') as file:
        for log in file:
            log = log.strip()
            json_dict = json.loads(log)
            print(json_dict["time"])
            print(json_dict["remote_ip"])

if __name__ == '__main__':
    # log file을 file이라는 변수로 가져오기 "r" : read, utf-8은 한글 포함 모든 문자열 다루기
    with open("sample_acc_new_index.log", "r", encoding='utf-8') as file:
        # file 에서 한줄 씩 log를 읽기
        for log in file:
            # log에 있는 엔터, 스페이스 등 필요없는 공백 제거하기
            log = log.strip()
            # dict 형으로 log를 변환하기
            json_dict = json.loads(log)
            # 신규 지표인 total_view_for_famous_teacher 가 있는지 확인하기
            if ("total_view_for_famous_teacher" in json_dict) :
                # 신규 지표가 있으면 출력하기
                print(json_dict["total_view_for_famous_teacher"])



