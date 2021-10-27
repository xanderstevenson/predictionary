#########################
#      GENDERIZE.IO     #
#########################

import requests

class Gender:

    def gender_func(valid_name):
        # make reequest, convert to JSON, extract, then format data
        g = requests.get("https://api.genderize.io?name=" + valid_name)
        gender_results = g.json()
        gender = gender_results['gender']
        gender_prob = gender_results['probability']
        gender_prob = '{:.0%}'.format(gender_prob)
        # print predicted gender and probability
        print(f'Your predicted gender is {gender}.\n')
        print(f'The probability is {gender_prob}')
        return gender, gender_prob
