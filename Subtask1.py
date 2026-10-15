# Subtask 1: Data Analysis Application
# This program reads component data from a file
# and displays components that start with a letter
# entered by the user.

search_letter = input("Enter a letter between A and Z: ").strip().lower()

if len(search_letter) != 1 or not search_letter.isalpha():
    print("Invalid input. Please enter a single letter.")
else:

    try:
        # Open the component data file
        with open("components_data.txt", "r") as file:

            found = False

            # Read each line in the file
            for line in file:

                # Remove spaces and the newline
                line = line.strip()

                # Ignore empty lines
                if not line:
                    continue

                # Separate component ID and voltage
                try:
                    component_id, voltage = line.split(",", 1)

                    # Remove unnecessary spaces
                    component_id = component_id.strip()
                    voltage = voltage.strip()

                    # Check if the component ID starts
                    # with the letter entered by the user
                    if component_id.lower().startswith(search_letter):
                        print("Component ID:", component_id)
                        print("Voltage:", voltage)
                        print("--------------------")

                        found = True

                except ValueError:
                    # Ignore lines that do not contain a comma
                    continue

            # Display message if there were no matches
            if not found:
                print("No components were found with IDs starting with",
                      search_letter.upper() + ".")

    except FileNotFoundError:
        print("Error: components_data.txt could not be found.")