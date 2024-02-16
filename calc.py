# calc.py
import math


def calculate(current_value, num, clear):
    if clear:
        return ''  # Clear the current value if clear button is pressed
    elif num:
        if num == 'sqrt':
            return math.sqrt(current_value)
        if num == '=':
            # Calculate result if '=' is pressed
            try:
                # Safely evaluate the current expression
                return str(eval(current_value))
            except:
                return 'Error'
        else:
            if num == "^":
                bepis = math.pow(int(current_value), 2)
                return str(bepis)
            if num == "sqrt":
                bepis = math.pow(int(current_value), .5)
                return str(bepis)
            # Append the pressed button value to the current value
            return current_value + num
    return current_value
