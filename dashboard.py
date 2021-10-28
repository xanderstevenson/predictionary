######################
#     MAIN CLASS     #
######################


# import adjacent modules
import age
import nationality
import gender
import ip


class Dash:

    # Ask the user to enter their first name and store in variable
    first_name = input("\n\nPlease enter your first name: \n\n")

    # Run nationality function imported from nationality.py module
    # At the same time, set a new var, name2 from the reurned value
    valid_name, country_1, country_2, country_3, code_1, code_2, code_3 = nationality.Nation.nationality_func(first_name)

    # Run age function imported from age.py module
    age = age.Age_Class.age_func(valid_name)

    # Run gender function imported from gender.py
    gender, gender_prob = gender.Gender.gender_func(valid_name)

    # Run ip function imported from ip.py
    ip.Ip.ip_func()
        

  