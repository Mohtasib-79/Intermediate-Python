# {
#     "name": "Urvashi",
#     "age": 24,
#     "skills": ["Python", "C++"],
#     "teacher": true,
#     Null
# }


# person = {
#     "name": "Urvashi",
#     "age": 24,
#     "skills": ["Python", "C++"],
#     "teacher": True,
#     "extra": None
# }


import requests

# url = "https://disease.sh/v3/covid-19/all"
# response = requests.get(url)
# data = response.json()
# print(data['active'])

from pprint import pprint
url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
response = requests.get(url)
data = response.json()
# print(response.status_code)
# print(response.url)
# print(response.content) # html format-> binary
# print(response.text)


#
# cases = data['cases']
# sorted_cases = dict(sorted(cases.items()))
#
# for key, value in sorted_cases.items():
#     if value > 20_000:
#         print(key, value)
#         break


# api to look into: https://openlibrary.org/search.json?q=the+lord+of+the+rings

