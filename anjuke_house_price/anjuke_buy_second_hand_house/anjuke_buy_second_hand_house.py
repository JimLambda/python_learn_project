from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)

# Set the page load timeout to 3 seconds.
driver.set_page_load_timeout(10)

driver.get('https://www.anjuke.com/sy-city.html')

# region Get all the cities hrefs.
cities_elements = driver.find_elements_by_css_selector(
    'body > div.content > div > div.letter_city > ul > li > div > a')
cities_hrefs_list = []
cities_names_list = []
for city_element in cities_elements:
    attribute = city_element.get_attribute('href')
    content = city_element.text
    print(attribute)
    cities_hrefs_list.append(attribute)
    cities_names_list.append(content)
# endregion

buy_second_hand_hrefs_list = []
for href in cities_hrefs_list:
    href += 'sale/o4/?from=sugg&areas=70_2147483647'
    buy_second_hand_hrefs_list.append(href)

with open('anjuke_buy_second_hand_house.csv', 'w', encoding='gbk') as file:
    file.write('City Name,Lowest Price,Average Price,Highest Price,Number of Samples,Price Unit(s),挂牌均价\n')

for href in buy_second_hand_hrefs_list:
    with open('anjuke_buy_second_hand_house.csv', 'a', encoding='gbk') as file:
        try:
            driver.get('about:blank')
            driver.get(href)

            city_name = driver.find_element_by_css_selector('.city-name').text

            price_list = []
            price_elements_list = driver.find_elements_by_css_selector(
                'html body div#__nuxt div#__layout div.list section.list-body section.list-main section.list-left section.list div.property span.property-price-total-num')
            for element in price_elements_list:
                price = float(element.text)
                price_list.append(price)

            lowest_price = price_list[0]
            number_of_samples = len(price_list)
            average_price = sum(price_list) / number_of_samples
            highest_price = max(price_list)

            price_unit_set = set()
            price_unit_elements_list = driver.find_elements_by_css_selector(
                'html body div#__nuxt div#__layout div.list section.list-body section.list-main section.list-left section.list div.property span.property-price-total-text')
            for element in price_unit_elements_list:
                price_unit = element.text
                price_unit_set.add(price_unit)
            price_units = f'{price_unit_set}'[1:][:-1]

            gua_pai_average_price = driver.find_element_by_css_selector('.price-trend-money > em:nth-child(1)').text

            file.write(
                f'{city_name},{lowest_price},{average_price},{highest_price},{number_of_samples},{price_units},{gua_pai_average_price}\n')
        except Exception as e:
            print(f'Error: {e}')
            file.write(
                f'{href},Error,Error,Error,Error,Error,Error\n')

if __name__ == '__main__':
    print(cities_hrefs_list)
    print(cities_names_list)
