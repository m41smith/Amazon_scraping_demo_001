import requests
from bs4 import BeautifulSoup

HEADER_FOR_GET_REQUEST = (
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
     'Accept-Language': 'en-US, en;q=0.5'}
)


def get_single_listing_title():
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


def get_multiple_listings_by_keyword(keywords: str):
    # wool sweater
    # wool+sweater
    base_url = 'https://www.amazon.com/s?k='
    search_keywords_formatted = keywords.replace(' ', '+')
    page_parameter = '&page=1'
    search_url = f'{base_url}{search_keywords_formatted}{page_parameter}'
    print(search_url)

    response_object = requests.get(search_url, headers=HEADER_FOR_GET_REQUEST)
    # print(response_object.content)

    soup_format = BeautifulSoup(response_object.content, 'html.parser')

    # print(soup_format)
    # print()
    # print(type(soup_format))

    # get the first search result
    search_result = soup_format.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})
    print(type(search_result))
    # print(search_result[0])

    # ct = 0
    # for item in search_result:
    #     print(item)
    #     print()
    #     ct += 1
    # print(ct)

    first_search_result_item = search_result[0]

    first_product_title = first_search_result_item.h2.text
    print(first_product_title)
    first_product_rating = first_search_result_item.i.text
    print(first_product_rating)


if __name__ == '__main__':
    # get_single_listing_title()
    get_multiple_listings_by_keyword('wool sweaters')
