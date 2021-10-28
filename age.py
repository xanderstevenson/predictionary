#####################
#     AGIFY.IO      #
#####################

import requests



class Age_Class:
    
    def age_func(valid_name):
        a = requests.get("https://api.agify.io?name=" + valid_name)
        age_results = a.json()
        age = age_results['age']
        # print('-------------------------------------------------------')
        # print(f'Based on your name, your age is predicted to be: {age}')
        # print('-------------------------------------------------------')
        return age


