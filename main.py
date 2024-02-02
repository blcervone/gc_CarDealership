# from vehicle_classes import *
# Create two lists: bikes, and trucks. Create at least 3 instances of both subclasses and store in the appropriate list.
# Create an empty list named vehicles_to_compare and fill with the user’s selection(s).
# Define system functions
    # get_menu_choice_validate() - gets user input for the main menu choice and validates it
    # compare_choice_validate() - asks the user if theyre ready to compare vehicles and validates their response
    # vehicle_choice_validate() - asks the user for the number vehicle they want to add to their compare list and validates the number is in the list shown
    # append_selection() - appends the selected vehicle to the vehicles_to_compare list
    # print_info() - prints the vehicle compare list with some formatting

# Set keep_going = True
# Print welcome message
# Start a while loop based on keep_going condition
# Call get_menu_choice_validate and store valid response in a variable
# IF menu choice == 'b'
    # print list of inventory bikes
    # Prompt user to compare now or not
    # call compare_choice_validate and store valid responsee in a variable
    # IF compare_choice == 'y'
        # Prompt user to select a vehicle from the list
        # call vehicle_choice_validate and store valid response in variable
        # call append_selection
        # Prompt user to compare now or later
            # If now, call print_info and exit program with exit message
            # else pass
    # else: pass
# IF menu choice == 't'
    # print list of inventory trucks
    # Prompt user to compare now or not
    # call compare_choice_validate and store valid responsee in a variable
    # IF compare_choice == 'y'
        # Prompt user to select a vehicle from the list
        # call vehicle_choice_validate and store valid response in variable
        # call append_selection
        # Prompt user to compare now or later
            # If now, call print_info and exit program with exit message
            # else pass
    # else: pass

# ==================================================================================================================== #

from vehicle_classes import *

b1 = Motorcycle("Harley", 0, 50000, 300)
b2 = Motorcycle("Ducati", 1000, 55000, 250)
b3 = Motorcycle("Honda", 20000, 20000, 240)

t1 = Truck("Toyota", 10000, 30000)
t2 = Truck("Ford", 200000, 5000)
t3 = Truck("Chevy", 50000, 20000)

bike_list = [b1, b2, b3]
truck_list = [t1, t2, t3]

vehicles_to_compare_list = []

def get_menu_choice_validate():
    menu_choice = input("Would you like to view our bikes or trucks? Input 'b' for bikes, 't' for trucks >")
    if menu_choice != 'b' and menu_choice != 't':
        print("Invalid selection!")
        get_menu_choice_validate()
    else:
        return menu_choice

def compare_choice_validate():
    compare_yn = input(" >")
    if compare_yn == 'y' or compare_yn == 'n':
        return compare_yn
    else:
        print("Invalid input!")
        compare_choice_validate()

def vehicle_choice_validate(list):
    try:
        vehicle_selection = int(input("Which vehicle would you like to compare? (please select a number from the list) >"))
        if vehicle_selection not in range(1, len(list) + 1):
            print("Invalid selection!")
            vehicle_choice_validate(list)
        else:
            return vehicle_selection
    except:
        print("Invalid input! Must be a digit from the list!")
        vehicle_choice_validate(list)


def append_selection(new_list, orig_list, vehicle_choice):
    new_list.append(orig_list[vehicle_choice - 1])
    print(f"{new_list[len(new_list)-1].make} added!")


def print_compare():
    print("Here are your vehicles to compare:")
    for vehicle in vehicles_to_compare_list:
        print(vehicle.__str__())
        noise = vehicle.make_noise()
        print(noise)
    print("Thank you and have a nice day!")


# ==================================================================================================================== #
# START PROGRAM

keep_going = True

print("""
Hello!
Welcome to GC Bikes & Trucks!""")

while keep_going:
    menu_choice = get_menu_choice_validate()
    if menu_choice == 'b':
        for bike in bike_list:
            print(f"{bike_list.index(bike) + 1}. {bike}")
        print("Would you like to compare one of these vehicles today? (y or n) >")
        compare_choice1 = compare_choice_validate()
        if compare_choice1 == 'y':
            vehicle_choice = vehicle_choice_validate(bike_list)
            append_selection(vehicles_to_compare_list, bike_list, vehicle_choice)
            print("Would you like to compare your vehicles now? (y or n)")
            compare_now = compare_choice_validate()
            if compare_now == 'y':
                print_compare()
                keep_going = False
            else:
                pass
        else:
            pass

    else:
        for truck in truck_list:
            print(f"{truck_list.index(truck) + 1}. {truck}")
        print("Would you like to compare one of these vehicles today? (y or n) >")
        compare_choice2 = compare_choice_validate()
        if compare_choice2 == 'y':
            vehicle_choice2 = vehicle_choice_validate(truck_list)
            append_selection(vehicles_to_compare_list, truck_list, vehicle_choice2)
            print("Would you like to compare your vehicles now? (y or n)")
            compare_now = compare_choice_validate()
            if compare_now == 'y':
                print_compare()
                keep_going = False
            else:
                pass
        else:
            pass

