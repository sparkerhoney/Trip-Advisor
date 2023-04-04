from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 크롬 드라이버 경로 설정
driver_path = "C:/chromedriver/chromedriver.exe"  # 본인의 크롬 드라이버 경로로 설정해주세요

# 네이버 여행 페이지로 이동
driver = webdriver.Chrome(driver_path)
driver.get("https://www.naver.com")
time.sleep(2) # 2초 대기

# 검색어 입력
search_box = driver.find_element_by_name("query")
search_box.send_keys("네이버 여행")
search_box.send_keys(Keys.RETURN) # Enter 키 입력
time.sleep(2)

# 여행 관광지 검색
search_box = driver.find_element_by_name("query")
search_box.send_keys("여행 관광지")
search_box.send_keys(Keys.RETURN) # Enter 키 입력
time.sleep(2)
lo
# 더보기 버튼 클릭
more_btn = driver.find_element_by_css_selector(".more > .btn_more")
more_btn.click()
time.sleep(2)

# 검색 결과 크롤링
contents = driver.find_elements_by_css_selector(".list_area .tit")

for content in contents:
    print(content.text)

# 브라우저 종료
driver.quit()
