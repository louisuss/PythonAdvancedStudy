import os  # 경로
import time  # 성능 측정
import sys
import csv
from concurrent import futures

# concurrent.futures 방법1
# ThreadPoolExecutor, ProcessPoolExecutor
# map()
# 서로 다른 스레드 또는 프로세스에서 실행가능
# 내부 과정 알 필요 없으며, 고수준으로 인터페이스 제공
# 글로번 인터프리터 락?
# Google Python GIL (Global Interpreter Lock)
# Gil은 한 번에 하나의 스레드만 수행 할 수 있게 인터프리터 자체에서 락을 거는 것. 안정성 이유.

# split 함수 통해 리스트로 생성
NATION_LS = (
    'Singapore Germany Israel Norway Italy Canada France Spain Maxico').split()

# 초기 CSV 위치
TARGET_CSV = '/Users/louis/Python/AdvancedPython/res/nations.csv'

# 저장 폴더 위치
DEST_DIR = '/Users/louis/Python/AdvancedPython/csvs'

# CSV 헤더 기초 정보
# ['Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority', 'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']
HEADER = 'Region, Country, Item Type, Sales Channel, Order Priority, Order Date, Order ID, Ship Date, Units Sold, Unit Price, Unit Cost, Total Revenue, Total Cost, Total Profit'.split(
    ', ')


# 국가별 분리
def get_sales_data(nt):
    with open(TARGET_CSV, 'r') as f:
        reader = csv.DictReader(f)
        # Dict을 리스트로 적재
        data = []
        # Header 확인
        # print(reader.fieldnames)
        for r in reader:
            # OrderedDict 확인
            # print(r)
            # 조건에 맞는 국가만 삽입
            if r['Country'] == nt:
                data.append(r)
    return data

# 중간 상황 출력


def show(text):
    print(text, end=' ')
    # 중간 출력(버퍼 지우기)
    sys.stdout.flush()

# 국가별 CSV 파일 저장


def save_csv(data, filename):
    # 최종 경로 생성
    path = os.path.join(DEST_DIR, filename)

    # 줄바꿈 처리 안되게 하기 위해 newline=''사용
    with open(path, 'w', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=HEADER)

        # Header Write
        writer.writeheader()
        # Dict to CSV Write
        for row in data:
            writer.writerow(row)

# 국가 별 분리 함수 싱행


def seperate_many(nt):
    # for nt in sorted(nt_list):
    # 분리 데이터
    data = get_sales_data(nt)

    # 상황 출력
    show(nt)

    # 파일 저장
    save_csv(data, nt.lower() + '.csv')

    return nt

# 시간 측정 및 메인 함수


def main(seperate_many):
    # worker 개수
    worker = min(20, len(NATION_LS))
    # 시작 시간
    start_tm = time.time()

    # 결과 건수
    # ProcessPoolExecutor : GIL 우회, 변경 후 -> os.cpu_count()
    # ThreadPoolExecutor : GIL 종속

    # with futures.ThreadPoolExecutor(worker) as executor:
    # 처리 속도는 빨라지지만 CPU 사용 극대화
    with futures.ProcessPoolExecutor(worker) as executor:
        # map -> 작업 순서 유지, 즉시 실행
        result_cnt = executor.map(seperate_many, sorted(NATION_LS))
    # 종료 시간
    end_tm = time.time() - start_tm

    msg = '\n{} csv separated in {:.2f}s'

    # 최종 결과 출력
    print(msg.format(list(result_cnt), end_tm))


# 실행
if __name__ == '__main__':
    main(seperate_many)
