from selenium import webdriver
import requests

driver = webdriver.Firefox()
driver.implicitly_wait(3)

# Set the page load timeout to 3 seconds.
driver.set_page_load_timeout(3)

driver.get('https://www.ke.com/city/')

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

zu_href_list = []
for href in hrefs_without_fang_list:
    splitted_href_list = href.split('.')
    splitted_href_list[0] = splitted_href_list[0] + '.zu'
    new_href = '.'.join(splitted_href_list)
    zu_href_list.append(new_href)

rent_threshold = 500

city_rent_info_list = []

with open(file='city_house_renting_info.csv', mode='w') as file:
    file.write('Number of House,City Name,Average Money\n')

for href in zu_href_list:
    href = href + 'zufang/rt200600000001l1l2l3erp' + str(rent_threshold)
    driver.get('about:blank')
    try:
        driver.get(href)
        number_of_house_element = driver.find_element_by_css_selector('span.content__title--hl')
        house_number = int(number_of_house_element.text)
        print(house_number)
        city_name_element = driver.find_element_by_css_selector('#content > div.content__article > p > a')
        city_name = city_name_element.text[:-2]
        print(city_name)

        if house_number > 0:
            rent_money_list = []
            rent_money_element_list = driver.find_elements_by_css_selector(
                '#content>div.content__article>div:nth-child(3) em')
            for rent_money_element in rent_money_element_list:
                rent_money = int(rent_money_element.text)
                rent_money_list.append(rent_money)
            average_money = sum(rent_money_list) / len(rent_money_list)
        else:
            average_money = 0
        print(average_money)

        city_rent_info_list.append('{},{},{}'.format(house_number, city_name, average_money))

        with open(file='city_house_renting_info.csv', mode='a') as file:
            file.write('{},{},{}\n'.format(house_number, city_name, average_money))

    except Exception as error_info:
        print(error_info)
        continue
