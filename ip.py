#############################
#    IP FAST - Public API   #
#############################

import requests

class Ip:
    def ip_func():

        # first api call

        i = requests.get('https://ip-fast.com/api/ip/?format=json&location=True')
        ip_results = i.json()
        ip_add = ip_results['ip']
        city = ip_results['city']
        country = ip_results['country']

        # second api call using results from above

        i2 = requests.get(f'https://ipinfo.io/{ip_add}/geo')
        i2_results = i2.json()

        state = i2_results['region']
        coord = i2_results['loc']
        timezone = ['timezone']
        org = i2_results['org']
        postal = i2_results['postal']

        # print('------------------------------------------')
        # print(f'Your IP Address: {ip_add}')
        # print(f'Your location is {city}, {country}')
        return ip_add, city, country, state, coord, timezone, org, postal
