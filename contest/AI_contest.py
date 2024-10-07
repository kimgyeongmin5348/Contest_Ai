import requests
from bs4 import BeautifulSoup


def search_on_google(query):
    base_url = "https://www.google.com/search"
    params = {"q": query}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')   # 여기를 수정해야하는데...

        results = []
        for result in search_results:
            results.append(result.get_text())

        return results
    else:
        print("Google 검색에 실패했습니다.")
        return []


# def search_on_naver(query):
#     base_url = "https://search.naver.com/search.naver"
#     params = {"query": query}
#
#     response = requests.get(base_url, params=params)
#
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         search_results = soup.find_all('div', class_='total_wrap')
#
#         results = []
#         for result in search_results:
#             results.append(result.get_text())
#
#         return results
#     else:
#         print("Naver 검색에 실패했습니다.")
#         return []


# 사용자로부터 입력 받기
search_query = input("검색어를 입력하세요: ")

# 구글에서 검색 수행
google_results = search_on_google(search_query)

# 네이버에서 검색 수행
# naver_results = search_on_naver(search_query)

# 구글과 네이버 검색 결과 합치기
# combined_results = google_results + naver_results

# 합쳐진 결과 출력
# for result in combined_results:
print(google_results)