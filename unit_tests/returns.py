def calculate_return(current_value, previous_value):
    # Return 0 when there is no previous value, to avoid dividing by zero
    if previous_value == 0:
        return 0.0
    return current_value / previous_value - 1