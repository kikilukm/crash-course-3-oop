import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Succes! Response {response.status_code}')
        #print(f'content{response.text}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Hasil pemanggilan URL {url}')
        print(f'Title= {soup.title.string.integrar}')
    else:
        print(f'Woops! there an error occured {response.status_code}')
except Exception as e:
        print(f'There has an Error {e}')
print('Program Ended')