import json

file_load = json.load(open('/Users/vineetsharma/Downloads/data.json'))
ask_user = input("Please enter a word ")
if ask_user.title() in file_load:
    print("".join(file_load[ask_user.title()]))
elif ask_user.upper() in file_load:
    print("".join(file_load[ask_user.upper()]))
elif ask_user.lower() in file_load:
    print("".join(file_load[ask_user.lower()]))
else:
    print("Please enter a valid word")
