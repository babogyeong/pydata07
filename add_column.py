import pandas as pd

# CSV 파일 읽어오기
df = pd.read_csv('전국의료기관표준데이터.csv', encoding='cp949')

# 의료기관 분류 함수 정의
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

# '의료기관분류' 열 추가
df['의료기관분류'] = df['병상수'].apply(classify_hospital)

#결과 확인
print(df)
#print(df[['번호', '병상수', '의료기관분류']])