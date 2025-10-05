import wind_energy_power as wep
import sys

# ==== Paragrath for Input instruction ====
instruction = """
Please enter the following parameters in order:
Wind Speed, rated power, cut-in wind speed, rated wind speed, cut-out wind speed, (Interpolation option, optional)
- Use commas (,) to seperate each value
- Use a period (.) as the decimal point.
- Avoid including spaces between entries.
- Interpolation option: 'linear' or 'cubic

Example:
12.1,12,4,11,16,linear
===================================================================================================================
"""
# ================================================

# ==== Gain Input function ====
# Gain input value, call data validation function till the proper format
# do-while structure
print(instruction)
User_Input = input("Your Input (or 'end' for closing program):")
if User_Input in ("end","exit"):
    sys.exit()
elif User_Input in ("info","?"):
    print(instruction)

while wep.input_validation(User_Input)==False:
    User_Input = input("Your Input (or 'end' for closing program; 'info' for instruction):")
    if User_Input in ("end","exit"):
        sys.exit()
    elif User_Input in ("info","?"):
        print(instruction)
#============================================================================

# ==== Trim and transformat Input for calling calculation function ====
parts = []
for x in User_Input.split(","):
    x = x.strip()
    if x == "":
        continue
    try:
        parts.append(float(x))
    except ValueError:
        parts.append(x)
# ========================================

# ==== Print out the power output result ====
print(f"Power Output is {wep.Power_Output(*parts)}.")
# ========================================



