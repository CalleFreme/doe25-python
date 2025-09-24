
def print_menu(menu_choice_number, message_string):
    choice_is_valid = int(menu_choice_number) in [1, 2, 3, 4] # Vi kontrollerar att valet är giltigt
    if not choice_is_valid:
        print("Invalid choice.")
        return  # Avslutar funktionen om valet är ogiltigt
    print(f"You selected option {menu_choice_number}. {message_string}")

menu_is_running = True

volume = 5

while menu_is_running:
    menu_choice = input("Enter a choice (1-3. 4 to quit)): ")
    
    #message_string = "You selected option "

    if menu_choice == '1':
        print_menu(menu_choice, "TV Settings")
        #message_string += f"{menu_choice}. TV Settings" # Konkatenerar sträng
    elif menu_choice == '2':
        print_menu(menu_choice, "Choose channel")
        #message_string += f"{menu_choice}. Choose channel"
    elif menu_choice == '3':
        valid_volume = False
        while not valid_volume:
            print(f"Volume is {volume}")
            print_menu(menu_choice, "Change volume")
            new_volume = input("Set volume 0-100. Enter e to exit: ")
            if new_volume == 'e':
                print("Returning to main menu...\n") 
                #print()
                break
            elif new_volume.isnumeric() and 0 <= int(new_volume) <= 100:
                volume = int(new_volume)
                print(f"Volume set to {volume}")
                valid_volume = True
            else:
                print("Volume must be between 0-100")
                continue
            #message_string += f"{menu_choice}. Change volume"

    elif menu_choice == '4':
        print_menu(menu_choice, "Turning off TV")
        #message_string += f"{menu_choice}. Turning off TV"
        break
    else:
        print("Invalid choice. Please choose a number 1-4.")
        continue
    
    #print(message_string)
    
print("Program exited.")
