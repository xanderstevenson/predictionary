##########################
#     NATIONALIZE.IO     #
##########################

import requests
import country_converter as coco


class Nation:

    def nationality_func(first_name):



        # Make request to Nationalize API
        r = requests.get("https://api.nationalize.io?name=" + first_name)

        # Turn results into JSON dictionary
        nation_results = r.json()

        while len(nation_results['country']) < 3:
            print(f"\n{first_name} is not recognized as a common name.\n")
            new_name = input("\n\nPlease enter your first name: \n\n")
            first_name = new_name
            r = requests.get("https://api.nationalize.io?name=" + first_name)

        # Turn results into JSON dictionary
            nation_results = r.json()


        # print results using f-Strings
        print(f"\n\nHere are your results, {first_name}:\n")
        print('----------------------------------------------------------------------\n')
        print(f'NATIONALITIES WITH GREATEST PERCENTAGES OF THE NAME {first_name}\n')
        print('----------------------------------------------------------------------\n')


        ##### REMEMBER to Validate and handle error of no matches

        # iterate through dictionary and convert results to list
        for key, item in nation_results.items():
            if key == 'country':
                country_1 = list(item[0].values())
                country_2 = list(item[1].values())
                country_3 = list(item[2].values())

        code_1 = country_1[0]
        code_2 = country_2[0]
        code_3 = country_3[0]

        # use country_converter package to convert country codes to full country names
        country_1[0] = coco.convert(names=country_1[0], to='name_short')
        country_2[0] = coco.convert(names=country_2[0], to='name_short')
        country_3[0] = coco.convert(names=country_3[0], to='name_short')

        # print county names and probabilities
        print(f"Country 1 : {country_1[0]}\nPercentage: {'{:.2%}'.format(country_1[1])}\n")
        print(f"Country 2 : {country_2[0]}\nPercentage: {'{:.2%}'.format(country_2[1])}\n")
        print(f"Country 3 : {country_3[0]}\nPercentage: {'{:.2%}'.format(country_3[1])}\n")
    
        valid_name = first_name

        country_1 = country_1[0]
        country_2 = country_2[0]
        country_3 = country_3[0]


        return valid_name, country_1, country_2, country_3, code_1, code_2, code_3

