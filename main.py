######################
#     MAIN CLASS     #
######################


# import adjacent modules
import age
import nationality
import gender
import ip

class Main:

    # Ask the user to enter their first name and store in variable
    first_name = input("\n\nPlease enter your first name: \n\n")

    # Run nationality function imported from nationality.py module
    # At the same time, set a new var, name2 from the reurned value
    valid_name = nationality.Nation.nationality_func(first_name)

    # Run age function imported from age.py module
    age.Age_Class.age_func(valid_name)

    # Run gender function imported from gender.py
    gender.Gender.gender_func(valid_name)

    # Run ip function imported from ip.py
    ip.Ip.ip_func()
