#############################
#     positionstack API     #
#############################

import requests

class GeoClass:
    def geo_func():

        # first api call

        ps_key = 'db72fb4a1511237d4994374ad4d945e4'
        locale = 'Chicago'

        i = requests.get(f'http://api.positionstack.com/v1/forward?access_key={ps_key}&query={locale}&limit=10&output=json')
        # ip_results = i.json()

        print(i)

        # ip_add = ip_results['ip']
        # city = ip_results['city']
        # country = ip_results['country']

        # # second api call using results from above

        # i2 = requests.get(f'https://ipinfo.io/{ip_add}/geo')
        # i2_results = i2.json()

        # state = i2_results['region']
        # coord = i2_results['loc']
        # timezone = ['timezone']
        # org = i2_results['org']
        # postal = i2_results['postal']

        # # print('------------------------------------------')
        # # print(f'Your IP Address: {ip_add}')
        # # print(f'Your location is {city}, {country}')
        # return ip_add, city, country, state, coord, timezone, org, postal
runit = GeoClass
runit.geo_func()