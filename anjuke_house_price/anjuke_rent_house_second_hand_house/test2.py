a_string = "A string is more than its parts!"
matches = ["morey", "wholesome", "milk", 'parts!']

if any(x in a_string for x in matches):
    print('found!')