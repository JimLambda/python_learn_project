str1 = 'http://hz.zu.com/345'

splitted_list = str1.split('/')
print(splitted_list)
first_3_elements = splitted_list[:3]
print(first_3_elements)
joined_str = '/'.join(first_3_elements)
print(joined_str)