def is_positive_number(s):
    """
    function checking if variants positive float
    """
    # if variant is positive float > true; else F
    try:
        if float(s) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def input_validation(user_input):
    """
    function for checking input data format
    """

    # split
    parts = [x.strip() for x in user_input.split(",") if x.strip != ""]
    # elements counting check
    if len(parts) not in (5,6):
        print(f"Expected 5 or 6 values, but got {len(parts)}.")
        return False

    else:
        # variant counting the correct numbers
        chk_count = 0

        ## ==== check each variants ====
        if is_positive_number(parts[0]):
            chk_count += 1
        else:
            print(f"Wind speed value: {parts[0]} is invalid format.")
        
        if is_positive_number(parts[1]):
            chk_count += 1
        else:
            print(f"Rated power value: {parts[1]} is invalid format.")
        
        if is_positive_number(parts[2]):
            chk_count += 1
        else:
            print(f"Cut-in wind speed value: {parts[2]} is invalid format.")
        
        if is_positive_number(parts[3]):
            chk_count += 1
        else:
            print(f"Rated wind speed value: {parts[3]} is invalid format.")
        
        if is_positive_number(parts[4]):
            chk_count += 1
        else:
            print(f"Cut-out wind speed value: {parts[4]} is invalid format.")
        
        # mode input validation
        if len(parts)==6:
            if parts[5] not in ('linear','L','l','cubic','C','c'):
                print(f"Interpolation option:{parts[5]} is invalid format.")
                return False
        ## =======================================

    # chk_count must be 5 for each numeric parameters check
    if chk_count == 5:
        return True
    else:
        return False

def P_linear_mode(ws,p_rated,ws_cin,ws_rated,ws_cout):
    # linear mode power output equation
    return ( (ws - ws_cin) / (ws_rated - ws_cin) ) * p_rated

def P_cubic_mode(ws,p_rated,ws_cin,ws_rated,ws_cout):
    # cubic mode power output equation
    return ( pow(ws,3) / pow(ws_rated,3) ) * p_rated

def Power_Output(ws,p_rated,ws_cin,ws_rated,ws_cout,mode="linear"):
    """
    Power Output main function
    """
    #detect the mode first; then if ws less than ws_rated output =0; greater >> output = p_rated; within >> call mode_output function
    if mode == "linear" or mode == "l" or mode == "L":
        if ws < ws_cin or ws >= ws_cout :
            return 0
        elif ws >=ws_rated:
            return p_rated
        else:
            return P_linear_mode(ws,p_rated,ws_cin,ws_rated,ws_cout)
    elif mode == "cubic" or mode == "c" or mode == "C":
        if ws < ws_cin or ws >= ws_cout:
            return 0
        elif ws >=ws_rated:
            return p_rated
        else:
            return P_cubic_mode(ws,p_rated,ws_cin,ws_rated,ws_cout)
    else:
        print("Hum... I'm not sure how you bypassed the data validation... My bad...")


