#필요한 모듈 임포트
import pandas as pd

# 필요한 CSV 파일 읽어오기
df = pd.read_csv('전국의료기관표준데이터.csv', encoding='cp949')

# 의료기관 분류 함수 정의
# 병상수 기준으로 30개 미만은 '의원', 30~100 병상은 '병원' 100~500 병상은 종합병원, 500 병상 이상은 상급종합병원으로 분류
def classify_hospital(size):
    if size < 30:
        return '의원'
    elif 30 <= size < 100:
        return '병원'
    elif 100 <= size < 500:
        return '종합병원'
    elif size >= 500:
        return '상급종합병원'
    else:
        return '분류불가'

# 병상수 기준으로 분류한 데이터를 새로운 '의료기관분류' 컬럼에 추가
df['의료기관분류'] = df['병상수'].apply(classify_hospital)

#결과 출력
print(df)
