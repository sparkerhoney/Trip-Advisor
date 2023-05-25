import streamlit as st
import streamlit.components.v1 as components

def Kakao_map(num, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5):
    my_component = components.declare_component(
        "my_component",
        url="http://localhost:3001"
    )

    # Streamlit 애플리케이션의 제목 설정
    st.title('카카오맵 API 예제')

    # HTML 작성
    components.html(
        f'''
        <!DOCTYPE html>
        <html>
        <head>
        	<meta charset="utf-8"/>
        	<title>Kakao 지도 시작하기</title>
        </head>
        <body>
        	<div id="map" style="width:1075px;height:600px;"></div>
        	<script type="text/javascript" src="https://dapi.kakao.com/v2/maps/sdk.js?appkey=fbfd65b295ce65b74143c51c496b2b94"></script>
        	<script>
            var mapContainer = document.getElementById('map'); // 지도를 표시할 div 

            var x_1 = {x_1}; // 위도 값을 변수로 선언
            var y_1 = {y_1}; // 경도 값을 변수로 선언
            var x_2 = {x_2}; // 위도 값을 변수로 선언
            var y_2 = {y_2}; // 경도 값을 변수로 선언
            var x_3 = {x_3}; // 위도 값을 변수로 선언
            var y_3 = {y_3}; // 경도 값을 변수로 선언
            var x_4 = {x_4}; // 위도 값을 변수로 선언
            var y_4 = {y_4}; // 경도 값을 변수로 선언
            var x_5 = {x_5}; // 위도 값을 변수로 선언
            var y_5 = {y_5}; // 경도 값을 변수로 선언
        

            var mapOption = {{ 
                center: new kakao.maps.LatLng(33.390701, 126.545667), // 변수로 받은 위도와 경도를 사용하여 지도의 중심 좌표 설정
                level: 9 // 지도의 확대 레벨
            }};

            var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

            // 마커를 표시할 위치와 title 객체 배열입니다 
            var positions = [
            {{
                title: '카카오', 
                latlng: new kakao.maps.LatLng({x_1}, {y_1})
            }},
            {{
                title: '생태연못', 
                latlng: new kakao.maps.LatLng({x_2}, {y_2})
            }},
            {{
                title: '텃밭', 
                latlng: new kakao.maps.LatLng({x_3}, {y_3})
            }},
            {{
                title: '근린공원',
                latlng: new kakao.maps.LatLng({x_4}, {y_4})
            }},
            {{
                title: '근린공원',
                latlng: new kakao.maps.LatLng({x_5}, {y_5})
            }}
        ];


            // 마커 이미지의 이미지 주소입니다
        var imageSrc = [
            "https://cdn-icons-png.flaticon.com/512/179/179349.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179350.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179351.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179352.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179357.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179358.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179359.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179360.png", 
            "https://cdn-icons-png.flaticon.com/512/179/179361.png" 
                ];       
        
        for (var i = 0; i < {num}; i ++) {{
        
        // 마커 이미지의 이미지 크기 입니다
        var imageSize = new kakao.maps.Size(35, 35); 
        
        // 마커 이미지를 생성합니다    
        var markerImage = new kakao.maps.MarkerImage(imageSrc[i], imageSize); 
        
        // 마커를 생성합니다
        var marker = new kakao.maps.Marker({{
            map: map, // 마커를 표시할 지도
            position: positions[i].latlng, // 마커를 표시할 위치
            title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
            image : markerImage // 마커 이미지 
            }});
            }}     

            // 지도에 컨트롤을 추가해야 지도위에 표시됩니다
            // kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
            map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

            // 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
            var zoomControl = new kakao.maps.ZoomControl();
            map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);
            </script>
        </body>
        </html>
        ''',
        height=1000,
        width=1600
    )

# Streamlit 애플리케이션 실행


x_1 = 33.400705
y_1 = 126.550677
x_2 = 33.470936
y_2 = 126.569477
x_3 = 33.420879
y_3 = 126.569940
x_4 = 33.451393
y_4 = 126.570738
x_5 = 0
y_5 = 0
Kakao_map(4, x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4, x_5, y_5)
