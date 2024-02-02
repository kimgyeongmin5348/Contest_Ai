import requests
from bs4 import BeautifulSoup


def search_on_google(query):
    base_url = "https://www.google.com/search"
    params = {"q": query}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('a', href=True)

        for result in search_results:
            print(result['href'])
    else:
        print("검색에 실패했습니다.")


# 사용자로부터 입력 받기
search_query = input("검색어를 입력하세요: ")

# 검색 수행
search_on_google(search_query)