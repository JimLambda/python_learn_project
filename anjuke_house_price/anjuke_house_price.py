from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(3)

# Set the page load timeout to 3 seconds.
driver.set_page_load_timeout(3)

# # Add chrome options to fix the selenium TimeoutException. Source: https://stackoverflow.com/q/48450594
# options = webdriver.ChromeOptions()
# options.add_argument('enable-automation')
# options.add_argument('--headless')
# options.add_argument('--window-size=1920,1080')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-infobars')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--disable-browser-side-navigation')
# options.add_argument('--disable-gpu')

driver.get('https://www.anjuke.com/sy-city.html')

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

with open(file='city_house_price_info.csv', mode='w', encoding='gbk') as file:
    file.write('City Name,Average Money\n')

city_name_index = 0
for href in cities_hrefs_list:
    driver.get('about:blank')
    city_name = cities_names_list[city_name_index]
    city_name_index += 1
    try:
        driver.get(href)

        average_price_element = driver.find_element_by_css_selector('.m-t-f-pricetrend span')
        average_price = int(average_price_element.text)

        with open(file='city_house_price_info.csv', mode='a', encoding='gbk') as file:
            file.write('{},{}\n'.format(city_name, average_price))

    except Exception as error_info:
        print(error_info)
        with open(file='city_house_price_info.csv', mode='a', encoding='gbk') as file:
            file.write('{},{}\n'.format(city_name, 'None'))
        continue
