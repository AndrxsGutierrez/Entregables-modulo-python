def validate_int(prompt, min_value=None, max_value=None):
    #Validate that the input is an integer and optionally within a min and max range.
    while True:
        value = input(prompt).strip()
        if not value.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue
        value = int(value)
        
        if min_value is not None and value < min_value:
            print(f"Number must be at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Number must be at most {max_value}.")
            continue
        return value

def validate_float(prompt, min_value=None, max_value=None):
    #Validate that the input is a float and optionally within a min and max range.
    while True:
        value = input(prompt).strip()
        try:
            value = float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        if min_value is not None and value < min_value:
            print(f"Number must be at least {min_value}.")
            continue

        if max_value is not None and value > max_value:
            print(f"Number must be at most {max_value}.")
            continue
        return value