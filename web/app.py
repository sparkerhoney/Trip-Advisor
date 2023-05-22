import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit as st



# 페이지 기본 설정
st.set_page_config(
   page_icon="🚌",
   page_title="Trip Advisor",
   layout="wide",
)

#페이지 헤더, 서브헤더 제목 설정
st.header("Trip Advisor")
st.subheader("당신에게, 최고의 여행 스케쥴러")

iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
  return species_dict[x]


df['species'] = df['species'].apply(mapp_species)
print(df)

# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title('여행지 설정')

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_species = st.sidebar.selectbox(
    '가고싶은 여행지를 설정해주세요',
    ['제주도']
)

# 여러개 선택할 수 있을 때는 multiselect를 이용하실 수 있습니다 
# return : list
select_multi_species = st.sidebar.multiselect(
    '가고싶은 관광지의 키워드를 설정해주세요. 복수선택가능',
    ["분위기", "로맨틱", "화려한", "아늑한", "모험적인", "신비로운", "편안한", "현대적인", "고요한", "전통적인", "활기찬", "이국적인", "로컬한", "청량한", "친환경적인", "힐링", "인스타감성", "자연친화적인", "감성적인", "레트로", "다채로운", "세계적인", "스포티한", "명상적인", "역사적인", "아트", "리조트", "도시적인", "농촌적인", "학문적인", "아이와 함께", "배움", "건강한"]

)

# 원래 dataframe으로 부터 꽃의 종류가 선택한 종류들만 필터링 되어서 나오게 일시적인 dataframe을 생성합니다
tmp_df = df[df['species'].isin(select_multi_species)]
# 선택한 종들의 결과표를 나타냅니다.  
st.table(tmp_df)

# 라디오에 선택한 내용을 radio select변수에 담습니다
radio_select =st.sidebar.radio(
    "what is key column?",
    ['sepal length', 'sepal width', 'petal length','petal width'],
    horizontal=True
    )
# 선택한 컬럼의 값의 범위를 지정할 수 있는 slider를 만듭니다. 
slider_range = st.sidebar.slider(
    "choose range of key column",
     0.0, #시작 값 
     10.0, #끝 값  
    (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능
)

# 필터 적용버튼 생성 
start_button = st.sidebar.button(
    "filter apply 📊 "#"버튼에 표시될 내용"
)

# button이 눌리는 경우 start_button의 값이 true로 바뀌게 된다.
# 이를 이용해서 if문으로 버튼이 눌렸을 때를 구현 
if start_button:
    tmp_df = df[df['species'].isin(select_multi_species)]
    #slider input으로 받은 값에 해당하는 값을 기준으로 데이터를 필터링합니다.
    tmp_df= tmp_df[ (tmp_df[radio_select] >= slider_range[0]) & (tmp_df[radio_select] <= slider_range[1])]
    st.table(tmp_df)
    # 성공문구 + 풍선이 날리는 특수효과 
    st.sidebar.success("Filter Applied!")
    st.balloons()