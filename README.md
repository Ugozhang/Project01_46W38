# Project01_46W38
The project 01 for 46W38, which for calculating Power output with wind speed input.

## Reference
Based on [46W38_Project01] (https://github.com/ju-feng-dk/46W38-2025-Projects/blob/main/Project_01/README.md).

## structure
main.py includes the input funciton, format transformation of input, and output function
wind_energy_power.py includes the validation functions, calculation functions

### instruction
Please enter the following parameters in order:
Wind Speed, rated power, cut-in wind speed, rated wind speed, cut-out wind speed, (Interpolation option, optional)
(ws, p_rated, ws_cin, ws_rated, ws_cout, (mode))
- Use commas (,) to seperate each value
- Use a period (.) as the decimal point.
- Avoid including spaces between entries.
- Interpolation option: 'linear' or 'cubic'

Example:
12.1,12,4,11,16,linear
