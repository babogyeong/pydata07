#노인 인구수, 병원 주소 비교 -> 동별로 통합 및 시각화
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')

# CSV 파일 읽기
hospital_data = pd.read_csv('fulldata_01_01_01_P_병원.csv', encoding='cp949')
population_data = pd.read_csv('202311_202311_연령별인구현황_월간 (2).csv', encoding='cp949')  # 파일 인코딩이 필요한 경우 지정

# '소재지전체주소'에서 동 정보 추출
hospital_data['동'] = hospital_data['소재지전체주소'].str.extract(r'\b(\S+[동읍면리])\b')

# 주소 데이터 정리
population_data['행정구역'] = population_data['행정구역'].str.replace(r'\([^)]*\)', '', regex=True)
population_data['동'] = population_data['행정구역'].str.extract(r'(\S+[동읍면리])')

# 노인 총 인구수 추출
population_data = population_data[['동', '2023년11월_계_총인구수']]

# 병원 개수 세기
hospital_count = hospital_data['동'].value_counts().reset_index()
hospital_count.columns = ['동', '병원개수']

# 데이터 병합
merged_data = pd.merge(hospital_count, population_data, on='동', how='outer')

# 시각화
plt.figure(figsize=(12, 6))

# 병원 개수와 노인 총 인구수의 관계 시각화
sns.scatterplot(x='병원개수', y='2023년11월_계_총인구수', data=merged_data, hue='동', palette='viridis', s=100)
plt.title('병원 개수와 노인 총 인구수의 관계')
plt.xlabel('병원 개수')
plt.ylabel('2023년11월_계_총인구수')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()