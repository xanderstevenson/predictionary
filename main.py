import requests


# Ask the user to enter their first name and store in variable
first_name = input("\n\nPlease enter your first name: \n\n")

# Make request to Nationalize API
r = requests.get("https://api.nationalize.io?name=" + first_name)

# Turn results into JSON dictionary
nation_results = r.json()

# print results using f-Strings
print(f"\n\nHere are your results, {first_name}:\n")
print('--------------------------------------\n')
print('NATIONALITY\n\n')


for key, item in nation_results.items():
    if key == 'country':
        country_1 = list(item[0].values())
        country_2 = list(item[1].values())
        country_3 = list(item[2].values())

print(f"Country 1 : {country_1[0]}\nProbabilty: {'{:.2%}'.format(country_1[1])}\n")
print(f"Country 2 : {country_2[0]}\nProbabilty: {'{:.2%}'.format(country_2[1])}\n")
print(f"Country 3 : {country_3[0]}\nProbabilty: {'{:.2%}'.format(country_3[1])}\n")

# print(nation_results)



# Print nationality based on first name
# print("Your Nationality is " + r)
