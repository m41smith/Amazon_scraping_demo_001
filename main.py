import requests


HEADER_FOR_GET_REQUEST = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
     'Accept-Language': 'en-US, en;q=0.5'}
)

def get_single_listiing():
    data_out_file = open('data_output.txt', 'r')

    target_url = 'https://www.amazon.com/dp/B01N1081RO/'
    web_response = requests.get(target_url, headers=HEADER_FOR_GET_REQUEST)

    print(web_response.text)

    data_out_file.close()


if __name__ == '__main__':
    get_single_listiing()
