import requests

# Ask the user to enter their first name and store in variable
first_name = input("Please enter your first name.")

# Make request to Nationalize API
r = requests.get("https://api.nationalize.io?name=" + first_name)

# Turn results into JSON dictionary
nation_results = r.json()

print(nation_results)



# Print nationality based on first name
# print("Your Nationality is " + r)
