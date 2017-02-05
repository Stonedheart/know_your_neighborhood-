from csvhandler import CsvHandler
from options import Options

class Menu:

    @classmethod
    def display_menu(cls):

        print("""
        What would you like to do:
        (1)List statistics
        (2)Display 3 cities with longest names
        (3)Display county's name with the largest number of communities
        (4)Display locations, that belong to more than one category
        (5)Advanced search
        (0)Exit program
        """)

    @classmethod
    def choose_option(cls):

        start = True
        valid_choices = ["1", "2", "3", "4", "5", "0", "dupa"]
        while start:

            menu = Menu.display_menu()
            user_choice = input("Choose option: ")
            main_list_from_csv = CsvHandler.read_from_csv("malopolska.csv")

            if user_choice in valid_choices:

                if user_choice == "1":
                    statistics = Options.list_statistics(main_list_from_csv)
                    CsvHandler.print_table(statistics, ["Małopolska"])

                elif user_choice == "2":
                    three_cities = Options.three_cities_with_longest_name(main_list_from_csv)
                    CsvHandler.print_table(three_cities, [""])

                elif user_choice == "3":
                    county = Options.county_with_largest_num_of_communities(main_list_from_csv)
                    print(county)

                elif user_choice == "4":
                    locations = Options.locations_with_more_than_one_category(main_list_from_csv)
                    CsvHandler.print_table(locations, [""])

                elif user_choice == "5":
                    to_find = input("What would You like to find: ")
                    adv = Options.advanced_searching(main_list_from_csv, to_find)
                    CsvHandler.print_table(adv, [""])
                elif user_choice == "0":
                    start = False

                elif user_choice == "dupa":
                    print("Do you mean Dupadu, Andhra Pradesh, Indie?")
            else:
                print("Invalid input, try again")