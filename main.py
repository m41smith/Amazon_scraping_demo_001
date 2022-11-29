import requests
from bs4 import BeautifulSoup


HEADER_FOR_GET_REQUEST = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
     'Accept-Language': 'en-US, en;q=0.5'}
)

def get_single_listiing():
    data_out_file = open('data_output.txt', 'w')

    target_url = 'https://www.amazon.com/dp/B01N1081RO/'
    web_response = requests.get(target_url, headers=HEADER_FOR_GET_REQUEST)
    # print(web_response.text)

    b_soup_format = BeautifulSoup(web_response.content, 'html.parser')
    # print(b_soup_format)

    try:
        product_title_bs_element = b_soup_format.find('span', attrs={'id': 'productTitle'})
        print(product_title_bs_element)
        print(type(product_title_bs_element))
        print()
        product_title_bs_element_str = product_title_bs_element.string
        print(product_title_bs_element_str)
        print(type(product_title_bs_element_str))
        print()
        product_name_str = product_title_bs_element_str.strip()
        print(product_name_str)
        print(type(product_name_str))
    except AttributeError:
        product_name_str = 'NA'
        print('product title = ', product_name_str)

    data_out_file.write(product_name_str)



    data_out_file.close()


if __name__ == '__main__':
    get_single_listiing()
