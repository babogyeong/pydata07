import pandas as pd

# 각각의 CSV 파일에서 데이터 불러오기
senior_population_data = pd.read_csv('/users/user/Downloads/202311_202311_연령별인구현황_월간 (2).csv', encoding='cp949')  # 노인 인구 데이터
hospital_data = pd.read_csv('/users/user/Desktop/fulldata_01_01_01_P_병원.csv', encoding='cp949')  # 의료 기관 데이터

# '동', '면', '읍' 중 하나라도 포함된 행 선택  서울시, 서울시 서초구, 서울시 서초구 내곡동 처럼 중복되는 데이터가 있기에 동/면/읍으로만 끝나는 데이터 가져오기
df_filtered = senior_population_data[senior_population_data['행정구역'].str.contains('동|면|읍', regex=True)]

# 결과 출력
print(df_filtered)

# "상세영업상태명"이 "운영"인 행만 선택
df_operating = hospital_data[hospital_data['상세영업상태명'] == '영업중']

# 결과 출력
print(df_operating)


