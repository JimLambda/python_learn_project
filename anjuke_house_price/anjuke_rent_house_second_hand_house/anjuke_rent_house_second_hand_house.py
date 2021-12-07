from datetime import datetime

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(5)

# Set the page load timeout to 5 seconds.
driver.set_page_load_timeout(5)

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


city_info_list = []

# File name.
file_name = 'anjuke_data_' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + '.csv'
with open(file=file_name, mode='w') as file:
    file.write(
        'Name,URL,官方均价(元/㎡),min租金(元/月),max租金(元/月),avg租金(元/月),房子数/租金样本数量,租房最小面积(㎡),租房最大面积(㎡)'
        ',租房平均面积(㎡),二手房样本数量,min二手房价(万元),max二手房价(万元),avg二手房价(万元),min二手房均价(元/㎡),'
        'max二手房均价(元/㎡),avg二手房均价(元/㎡)\n')

for index, href in enumerate(cities_hrefs_list):
    try:
        current_city_info_dict = {}

        current_city_info_dict.setdefault('name', cities_names_list[index])
        current_city_info_dict.setdefault('url', href)
        current_city_info_dict['official_average_money'] = 'INIT'
        current_city_info_dict['current_city_rent_money_min'] = 'INIT'
        current_city_info_dict['current_city_rent_money_max'] = 'INIT'
        current_city_info_dict['current_city_rent_money_avg'] = 'INIT'
        current_city_info_dict['rent_money_sample_size'] = 'INIT'
        current_city_info_dict['min_house_area'] = 'INIT'
        current_city_info_dict['max_house_area'] = 'INIT'
        current_city_info_dict['avg_house_area'] = 'INIT'
        current_city_info_dict['second_hand_house_sample_size'] = 'INIT'
        current_city_info_dict['second_hand_house_min_price'] = 'INIT'
        current_city_info_dict['second_hand_house_max_price'] = 'INIT'
        current_city_info_dict['second_hand_house_avg_price'] = 'INIT'
        current_city_info_dict['second_hand_house_min_single_price'] = 'INIT'
        current_city_info_dict['second_hand_house_max_single_price'] = 'INIT'
        current_city_info_dict['second_hand_house_avg_single_price'] = 'INIT'

        # region Official average money crawler.
        try:
            driver.get(href)
            official_average_money_element = driver.find_element_by_css_selector('.m-t-f-pricetrend>dd>span')
            official_average_money = int(official_average_money_element.text)
        except Exception as e:
            if any(x in driver.current_url for x in ['verify', 'captcha']):
                input('Please verify the captcha first, then press <ENTER> key to continue.')
            print('Error:', e, 'Unable to locate official_average_money.', 'Errored city:', cities_names_list[index],
                  'Errored URL:', href)
            official_average_money = -1

        current_city_info_dict['official_average_money'] = official_average_money
        # endregion

        try:
            # region Rent house info crawler.
            driver.find_element_by_css_selector('.m-t-box>.box>.left-tabs span[data-type="3"]').click()
            driver.find_element_by_css_selector('#btnSubmit[value="租房"]').click()

            current_url = driver.current_url
            splitted_list = current_url.split('/')
            first_3_elements = splitted_list[:3]
            joined_str = '/'.join(first_3_elements)
            href_with_conditions = joined_str + '/fangyuan/fx2-px1-x1-lx1-v1'

            driver.get(href_with_conditions)

            rent_money_elements_list = driver.find_elements_by_css_selector(
                '#list-content .zu-itemmod strong>b.strongbox')
            rent_money_list = []
            for rent_money_element in rent_money_elements_list:
                rent_money = int(rent_money_element.text)
                rent_money_list.append(rent_money)
            current_city_rent_money_min = min(rent_money_list)
            current_city_rent_money_max = max(rent_money_list)
            current_city_rent_money_avg = sum(rent_money_list) / len(rent_money_list)
            rent_money_sample_size = len(rent_money_list)
            current_city_info_dict['current_city_rent_money_min'] = current_city_rent_money_min
            current_city_info_dict['current_city_rent_money_max'] = current_city_rent_money_max
            current_city_info_dict['current_city_rent_money_avg'] = current_city_rent_money_avg
            current_city_info_dict['rent_money_sample_size'] = rent_money_sample_size

            house_area_list = []
            house_area_elements_list = driver.find_elements_by_css_selector('.details-item>b.strongbox:nth-child(4)')
            for house_area_element in house_area_elements_list:
                house_area = float(house_area_element.text)
                house_area_list.append(house_area)
            min_house_area = min(house_area_list)
            max_house_area = max(house_area_list)
            avg_house_area = sum(house_area_list) / len(house_area_list)
            current_city_info_dict['min_house_area'] = min_house_area
            current_city_info_dict['max_house_area'] = max_house_area
            current_city_info_dict['avg_house_area'] = avg_house_area
            # endregion
        except Exception as e:
            if any(x in driver.current_url for x in ['verify', 'captcha']):
                input('Please verify the captcha first, then press <ENTER> key to continue.')
            print('Error:', e, 'Errored city:', cities_names_list[index], 'Errored URL:', href)

        try:
            # region Second hand house price crawler.
            second_hand_href = href + 'sale/o4/?from=sugg&areas=70_2147483647'
            driver.get(second_hand_href)

            second_hand_house_price_list = []
            second_hand_house_price_elements_list = driver.find_elements_by_css_selector('.property-price-total-num')
            for second_hand_house_price_element in second_hand_house_price_elements_list:
                second_hand_house_price = float(second_hand_house_price_element.text)
                second_hand_house_price_list.append(second_hand_house_price)

            second_hand_house_single_price_list = []
            second_hand_house_single_price_elements_list = driver.find_elements_by_css_selector(
                '.property-price-average')
            for second_hand_house_single_price_element in second_hand_house_single_price_elements_list:
                second_hand_house_single_price = int(second_hand_house_single_price_element.text.split('元')[0])
                second_hand_house_single_price_list.append(second_hand_house_single_price)

            second_hand_house_sample_size = len(second_hand_house_price_list)
            second_hand_house_min_price = min(second_hand_house_price_list)
            second_hand_house_max_price = max(second_hand_house_price_list)
            second_hand_house_avg_price = sum(second_hand_house_price_list) / len(second_hand_house_price_list)
            second_hand_house_min_single_price = min(second_hand_house_single_price_list)
            second_hand_house_max_single_price = max(second_hand_house_single_price_list)
            second_hand_house_avg_single_price = sum(second_hand_house_single_price_list) / len(
                second_hand_house_single_price_list)

            current_city_info_dict['second_hand_house_sample_size'] = second_hand_house_sample_size
            current_city_info_dict['second_hand_house_min_price'] = second_hand_house_min_price
            current_city_info_dict['second_hand_house_max_price'] = second_hand_house_max_price
            current_city_info_dict['second_hand_house_avg_price'] = second_hand_house_avg_price
            current_city_info_dict['second_hand_house_min_single_price'] = second_hand_house_min_single_price
            current_city_info_dict['second_hand_house_max_single_price'] = second_hand_house_max_single_price
            current_city_info_dict['second_hand_house_avg_single_price'] = second_hand_house_avg_single_price
            # endregion
        except Exception as e:
            if any(x in driver.current_url for x in ['verify', 'captcha']):
                input('Please verify the captcha first, then press <ENTER> key to continue.')
            print('Error:', e, 'Errored city:', cities_names_list[index], 'Errored URL:', href)

        print(current_city_info_dict)
        city_info_list.append(current_city_info_dict)

        with open(file=file_name, mode='a') as file:
            file.write(current_city_info_dict['name'] + ',' +
                       current_city_info_dict['url'] + ',' +
                       str(current_city_info_dict['official_average_money']) + ',' +
                       str(current_city_info_dict['current_city_rent_money_min']) + ',' +
                       str(current_city_info_dict['current_city_rent_money_max']) + ',' +
                       str(current_city_info_dict['current_city_rent_money_avg']) + ',' +
                       str(current_city_info_dict['rent_money_sample_size']) + ',' +
                       str(current_city_info_dict['min_house_area']) + ',' +
                       str(current_city_info_dict['max_house_area']) + ',' +
                       str(current_city_info_dict['avg_house_area']) + ',' +
                       str(current_city_info_dict['second_hand_house_sample_size']) + ',' +
                       str(current_city_info_dict['second_hand_house_min_price']) + ',' +
                       str(current_city_info_dict['second_hand_house_max_price']) + ',' +
                       str(current_city_info_dict['second_hand_house_avg_price']) + ',' +
                       str(current_city_info_dict['second_hand_house_min_single_price']) + ',' +
                       str(current_city_info_dict['second_hand_house_max_single_price']) + ',' +
                       str(current_city_info_dict['second_hand_house_avg_single_price']) + '\n')

    except Exception as e:
        if any(x in driver.current_url for x in ['verify', 'captcha']):
            input('Please verify the captcha first, then press <ENTER> key to continue.')
        print('Error:', e, 'Errored city:', cities_names_list[index], 'Errored URL:', href)

if __name__ == '__main__':
    print(city_info_list)
    print(cities_hrefs_list)
    print(cities_names_list)
