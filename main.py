import wind_energy_power as wep
import sys

# ==== Trim and transformat Input format ====
def input_transform(User_Input):
    """
    Use for transforming string reading Input into list of 5 numerics (and 1 mode element)
    """
    parts = []
    for x in User_Input.split(","):
        x = x.strip()
        if x == "":
            continue
        try:
            parts.append(float(x))
        except ValueError:
            parts.append(x)
    return parts
# ========================================

def info_and_example():
    """
    Function show instruction and Give an example
    """
    # Paragrath for Input instruction
    instruction = """
    Please enter the following parameters in order:
    Wind Speed, rated power, cut-in wind speed, rated wind speed, cut-out wind speed, (Interpolation option, optional)
    - Use commas (,) to seperate each value.
    - Use a period (.) as the decimal point.
    - Avoid including spaces between entries.
    - Interpolation option: 'linear' or 'cubic'.
    """
    print(instruction)
    # Example 
    test_exp = "10.9,12,4,11,16,linear"
    parts = input_transform(test_exp)
    print(f"Example:\nYour Input :{test_exp}\nPower Output is {wep.Power_Output(*parts):.2f} MW.\n-----------------")

# ==== Gain Input function ====
# Gain input value, call data validation function till the proper format
# do-while structure
info_and_example()
User_Input = input("Your Input (or 'end' for closing program):")
if User_Input in ("end","exit"):
    sys.exit()
elif User_Input in ("info","?"):
    info_and_example()

while wep.input_validation(User_Input)==False:
    User_Input = input("Your Input (or 'end' for closing program; 'info' for instruction):")
    if User_Input in ("end","exit"):
        sys.exit()
    elif User_Input in ("info","?"):
        info_and_example()
#============================================================================

# ==== Print out the power output result ====
parts = input_transform(User_Input)
print(f"Power Output is {wep.Power_Output(*parts):.2f} MW.")
# ========================================



