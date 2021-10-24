
# from nationality import nationality_func
from age import age_func
import nationality




# Ask the user to enter their first name and store in variable
first_name = input("\n\nPlease enter your first name: \n\n")

# Run nationality function imported from nationality.py module
# At the same time, set a new var, name2 from the reurned value
valid_name = nationality.nation.nationality_func(first_name)

# Run age function imported from age.py module
age_func(valid_name)

