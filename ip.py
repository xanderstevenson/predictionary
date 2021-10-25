#############################
#    IP FAST - Public API   #
#############################

import requests

class Ip:
    def ip_func():

        i = requests.get('https://ip-fast.com/api/ip/?format=json&location=True')
        ip_results = i.json()
        ip_add = ip_results['ip']
        city = ip_results['city']
        country = ip_results['country']


        print('------------------------------------------')
        print(f'Your IP Address: {ip_add}')
        print(f'Your location is {city}, {country}')
