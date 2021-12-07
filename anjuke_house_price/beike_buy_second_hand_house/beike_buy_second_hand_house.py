import selenium.common.exceptions
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(5)

# Set the page load timeout to 5 seconds.
driver.set_page_load_timeout(5)

driver.get('https://www.ke.com/city/')

# region Get all the cities hrefs.
cities_elements = driver.find_elements_by_css_selector(
    'body > div.city_selection_section > div.city_recommend > div.city-item > div.city_list_section > ul > li > div.city_list .CLICKDATA > a')
cities_hrefs_list = []
for city_element in cities_elements:
    attribute = city_element.get_attribute('href')
    print(attribute)
    cities_hrefs_list.append(attribute)

hrefs_without_fang_list = []
for href in cities_hrefs_list:
    if '.fang.' not in href:
        hrefs_without_fang_list.append(href)

print(hrefs_without_fang_list)
print(len(hrefs_without_fang_list))
# endregion

buy_second_hand_hrefs_list = []
for href in hrefs_without_fang_list:
    href += 'ershoufang/co21ba70ea10000/'
    buy_second_hand_hrefs_list.append(href)

with open('beike_buy_second_hand_house.csv', 'w', encoding='gbk') as file:
    file.write(
        'City Name,Lowest Price,Average Price,Highest Price,Number of Samples,Price Unit(s),Total number of Houses\n')

for href in buy_second_hand_hrefs_list:
    with open('beike_buy_second_hand_house.csv', 'a', encoding='gbk') as file:
        try:
            driver.get('about:blank')
            try:
                driver.get(href)
            except selenium.common.exceptions.TimeoutException as e:
                print(f'Small Error: {e}... Continue...')

            city_name = driver.find_element_by_css_selector('.total > a:nth-child(2)').text[:-3]

            price_list = []
            price_elements_list = driver.find_elements_by_css_selector(
                'div.totalPrice span')
            for element in price_elements_list:
                price = float(element.text)
                price_list.append(price)

            lowest_price = price_list[0]
            number_of_samples = len(price_list)
            average_price = sum(price_list) / number_of_samples
            highest_price = max(price_list)

            price_unit_set = set()
            price_unit_elements_list = driver.find_elements_by_css_selector(
                'div.totalPrice')
            for element in price_unit_elements_list:
                price_unit = element.text[-1]
                price_unit_set.add(price_unit)
            price_units = f'{price_unit_set}'[1:][:-1]

            total_number_of_houses = driver.find_element_by_css_selector('.total > span:nth-child(1)').text

            file.write(
                f'{city_name},{lowest_price},{average_price},{highest_price},{number_of_samples},{price_units},{total_number_of_houses}\n')
        except Exception as e:
            print(f'Error: {e}')
            file.write(
                f'{href},Error,Error,Error,Error,Error,Error\n')

if __name__ == '__main__':
    print(cities_hrefs_list)
    print(hrefs_without_fang_list)
