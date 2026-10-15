# Subtask 2: Enhanced Data Processing with Input Validation
# This program checks component data for errors
# and records invalid entries in error_log.txt.


# Validation function
def validate_component(component_id, voltage):
    """
    Checks whether the component ID and voltage are valid.

    A valid component ID:
    - Contains only letters and numbers
    - Is exactly 4 characters long

    A valid voltage:
    - Is present
    - Is numeric
    """

    # Check component ID length
    if len(component_id) != 4:
        return False

    # Check that the component ID contains
    # only letters and numbers
    if not component_id.isalnum():
        return False

    # Check that voltage is not empty
    if voltage == "":
        return False

    # Check that voltage is numeric
    try:
        float(voltage)
    except ValueError:
        return False

    return True


# Open the input file and error log
try:

    with open("components_data_ERR.txt", "r") as input_file, \
         open("error_log.txt", "w") as error_file:

        invalid_count = 0

        # Read each line
        for line_number, line in enumerate(input_file, start=1):

            line = line.strip()

            # Check for an empty line
            if not line:
                invalid_count += 1
                error_file.write(
                    f"Line {line_number}: Empty line.\n"
                )
                continue

            # Separate component ID and voltage
            try:
                component_id, voltage = line.split(",", 1)

                component_id = component_id.strip()
                voltage = voltage.strip()

            except ValueError:
                invalid_count += 1

                error_file.write(
                    f"Line {line_number}: Invalid format - "
                    f"missing comma or data.\n"
                )
                continue

            # Check component ID
            if len(component_id) != 4:
                invalid_count += 1

                error_file.write(
                    f"Line {line_number}: Component ID must "
                    f"be exactly 4 characters long.\n"
                )

                continue

            if not component_id.isalnum():
                invalid_count += 1

                error_file.write(
                    f"Line {line_number}: Component ID must "
                    f"contain only letters and numbers.\n"
                )

                continue

            # Check voltage
            if voltage == "":
                invalid_count += 1

                error_file.write(
                    f"Line {line_number}: Voltage reading is missing.\n"
                )

                continue

            try:
                float(voltage)

            except ValueError:
                invalid_count += 1

                error_file.write(
                    f"Line {line_number}: Voltage reading "
                    f"must be numeric.\n"
                )

                continue

        # Display final result
        if invalid_count == 0:
            print("components_data.txt is free of errors.")
            print("Development can continue.")
        else:
            print(
                invalid_count,
                "invalid entries found. "
                "Please check error_log.txt for details."
            )

except FileNotFoundError:
    print("Error: components_data_ERR.txt could not be found.")