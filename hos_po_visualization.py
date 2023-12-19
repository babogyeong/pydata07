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
#총 인구수 결측치 제거(인구수 0이 아닌 결측치)
merged_data = merged_data.dropna(subset=['2023년11월_계_총인구수'])
#1,000단위 쉼표 제거
merged_data['2023년11월_계_총인구수'] = merged_data['2023년11월_계_총인구수'].str.replace(',', '').astype('int64')


#병원개수 및 총인구수 기준 하위 30개
merged_cut_data = merged_data.nsmallest(30, columns=['병원개수', '2023년11월_계_총인구수'])

# 시각화
plt.figure(figsize=(12, 6))

# 노인 총 인구수 대비 병원개수 적은 동 찾기
sns.scatterplot(x='병원개수', y='2023년11월_계_총인구수', data=merged_cut_data, hue='동', palette='hsv', s=100, alpha = 0.4)
plt.title('노인 총 인구수 대비 병원 개수 적은 동')
plt.xlabel('병원 개수')
plt.ylabel('노인 인구')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()