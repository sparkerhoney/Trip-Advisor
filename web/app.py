import pandas as pd
import streamlit as st
import pydeck as pdk
import openai

# 페이지 기본 설정
st.set_page_config(
   page_icon="🚌",
   page_title="Trip Advisor",
   layout="wide",
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("Trip Advisor")
st.subheader("당신에게, 최고의 여행 스케쥴러")

# 사이드바에 select box를 활용하여 종을 선택한 다음 그에 해당하는 행만 추출하여 데이터프레임을 만들고자합니다.
st.sidebar.title('여행지 설정')

# select_species 변수에 사용자가 선택한 값이 지정됩니다
select_species = st.sidebar.selectbox(
    '가고싶은 여행지 설정',
    ['제주도']
)

keywords = ["분위기", "로맨틱", "화려한", "아늑한", "모험적인", "신비로운", "편안한", "현대적인", "고요한", "전통적인", "활기찬", "이국적인", "로컬한", "청량한", "친환경적인", "힐링", "인스타감성", "자연친화적인", "감성적인", "레트로", "다채로운", "세계적인", "스포티한", "명상적인", "역사적인", "아트", "리조트", "도시적인", "농촌적인", "학문적인", "아이와 함께", "배움", "건강한"]

# select_multi_species 변수에 사용자가 선택한 키워드들이 지정됩니다.
select_multi_species = st.sidebar.multiselect(
    '관광지 키워드 설정',
    keywords
)

# 여행 시작 버튼 생성
start_button = st.sidebar.button('여행 시작!')

# OpenAI API key 설정
openai.api_key = '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'

if start_button:
    if len(select_multi_species) != 3:  # 3개의 키워드가 선택되지 않은 경우 경고 메시지를 출력합니다.
        st.sidebar.warning('3개의 키워드를 모두 선택해주세요.')
    else:
        # 가정된 "모델"을 실행하고 결과를 출력합니다.
        model_output = ", ".join(select_multi_species)
        st.write(f"당신의 여행 키워드는 다음과 같습니다: {model_output}")

        # 제주도 위도, 경도
        latitude = 33.4906
        longitude = 126.4987

        # 제주도 지도 생성
        jeju_map = pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=latitude,
                longitude=longitude,
                zoom=11,
                pitch=50,
            ),
        )

        # 위치 데이터 프레임 생성
        data = pd.DataFrame(
            {
            'lat': [33.4982, 33.4892, 33.4851],
            'lon': [126.5312, 126.5323, 126.5432],
            'name': ['Location A', 'Location B', 'Location C'],
            }
        )
        # Pydeck Layer 생성
        layer = pdk.Layer(
            'ScatterplotLayer',  # 사용할 레이어 유형
            data,  # 사용할 데이터
            get_position=['lon', 'lat'],  # 위치 정보 칼럼
            get_radius=1000,  # 마커 크기
            get_fill_color=[180, 0, 200, 140],  # 마커 색상
            pickable=True, tooltip={"text": "{name}"}
        )
        # Deck 생성 후 레이어 추가
        jeju_map = pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=33.4890,
                longitude=126.4982,
                zoom=11,
                pitch=50,
            ),
            layers=[layer],
        )
        # 지도를 Streamlit 앱에 추가
        st.pydeck_chart(jeju_map)

        # 여기서부터 챗 GPT API 호출 부분 추가
        response = openai.ChatCompletion.create(
            model="text-davinci-002",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"I want to have a {model_output} trip to {select_species}. Can you recommend an itinerary?"},
            ]
        )

        # API 응답을 사용자에게 출력
        st.write(response['choices'][0]['message']['content'])


