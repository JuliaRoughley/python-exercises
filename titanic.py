import itertools
from load_data import load_data

all_data = load_data()


def show_countries(ships_data):
    """Gets all the country names of the ships, removes
  the duplicates, orders them alphabetically and returns
  list to the user"""
    country_names = []
    for ship_info in ships_data['data']:
        country_names.append(ship_info['COUNTRY'])
    no_duplicate_country_names = sorted(list(set(country_names)))
    return no_duplicate_country_names


def welcome_cli():
    """When program is started, this function runs to inform the user
  of available options and actions"""
    print("Welcome to the Ships CLI! Enter 'help' to view available commands.")
    user_inputs_choice()


def user_inputs_choice():
    """allows user to input a command, to be used at the end of other
  functions to keep the program running until user exits"""
    user_choice = input()
    user_parameters = user_choice.split(' ')
    function_dictionary = {"help": (help_command, 0),
                           "show_countries": (show_countries, 1),
                           "top_countries": (top_countries_with_most_ships, 2)
                           }

    chosen_function = user_parameters[0]
    command = function_dictionary[chosen_function]
    use_all_data = command[1]
    if (use_all_data):
        params = [all_data]
    else:
        params = []

    result = command[0](*params)
    print(result)
    user_inputs_choice()


def help_command():
    """When user inputs 'help', prints a list of available commands
  to the terminal"""
    print("\nhelp\nshow_countries\ntop_countries <num_countries>\n")


def top_countries_with_most_ships(ships_data, num_countries):
    """Prints a list of the top countries with the most ships.
  Gets these from all_data parameter and user input of
  num_countries"""
    countries_num_ships = {}
    for ship in ships_data['data']:
        if ship['COUNTRY'] in countries_num_ships:
            countries_num_ships[ship['COUNTRY']] += 1
        else:
            countries_num_ships[ship['COUNTRY']] = 1
    sorted_countries_ships = sorted(countries_num_ships.items(), key=lambda x: x[1], reverse=True)
    dict_sorted_countries = dict(sorted_countries_ships)
    list_countries_ship_number = itertools.islice(dict_sorted_countries.items(), num_countries)
    for country in list_countries_ship_number:
        print(f"{country[0]}: {country[1]}")


def main():
    """Welcomes user, gives instructions, and calls functions to return
  info."""
    welcome_cli()


if __name__ == "__main__":
    main()
