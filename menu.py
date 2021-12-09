# James Shaw
# menu.py
# 11/15/21

def get_list_from_user():
    # Using IDE helper values within function headers
    # Hovering over a function call with your mouse, as long as the function has helper values in the header,
    # will display the header and helper values within certain more advanced IDEs, like so:
    # Gathers a list of user provided integers
    # Returns: List of provided integers
    """
    Gathers a list of user provided integers
    
    :return: List of provided integers
    """
    new_list = []
    user_input = input("Enter integer (q to quit): ")
    while user_input != 'q':
        new_list.append(int(user_input))
        user_input = input("Enter integer (q to quit): ")
    return new_list


def print_menu():
    """
    Prints the menu and choices

    :return: String - A string the user inputs through the console choosing one of the options within the menu
    """
    print("""MENU
    n - Number of integers in list
    p - Print the list
    u - Unique integers
    o - Odd integers
    e - Even integers
    a - Add integer to list
    q - Quit\n""")
    return input("Choose an option: ")


def num_in_list(input_list):
    """
    :param input_list: List of integers
    :return: Int - Length of input_list
    """
    return len(input_list)


def print_list(iterable):
    """
    Prints a string of given objects in set or list, separated by a space
    
    :param iterable: Set or list
    """
    # The map function applies a function to every object within an iterable container.  In this case I am
    # using the map function to convert every object within the iterable container into strings, then putting
    # them back into a list for use with the string.join() method.
    iterable = list(map(str, iterable))
    print(" ".join(iterable))


def unique_integers(input_list):
    """
    :param input_list: List of integers
    :return: Set - Sorted set of unique integers within the list
    """
    return sorted(set(input_list))


def odd_integers(input_list):
    """
    :param input_list: List of integers
    :return: List - Odd integers from input_list
    """
    return [integer for integer in input_list if integer % 2 != 0]


def even_integers(input_list):
    """
    :param input_list: List of integers
    :return: List - Even integers from input_list
    """
    return [integer for integer in input_list if integer % 2 == 0]


def add_integer(input_list):
    """
    Appends a new integer to the input_list
    
    :param input_list: List of integers
    """
    new_int = int(input("Please enter an integer to add to the list: "))
    input_list.append(new_int)


my_list = get_list_from_user()
menu_choice = print_menu()

while menu_choice != 'q':
    if menu_choice == 'n':
        print(num_in_list(my_list))
    elif menu_choice == 'p':
        print_list(my_list)
    elif menu_choice == 'u':
        print_list(unique_integers(my_list))
    elif menu_choice == 'o':
        print_list(odd_integers(my_list))
    elif menu_choice == 'e':
        print_list(even_integers(my_list))
    elif menu_choice == 'a':
        add_integer(my_list)
    else:
        print("Invalid option")
        break
    menu_choice = print_menu()
